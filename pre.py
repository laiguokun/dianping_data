
import json

fin = open("dianping.lexicon", "r");
lexicon = {}
for line in fin:
	word = line[0:-1];
	lexicon[word] = len(lexicon);
citys = [];
fin = open("hascity.txt", "r");
for line in fin:
	words = line[0:-1].split('=');
	citys.append(words[1]);
fin = open("businesses.txt", "r", encoding = "utf8");
cnt = 0;
item = {}
for line in fin:
	ff = line.split('^');
	word = "";
	for i in range(1, len(ff)):
		word += ff[i];
	if (cnt != 0):
		tmp = json.loads(word);
		if (("2" in tmp) and (tmp["2"] in citys)):
			item[tmp["0"]] = tmp ["2"];
	cnt += 1;

fin = open("reviews.txt", "r", encoding = "utf8");
fout = open("city-feature.100.txt", "w");
jsondist = [];
cnt = 0;
city_feature = {};
city_cnt = {};
cnt2 = 0;
print (len(item));
for line in fin:
	ff = line.split('^');
	word = "";
	for i in range(1, len(ff)):
		word += ff[i];
	if (cnt != 0):
		tmp = (json.loads(word));
		id = str(tmp["restId"]);
		if (id in item.keys()):		
			city = item[id];
			review = tmp["content"];
			if (not(city in city_cnt)):
				city_cnt[city] = 0;
			city_cnt[city] += 1;
			for w in lexicon.keys():
				if (w in review):
					if (not (city in city_feature)):
						city_feature[city] = {};
					if (not (lexicon[w] in city_feature[city])):
						city_feature[city][lexicon[w]] = 0;
					city_feature[city][lexicon[w]] += 1;
		else:
			cnt2 +=1;
	if (cnt % 10000 == 0):
		print(str(cnt)+" "+str(cnt2));
	cnt += 1;
print("cnt2:"+str(cnt));
realcity = []
for city in city_feature.keys():
	if (city_cnt[city] < 1000):
		continue;
	realcity.append(city);
	for feature in city_feature[city].keys():
		line = str(city) + "\t" + str(feature) + "\t" + str(float(city_feature[city][feature])/float(city_cnt[city])) + "\n";
		fout.write(line);
fout = open("existcity.100.txt","w");
for city in realcity:
	fout.write(str(city)+ "\n");
fin.close();
fout.close();
