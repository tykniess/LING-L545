import sys #needed for standard input and sys.argv
from nltk import sent_tokenize #needed to tokenize

###########################
#Stage 1: sent tokenisation
l1 = [] #new list for lines
l2 = [] #output list
for line in sys.stdin:
        for sent in sent_tokenize(line, language = 'german'):
                l1.append(sent)
	
print ("#####\nYour file is " + str(len(l1))+ " sentences long!\n#####")

###########################
#Stage 2: word/character tokenisation (Japanese)

for line in l1:
        i=0
        with open('ja_dict.txt','r') as dict:
                for entry in dict:
                        if line[:len(line)-i] in entry:
                                l2.append(line)
                                break #go to next line?
                        else:
                                i=i+1
print(len(l2))
for line in l2:
        print(line)
        


#adding the dictionary argument
print ("#####\nYour script has the following arguments: " + str(sys.argv))
