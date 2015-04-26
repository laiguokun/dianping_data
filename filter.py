import random;
fin = open("city_cnt.txt");
city_cnt = {}
city_feature = {}
for line in fin:
	words = line[0:-1].split('\t');
	city_cnt[words[0]] = words[1];
	city_feature[words[0]] = {}
fin = open("info_city_before.txt", "r");
fout = open("info_city.txt","w");
sample = 0.1;
for line in fin:
	words = line[0:-1].split('\t');
	city = words[3];
	if (int(city_cnt[city]) > 1000):
		r = random.random();
		if (r < 0.1):
			fout.write(line);