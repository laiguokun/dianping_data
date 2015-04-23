fin = open("train_info.txt");
fout = open("train.txt" ,"w");
for line in fin:
	words= line[0:-1].split('\t');
	output = words[0] + '\t' + words[1] + '\t'+ words[2] + '\n';
	fout.write(output);
fin = open("test_info.txt");
fout = open("test.txt" ,"w");
for line in fin:
	words= line[0:-1].split('\t');
	output = words[0] + '\t' + words[1] + '\t'+ words[2] + '\n';
	fout.write(output);