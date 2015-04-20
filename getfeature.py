import math
fin = open("hascity.txt", "r");
citys = []
for line in fin:
	words = line[0:-1].split('=');
	citys.append(words[1]);

for city in citys:
	fname = "city_feature\\" + city + "_train_feature.txt";
	fin = open(fname, "r");
	user_feature = {};
	item_feature = {};
	for line in fin:
		words = line[0:-1].split("\t");
		user = int(words[0]);
		item = int(words[1]);
		feature = int(words[2]);
		if (not(user in user_feature.keys())):
			user_feature[user] = {};
		if (not(feature in user_feature[user].keys())):
			user_feature[user][feature] = 0;
		user_feature[user][feature] += 1;
		if (not(item in item_feature.keys())):
			item_feature[item] = {};
		if (not(feature in item_feature[item].keys())):
			item_feature[item][feature] = 0;
		item_feature[item][feature] += 1;
	fout = open("city_feature\\" + city + "_user_feature.txt", "w");
	for user in user_feature.keys():
		for feature in user_feature[user].keys():
			num=(1.0/(1.0+math.exp(-user_feature[user][feature])))*4+1;
			line = str(user) + "\t" + str(feature) + "\t" + str(num) + '\n';
			fout.write(line);
	fout.flush();
	fout = open("city_feature\\" + city + "_item_feature.txt", "w");
	for item in item_feature.keys():
		for feature in item_feature[item].keys():
			num=(1.0/(1.0+math.exp(-item_feature[item][feature])))*4+1;
			line = str(item) + "\t" + str(feature) + "\t" + str(num) + '\n';
			fout.write(line);
	fout.flush();