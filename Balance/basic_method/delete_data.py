import random
import csv

rate=0.2

file = open('1.lang2.2_all.csv')
line = file.readline()

listCsv = []
neg=[]
pos=[]

while line!='':
    listCsv.append(line.split(','))
    line = file.readline()
print(listCsv)

for a in range(1,len(listCsv)):
    if(int(listCsv[a][len(listCsv[a])-1])>0):
        pos.append(listCsv[a])
    else:
        neg.append(listCsv[a])

print(len(listCsv))
print (pos)
print (len(pos))
print(len(neg))

while (float((len(pos))/float(len(listCsv))))<rate:
    rand=random.randint(0, len(neg)-1)
    listCsv.remove(neg[rand])
    neg.pop(rand)

print (len(neg))
print (float((len(pos))/float(len(listCsv))))


out=open("test.csv","w")
for l in listCsv:
    for k in range(0,len(l)):
        if k!=len(l)-1:
            out.write(l[k])
            out.write(',')
        else:
            out.write(l[k])
    '''out.write('\n')'''
out.close()

