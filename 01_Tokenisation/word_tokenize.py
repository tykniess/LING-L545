import sys
from nltk import word_tokenize

list = []

for line in sys.stdin:
	for word in word_tokenize(line, language = 'german'):
                list.append(word)

#for line in list:
#        print (line + '\n')

#with open('newfile_segmented.txt', 'w') as file:
#	for item in list:
#		file.write('\n' + item)
