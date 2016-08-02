# coding: utf-8

import csv
import random
from numpy import *

'''读取文件的方法按照不同的文件来写'''

listCsv = []
neg = []
pos = []


def read_file(filename):
    del listCsv[:]
    del pos[:]
    del neg[:]
    file = open(filename)
    line = file.readline()
    while line!='':
        listCsv.append(line.split(','))
        line = file.readline()
    '''print(listCsv)'''
    for a in range(1,len(listCsv)):
        if(int(listCsv[a][len(listCsv[a])-1])>0):
            pos.append(listCsv[a])
        else:
            neg.append(listCsv[a])


'''a,b为2个需要计算距离的向量'''
def cal_distance(a,b):
    dis=0
    v=[]
    for i in range (1,len(a)-1):
        temp=abs(float(a[i])-float(b[i]))
        dis=dis+pow(temp,2)
    dis=pow(dis,0.5)
    return dis

'''a为当前样本,b为想要找到找到距离最短的数据集'''
def get_min_dis(a,b):
    min_v=[]
    min_distance=cal_distance(a,b[0])
    min_v = b[0]
    for i in range (0,len(b)):
        now_distance=cal_distance(a,b[i])
        if(now_distance<min_distance):
            min_distance=now_distance
            min_v=b[i]
    return min_v


'''TEST'''
'''
read_file('1.lang2.2_all.csv')
print(cal_distance(pos[1],neg[1]))
print(get_min_dis(pos[1],listCsv))
print(type(get_min_dis(pos[1],neg)))
'''