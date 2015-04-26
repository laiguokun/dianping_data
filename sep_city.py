fin_train = open("train_info.txt");
fin_test = open("test_info.txt");

fout_train = {}
fout_test = {};
fout = open("city_id.txt","w");
for line in fin_train:
	words = line[0:-1].split('\t');
	city = words[3];
	if (not(city in fout_train)):
		fout_train[city] = open("city\\"+city+"_train.txt","w");
	fout_train[city].write(words[0] + '\t' + words[1] + '\t' +words[2] + '\n');

test_cnt = {}
for line in fin_test:
	words = line[0:-1].split('\t');
	city = words[3];
	if (not(city in fout_test)):
		fout_test[city] = open("city\\"+city+"_test.txt","w");
		test_cnt[city] = 0;
	test_cnt[city] += 1;
	fout_test[city].write(words[0] + '\t' + words[1] + '\t' +words[2] + '\n');

for city in test_cnt.keys():
	fout.write(city + '\t' + str(test_cnt[city]) + '\n');