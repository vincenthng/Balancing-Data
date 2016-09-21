# coding=UTF-8
from numpy import  *
import random
import operator
import string
def discrete_recom(vector1,vector2):
    leng = len(vector1)
    new_bug = []
    for i in range(0,leng):
        random_num = random.randint(1,1000)
        if random_num > 650:   #正例
            new_bug.append(vector1[i])

        else :
            new_bug.append(vector2[i])
            #print random_num


    #print  type(new_bug)
    #print vector1,'\n'
    #print vector2,'\n'
    #print  new_bug
    from judge import judge_lable
    new_bug = judge_lable(vector1,vector2,new_bug)
    return new_bug
   
