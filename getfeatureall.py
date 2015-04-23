import math
fname = "train_info.txt";
fin = open(fname, "r");
user_feature = {};
item_feature = {};
for line in fin:
	words = line[0:-1].split("\t");
	user = int(words[0]);
	item = int(words[1]);
	for i in range(4, len(words)):
		feature = int(words[i]);
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
		
		
fout = open("user_feature.txt", "w");
for user in user_feature.keys():
	sum = 0;
	for feature in user_feature[user].keys():
		sum += user_feature[user][feature];
	for feature in user_feature[user].keys():
		num=float(user_feature[user][feature])/float(sum);
		line = str(user) + "\t" + str(feature) + "\t" + str(num) + '\n';
		fout.write(line);
fout.flush();
fout = open("item_feature.txt", "w");
for item in item_feature.keys():
	sum = 0;
	for feature in item_feature[item].keys():
		sum += item_feature[item][feature];
	for feature in item_feature[item].keys():
		num=float(item_feature[item][feature])/float(sum);
		line = str(item) + "\t" + str(feature) + "\t" + str(num) + '\n';
		fout.write(line);
fout.flush();