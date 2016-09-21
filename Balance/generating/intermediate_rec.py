# coding=UTF-8
from numpy import  *
import random
import operator
import string
def intermediate_rec(vector1,vector2):
    d = 0.25
    random_num = random.uniform(d,1.0)
   # vector_interim = ((vector1 - vector2) * (vector1 - vector2)) ** 0.5
    vector_interim = abs((vector1 - vector2))
    random_choos_father = random.uniform(0.0, 1.0)
    if random_choos_father >= 0.5:
        new_bug = vector1 + random_num * vector_interim
    else:
        new_bug = vector2 + random_num * vector_interim
    from judge import judge_lable
    new_bug = judge_lable(vector1,vector2,new_bug)
    #print new_bug
    return new_bug
