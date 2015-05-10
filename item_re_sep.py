import random;
fin = open("user_home.txt");
user_home = {}
for line in fin:
	words = line[0:-1].split('\t');
	user_home[words[0]] = words[1];

fin = open("info_city.txt", "r")
fout = open("train_info.txt", "w");
fout_test = open("test_info.txt","w");
user_cnt = {}
user_rate = {}
for line in fin:
	words = line[0:-1].split('\t');
	user = words[0];
	if (user_home[user] != words[3]):
		continue;
	if (len(user_cnt) < 200):
		if (not(user in user_cnt)):
			user_cnt[user] = 0;
	if ((user in user_cnt) and words[3] == user_home[user]):
		user_cnt[user] += 1;
test_set = {}
for user in user_cnt.keys():
	user_rate[user] = user_cnt[user] - 10;
	print(user_cnt[user]);
	test_set[user] = 0;
fin = open("info_city.txt","r");
for line in fin:
	words = line[0:-1].split('\t');
	user = words[0];
	item = words[1];
#	print (user_home[user]);
	if (not(user in user_cnt) or words[3] != user_home[user]):
		fout.write(line);
		continue;
	if (user_cnt[user] <= 20):
		fout.write(line);
		continue;
	r = random.random();
	if (test_set[user] < 10 and r < 10.0/float(user_cnt[user])):
		fout_test.write(line);
		test_set[user] += 1;
		continue;
	if (user_rate[user] <= 0):
		fout_test.write(line);
		continue;
	fout.write(line);
	user_rate[user] -= 1;
		