import sys #needed for standard input and sys.argv
import ssl
from nltk import sent_tokenize #needed to tokenize

###########################
#Stage 1: sent tokenisation
l1 = [] #new list for lines
for line in sys.stdin:
#        for sent in sent_tokenize(line, language = 'japanese'):
###Had to scrap tokenisation because PUNKT doesn't have japanese.pickle
        l1.append(line)
	

###########################
#Stage 2: word/character tokenisation (Japanese)

#2a: create list of possible maxmatch types
l2=[]
i=0
firstword = ''
remainder = ''
ja_dict = []
with open('ja_dict.txt','r') as file:
        for line in file:
                ja_dict.append(line)
print('your dictionary has ' + str(len(ja_dict)) + ' entries')

for sent in l1:
        if sent == '':
                break
        else:
                i = len(sent)
                while i > 0:
                        firstword = sent[:i]
                        remainder = sent[i:]
                        print('first word is ' + firstword)
                        print('remainder is ' + remainder)
                        print('i is now '+str(i))

                        for entry in ja_dict:
                                if firstword in entry:
                                        print('###we have a match')
                                        l2.append(entry)
                                        break
                        i=i-1
                break

print ('your maxmatch output is: ' + str(l2))


print ("#####\nYour script has the following arguments: " + str(sys.argv))


