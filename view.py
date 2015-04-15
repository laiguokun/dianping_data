
import json
fin = open("dianping.lexicon-all", "r");
lexicon = {}
for line in fin:
	word = line[0:-1];
	lexicon[word] = len(lexicon);
citys = [];
fin = open("hascity.txt", "r");
for line in fin:
	words = line[0:-1].split('=');
	citys.append(words[1]);
fin = open("businesses.txt", "r", encoding = "utf8");
cnt = 0;
item = {}
for line in fin:
	ff = line.split('^');
	word = "";
	for i in range(1, len(ff)):
		word += ff[i];
	if (cnt != 0):
		tmp = json.loads(word);
		if (("2" in tmp) and (tmp["2"] in citys)):
			item[tmp["0"]] = tmp ["2"];
	cnt += 1;

fin = open("reviews.txt", "r", encoding = "utf8");
fout = open("view.txt", "w", encoding = "utf8"); 
cnt = 0;
for line in fin:
	ff = line.split('^');
	word = "";
	for i in range(1, len(ff)):
		word += ff[i];
	if (cnt != 0):
		tmp = (json.loads(word));
		id = str(tmp["restId"]);
		if (id in item.keys()):		
			city = item[id];
			if (city == 397):
				print(tmp["content"]);
				fout.write(tmp["content"]+'\n');
	if (cnt % 10000 == 0):
		print(str(cnt));
	cnt += 1;