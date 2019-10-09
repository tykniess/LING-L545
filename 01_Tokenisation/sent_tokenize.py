import sys
from nltk import sent_tokenize

list = []

for line in sys.stdin:
	for sent in sent_tokenize(line, language = 'german'):
                list.append(sent)

for line in list:
        print (line + '\n')

#with open('newfile_segmented.txt', 'w') as file:
#	for item in list:
#		file.write('\n' + item)
