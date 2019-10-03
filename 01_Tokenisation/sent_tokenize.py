name = input('what is filename?')
from nltk import sent_tokenize

list = []

with open(name, 'r') as file:
	for line in file:
		sent_tokenize(line, language = 'german')
		list.append(line)

with open(name+'segmented.txt', 'w') as file:
	for item in list:
		file.write('\n' + item)
