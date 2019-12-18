#This script extracts information on object-verb order from train.conllu file(s)
#and prints the information in a legible format.
#It was designed to be used in command line to write to a text file and to
#create a .png visualization.

#to use it, pass it any number of .conllu files in command line.

#it does this by reading the file line-by-line and looking for
#lines containing 'obj' determining if they point forward or backward.
#Because the annotation includes in column 6 the head verb, we can link
#object to verb.

#e.g.
#11	stelle	stellen	VERB	VVFIN	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	3	parataxis	_	_
#12	ich	ich	PRON	PPER	Case=Nom|Number=Sing|Person=1|PronType=Prs	11	nsubj	_	_
#13	mir	ich	PRON	PRF	Case=Dat|Number=Sing|Person=1|PronType=Prs|Reflex=Yes	11	iobj	_	_
#14	Kundenservice	Kundenservice	NOUN	NN	Case=Acc|Gender=Neut|Number=Sing	11	obj	_	_
#15	vor	vor	ADP	PTKVZ	_	11	compound:prt	_	SpaceAfter=No

import sys
import csv
import matplotlib.pyplot as plt
csv.field_size_limit(sys.maxsize) #needed to unlock the exta memory to be over 9000
tuples = [] #list-of-tuples to save processing time later
print('(Language,num_VO,num_OV)')

def count(conllu_name):
    with open(conllu_name, 'r') as csv_file: #for each .conllu file reads lines
        csv_reader = csv.reader(csv_file, delimiter = '\t') #tab-delineated
        #figure out language name by reading until you hit a dash
        i=0
        for char in conllu_file:
            if char == '-':
                break
            else:
                i=i+1
        language_name = conllu_file[3:i]
        #create some juicy indices
        VO_sen = 0
        OV_sen = 0
        #check the .conllu file, fool!
        for line in csv_reader:
            if len(line) < 7: #ignore small lines
                pass
            elif line[7] == 'obj': #if you have an object
                #check if line[0] is greater than line[6]
                if line[0] > line[6]:
                    #then we know this is a V-O sentence because [0] is this position and [6] is the head
                    VO_sen = VO_sen + 1
                else:
                    #assuming that it's OV if it isn't VO
                    OV_sen = OV_sen + 1
            else:
                pass
        return language_name, VO_sen, OV_sen

for conllu_file in sys.argv[1:]: #takes any number of .conllu arguments
    tuples.append(count(conllu_file))

for item in tuples:
    print(item)

#now to plot. I want this baby to be able to automatically create labels and values
labels = {}
x = [] # percent OV
y = [] # percent VO
i=0 #index to work through list of tuples
while i < len (tuples):
    pct_OV = tuples[i][2]/(tuples[i][1]+tuples[i][2])
    pct_VO = tuples[i][1]/(tuples[i][1]+tuples[i][2])
    labels[i]=tuples[i][0] #take the first element of the tuple at index i in the list
    x.append(pct_OV) #add the number of VO sentences (see language_data.txt)
    y.append(pct_VO) #add pct_VO
    i=i+1

plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for j in labels:  # Add labels to each of the points
    plt.text(x[j]-0.03, y[j]-0.03, labels[j], fontsize=5.5)
plt.savefig('languages')
#plt.show()
