import random
from pre_solving.pre_solving import *
from numpy import *
def variation(sample,rate):
    num=random.randint(0,len(sample))
    count=0
    while count<num:
        bit=random.randint(0,len(sample))
        np=random.randint(0,1)
        sample[bit]=sample[bit]*(1+(pow(-1,np)*rate))
        count=count+1
    return sample