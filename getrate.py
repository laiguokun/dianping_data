
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

user_map = {}
item_map = {}

fin = open("reviews.txt", "r", encoding = "utf8");
fout_rate = {};
fout_feature = {};
for city in citys:
	fout_rate[int(city)] = (open("city_rate\\" + str(city) + "_rate.txt", "w"));
	fout_feature[int(city)] = (open("city_feature\\" + str(city) +"-feature.txt", "w"));
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
			if (tmp["rate"] == -1):
				continue;
			if (not (tmp["userId"] in user_map)):
				user_map[tmp["userId"]] = len(user_map);
			if (not (tmp["restId"] in item_map)):
				item_map[tmp["restId"]] = len(item_map);
			fout_rate[int(city)].write(str(user_map[tmp["userId"]]) + "\t" + str(item_map[tmp["restId"]]) + "\t" + str(tmp["rate"]) + '\n');
			
			for w in lexicon.keys():
				if (w in review):
					fout_feature[int(city)].write(str(user_map[tmp["userId"]]) + "\t" + str(item_map[tmp["restId"]]) + "\t" + str(lexicon[w]) + '\n');
			
		else:
			cnt2 +=1;
	if (cnt % 10000 == 0):
		print(str(cnt)+" "+str(cnt2));
	cnt += 1;
print("cnt2:"+str(cnt));
for city in citys:
	fout_rate[int(city)].flush();
	fout_feature[int(city)].flush();
