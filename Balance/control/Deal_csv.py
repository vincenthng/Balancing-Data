# coding=utf-8
from numpy import *
import numpy
n = 0
inputs = []
file = 'C:/Users/Chris/Desktop/1.lang2.2_all.csv'
num = '_1'
file_1 = 'C:/Users/Chris/Desktop/1.lang2.2_all%s.csv' % num
#print file_1

'''
f = open('C:/Users/Chris/Desktop/1.lang2.2_all.csv','a+')
for line in f:
    inputs.append(line.split(","))
for line in f:
    inputs.append(line.split(","))
for i in range(1, len(inputs)):  # 将bug位转换为2分类
    if inputs[i][30] != '0\n':
        inputs[i][30] = '1\n'
for j in range(1, len(inputs)):  # 将模块名去掉
    inputs[j].remove(inputs[j][0])
print inputs[4]
'''


while n < 4:
    print n
    inputs = []
    file_name = 'C:/Users/Chris/Desktop/R/nodeal_data/result/lang/1.lang2.2_all-%d.csv' % n
    f = open(file_name, 'a+')
    for line in f:
        inputs.append(line.split(","))
    f.close()
    for i in range(1, len(inputs)):   #将bug位转换为2分类
        if inputs[i][len(inputs[i])-1] != '0\n':
          inputs[i][len(inputs[i])-1] = '1\n'
    j = 0
    for j in range(0, len(inputs)):   #将模块名去掉
        inputs[j].remove(inputs[j][0])



    file_save = "C:/Users/Chris/Desktop/R/deal_data/lang-%d.csv" % n
    f =open(file_save,'w')
    for i in range(len(inputs)):
       # new_str = str(inputs[i])
        new_str = ','.join(inputs[i])
        new_str = new_str[0:len(new_str)-1]
        new_str = new_str + '\n'
       # print new_str

        f.write(new_str)
    f.close()
    n = n + 1
