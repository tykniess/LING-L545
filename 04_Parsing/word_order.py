#This script extracts information on subject-verb order from a train.conllu file
#and returns a tuple of ( language name , number of s-v sentences, number of
#v-s sentences )

#it does this by reading the file line-by-line and looking for
#lines containing 'obj' and lines containing 'VerbForm=Fin'.
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
csv.field_size_limit(sys.maxsize) #needed to unlock the exta memory to be over 9000
print('Language\tnum_VO\tnum_OV')

for conllu_file in sys.argv[1:]: #takes any number of .conllu arguments
    with open(conllu_file, 'r') as csv_file: #for each .conllu file reads lines
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
        print(language_name +'\t'+ str(VO_sen) +'\t'+ str(OV_sen))
