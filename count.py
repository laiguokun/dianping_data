fin = open("city-feature.txt", "r");
ff = [];
feature_num = 109;
for i in range(0,feature_num):
	ff.append(open("feature//" + str(i) + ".txt", "w"));
avg = {};
cnt = {};
var = {};
for i in range(0,feature_num):
	avg[i] = 0.0;
	cnt[i] = 0.0;
	var[i] = 0.0;
max = 0;
for line in fin:
	words = line[0:-1].split("\t");
	avg[int(words[1])] += float(words[2]);
	cnt[int(words[1])] += 1;
	ff[int(words[1])].write(words[0] + " " + words[2] + '\n');
	if (int(words[0]) > max):
		max = int(words[0]);

print(max);

for i in range(0, feature_num):
	avg[i] = avg[i] / cnt[i];
fin = open("city-feature.txt", "r");
for line in fin:
	words = line[0:-1].split("\t");
	a = avg[int(words[1])];
	b = float(words[2]);
	var[int(words[1])] += (b-a) * (b-a);
#	print(var[int(words[1])]);
#print(var);
for i in range(0,feature_num):
	var[i] = var[i] / cnt[i];
s = sorted(var.items(), key = lambda asd:asd[1], reverse = True)
for i in range(0,10):
	print(str(s[i][0]) + "\t" + str(s[i][1]));