import nltk
#unigram tagger requires two arguments: a training corpus and a test corpus

import sys
from nltk import word_tokenize
from nltk import pos_tag
import csv
trained = []
correctly_tagged = 0
incorrectly_tagged = 0

#sys.argv[1] is the filename of training corpus
#sys.argv[2] is the filename of the test corpus

with open(sys.argv[1], 'r') as csv_file: #to be able to reference columns later
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for line in csv_reader: #go through the training corpus
        if len(line) == 0: #empty line
            pass
        elif len(line) == 1: # sentence id or text
            pass
        else:
            entry = line[1], line[3]
            trained.append(entry) #tagged token: get token and tag as tuple

#now we have a simple list of unigrams and POS.
with open(sys.argv[2], 'r') as csv_file: #to be able to reference columns later
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    for line in csv_reader:
        if len(line) == 0: #empty line
            pass
        elif len(line) == 1: # sentence id or text
            pass
        else:
            #now we are looking at test data. column 2 is the word to be analyzed
            #cycle through trained and look for unigram
            for tup in trained:
                if tup[0] == line[1]:
                    if tup [1] == line[3]:
                        correctly_tagged = correctly_tagged + 1
                        break
                    else:
                        incorrectly_tagged = incorrectly_tagged + 1
                incorrectly_tagged = incorrectly_tagged + 1

print('correctly tagged: '+str(correctly_tagged)+'\nincorrectly tagged: '+ \
      str(incorrectly_tagged))

print("That's an accuracy of " + str(correctly_tagged/(correctly_tagged+incorrectly_tagged)) + "%")
