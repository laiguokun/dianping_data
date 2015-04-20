import random;
fname = "rate_all.txt";
fin = open(fname, "r");
fname = "train.txt";
fout = open(fname, "w");
fout_test = open("test.txt", "w");
test = {}
for line in fin:
	words = line[0:-1].split("\t");
	user = words [0];
	item = words [1];
	r = random.random();
	if (r < 0.2):
		if (not(user in test.keys())):
			test[user] = [];
		test[user].append(item);
		fout_test.write(line);
	else:
		fout.write(line);
fname = "feature_all.txt";
fin = open(fname, "r");
fname = "train_feature.txt";
fout = open(fname, "w");
for line in fin:
	words = line[0:-1].split("\t");
	user = int(words[0]);
	item = int(words[1]);
	feature = int(words[2]);
	if (user in test.keys() and item in test[user]):
		continue;
	fout.write(line);