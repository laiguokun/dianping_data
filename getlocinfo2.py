fin = open("city_cnt.txt");
city_cnt = {}
city_feature = {}
for line in fin:
	words = line[0:-1].split('\t');
	city_cnt[words[0]] = words[1];
	city_feature[words[0]] = {}
	
fin = open("train_info.txt", "r");
for line in fin:
	words = line[0:-1].split('\t');
	city = words[3];
	if (not(words[3] in city_feature)):
		city_feature[words[3]] = {};
	for i in range(4,len(words)):
		feature = words[i];
		if (not(feature in city_feature[words[3]])):
			city_feature[words[3]][feature] = 0;
		city_feature[words[3]][feature] += 1;

fout = open("loc_feature.txt", "w");	
for city in city_cnt.keys():
	for feature in city_feature[city].keys():
		ratio = float(city_feature[city][feature])/float(city_cnt[city]);
		fout.write(str(city) + '\t' + str(feature) + '\t' + str(ratio) + '\n');
		