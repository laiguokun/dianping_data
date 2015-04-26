fin = open("info_city.txt");
fout = open("user_home.txt","w");
user_city = {};
for line in fin:
	words = line[0:-1].split('\t');
	if (not(words[0] in user_city)):
		user_city[words[0]] = {};
	if (not(words[3] in user_city[words[0]])):
		user_city[words[0]][words[3]] = 0;
	user_city[words[0]][words[3]] += 1;

for user in user_city.keys():
	max = 0;
	max_aug = '';
	for city in user_city[user].keys():
		if (user_city[user][city] > max):
			max = user_city[user][city];
			max_aug = city;
	fout.write(user + '\t' + max_aug + '\n');