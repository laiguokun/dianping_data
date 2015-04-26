fin = open("user_home.txt");
user_home = {}
for line in fin:
	words = line[0:-1].split('\t');
	user_home[words[0]] = words[1];

fin = open("info_city.txt", "r")
fout = open("train_info.txt", "w");
fout_test = open("test_info.txt","w");
user_cnt = {}
for line in fin:
	words = line[0:-1].split('\t');
	user = words[0];
	if (not(user in user_cnt)):
		user_cnt[user] = 0;
	user_cnt[user] += 1;
user_test_cnt = {}
fin = open("info_city.txt");
for line in fin:
	words = line[0:-1].split('\t');
	user = words[0];
	city = words[3];
	if (user_cnt[user] <= 25):
		fout.write(line);
		continue;
	if (city != user_home[user]):
		continue;
	if (not(user in user_test_cnt)):
		user_test_cnt [user] = 0;
	user_test_cnt [user] += 1;
	if (user_test_cnt[user] <= 10):
		fout_test.write(line);
	else:
		fout.write(line);