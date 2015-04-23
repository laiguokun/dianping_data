fin = open("info_city.txt", "r");
city_feature = {}
city_cnt = {}
for line in fin:
	words = line[0:-1].split('\t');
	if (not(words[3] in city_feature)):
		city_feature[words[3]] = {};
	if (not(words[2] in city_feature[words[3]])):
		city_feature[words[3]][words[2]] = 0;
	city_feature[words[3]][words[2]] += 1;
	if (not(words[3] in city_cnt)):
		city_cnt[words[3]] = 0;
	city_cnt[words[3]] += 1;

fout = open("city_feature.txt", "w");	
for city in city_cnt.keys():
	for feature in city_feature[city].keys():
		ratio = float(city_feature[city][feature])/float(city_cnt[city]);
		fout.write(str(city) + '\t' + str(feature) + '\t' + str(ratio) + '\n');
		