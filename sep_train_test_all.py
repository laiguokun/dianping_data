import random;
fname = "info_city.txt";
fin = open(fname, "r");
fname = "train_info.txt";
fout = open(fname, "w");
fout_test = open("test_info.txt", "w");
test = {}
for line in fin:
	words = line[0:-1].split("\t");
	user = words [0];
	item = words [1];
	r = random.random();
	if (r < 0.2):
		fout_test.write(line);
	else:
		fout.write(line);