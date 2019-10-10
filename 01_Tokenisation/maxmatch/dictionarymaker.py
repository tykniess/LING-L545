#test
l = [] #a list of strings
with open('ja_gsd-ud-train.conllu', 'r') as file:
    for line in file:
        l.append(str(line))

with open('dict' ,'w') as gile:
    for line in l:
        gile.write(line)

print ('Your dictionary is ' + str(len(l)) + ' lines long. \nCreated in this directory with the name dict')
