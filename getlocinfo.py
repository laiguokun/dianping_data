
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

user_map = {}
item_map = {}

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

fin = open("city_cnt.txt");
city_cnt = {}
for line in fin:
	words = line[0:-1].split('\t');
	city_cnt[words[0]] = words[1];
	
fin = open("reviews.txt", "r", encoding = "utf8");
fout_feature = open("info_city.txt","w");
user_home = {};
item_home = {}

jsondist = [];
cnt = 0;
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
			city = int(item[id]);
			review = tmp["content"];
			if (tmp["rate"] == -1):
				continue;
			if (not (tmp["userId"] in user_map)):
				user_map[tmp["userId"]] = len(user_map);
			user = user_map[tmp["userId"]];
			if (not (tmp["restId"] in item_map)):
				item_map[tmp["restId"]] = len(item_map);
			items = item_map[tmp["restId"]];
			if (not (user in user_home)):
				user_home[user] = {}
			if (not (city in user_home[user])):
				user_home[user][city] = 0;
			user_home[user][city] += 1; 
			if (not (items in item_home)):
				item_home [items] = city;
			line = str(user_map[tmp["userId"]]) + "\t" + str(item_map[tmp["restId"]]) + "\t" +str(tmp["rate"]) +'\t' +str(city);
			for w in lexicon.keys():
				if (w in review):
					line += "\t" + str(lexicon[w]);
			line +='\n';
			fout_feature.write(line);
			if (not(city in city_cnt)):
				city_cnt[city] = 0;
			city_cnt[city] +=1;
		else:
			cnt2 +=1;
	if (cnt % 10000 == 0):
		print(str(cnt)+" "+str(cnt2));
	cnt += 1;
print("cnt2:"+str(cnt));

fout= open("item_home.txt", "w");
for item in item_home.keys():
	fout.write(str(item) + '\t' + str(item_home[item]) + '\n');
print(cnt);