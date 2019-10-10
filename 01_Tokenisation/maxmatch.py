import sys #needed for standard input and sys.argv
import csv #needed to just grab surfce forms from dictionary

###########################
#Stage 1: making a list from tokenized input 
l1 = [] # list for input lines
for line in sys.stdin:
        l1.append(line)
l2 = [] # list for maxmatch output forms

###########################
input_file = "ja_dict.txt"
output_file = input_file + "-surface_forms.txt"

with open(input_file,'r') as to_read:
        with open(output_file, 'w') as temp_file:
                reader = csv.reader(to_read, delimiter = "\t")
                #writer = open(temp_file, 'w')
                desired_column = [2]

                for row in reader:
                        if len(row) != 10:
                                continue
                        else:
                                column = row[2] #for i in desired_column)
                                temp_file.write(column + '\n')


def Find(word):
        with open(output_file, 'r') as searchable:
                for line in searchable:
                        if word == line[:len(line)-1]:
                                return True
                        else:
                                continue

def MaxMatch(sentence):
        """Takes a sentence and attempts to find maxmatch in a dictionary."""        
        if sentence == '':
                return False
                print ('empty sentence')
        else:
                i=len(sentence)
                while i > 0:
                        firstword = sentence[:i]
                        remainder = sentence[i:]
                        if Find(firstword):
                                l2.append(firstword)
                                sentence = remainder
                                i = len(sentence)
                        else:
                                i=i-1
                
                                
for sent in l1:
        MaxMatch(sent)

print("Your MaxMatch tokenized output is:")
i = 1
for maxmatch_output in l2:
        print (str(i) + '\t' + maxmatch_output + '\n')
        i = i + 1
