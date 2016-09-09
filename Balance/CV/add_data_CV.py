#coding=utf-8
from pre_solving.pre_solving import *
import random

def two_fold(list1):
    list2=[]
    list1.pop(0)
    while len(list2)<len(list1):
        r = random.randint(0, len(list1)-1)
        list2.append(list1[r])
        list1.pop(r)
    result=[]
    result.append(list1)
    result.append(list2)
    return result

def distinguish(list1):
    p=[]
    n=[]
    for i in range(0,len(list1)):
        if(double(list1[i][len(list1[i])-1])>0):
            p.append(list1[i])
        else:
            n.append(list1[i])
    result=[]
    result.append(p)
    result.append(n)
    return result

#save="result/"
def add_data_cv(rate,load,save,times):
    file = open(load)
    line = file.readline()

    listCsv = []

    while line!='':
       listCsv.append(line.split(','))
       line = file.readline()

    atf=two_fold(listCsv)

    np0=distinguish(atf[0])
    np1=distinguish(atf[1])

    #load="promise/……"
    output=save+load.split('/')[0]+"/add/"+load.split('/')[1]
    a=output.split(".csv")
    output=output.split(".csv")[0]+"_"+str(times)+"_0_1.csv"
    out=open(output,"w")
    for l in atf[0]:
       for k in range(0,len(l)):
            if k!=len(l)-1:
              out.write(l[k])
              out.write(',')
            else:
              out.write(l[k])
       '''out.write('\n')'''
    out.close()

    output = save + load.split('/')[0] + "/add/" + load.split('/')[1]
    output = output.split(".csv")[0] + "_" + str(times) + "_1_1.csv"
    out=open(output,"w")
    for l in atf[1]:
       for k in range(0,len(l)):
            if k!=len(l)-1:
              out.write(l[k])
              out.write(',')
            else:
              out.write(l[k])
       '''out.write('\n')'''
    out.close()

    while (float((len(np1[0]))/float(len(atf[1]))))<rate:
      rand=random.randint(0, len(np1[0])-1)
      atf[1].append(np1[0][rand])
      np1[0].append(np1[0][rand])



    while (float((len(np0[0]))/float(len(atf[0]))))<rate:
      rand=random.randint(0, len(np0[0])-1)
      atf[0].append(np0[0][rand])
      np0[0].append(np0[0][rand])


    #print (len(neg))
    #print (float((len(pos))/float(len(listCsv))))

    output=save+load.split('/')[0]+"/add/"+load.split('/')[1]
    output=output.split(".csv")[0]+"_"+str(times)+"_0_0.csv"
    out=open(output,"w")
    for l in atf[1]:
       for k in range(0,len(l)):
            if k!=len(l)-1:
              out.write(l[k])
              out.write(',')
            else:
              out.write(l[k])
       '''out.write('\n')'''
    out.close()

    output = save + load.split('/')[0] + "/add/" + load.split('/')[1]
    output = output.split(".csv")[0] + "_" + str(times) + "_1_0.csv"
    out=open(output,"w")
    for l in atf[0]:
       for k in range(0,len(l)):
            if k!=len(l)-1:
              out.write(l[k])
              out.write(',')
            else:
              out.write(l[k])
       '''out.write('\n')'''
    out.close()



import glob
for filename in glob.glob(r'promise/*.csv'):
    i = 0
    while i<10:
        add_data_cv(0.2,filename,"result/",i)
        i=i+1







