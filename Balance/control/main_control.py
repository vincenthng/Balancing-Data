# coding=utf-8
from basic_method.add_data import *
from basic_method.delete_data import *
from generating.linear_recom import *
from generating.discrete_recom import *
from generating.single_point import *
from generating.variation import *
from data_choosing.data_choosing import *
from generating.intermediate_rec import *


'''bug的比例'''
rate = 0.2

'''将list转为array'''
def convert(selected):
    selected_=[]
    for i in selected:
        k=0
        array_temp = []
        while k<len(i)-1:
            array_temp.append(double(i[k+1]))
            k=k+1
        selected_.append(array_temp)
    return array(selected_)


'''a表示选择2个正例的比例,b为两个负例的比例,c为一正一负的比例'''
def choose(a,b,c,listCsv,pos,neg):
    r=random.randint(0,100)
    result=[]
    if(r<a):
        result=choosing_neg_neg(neg)
    elif(r in range(a,a+b)):
        result=choosing_pos_pos(pos)
    else:
        result=choosing_pos_neg(listCsv,pos,neg)
    return result

def convert_(a,name):
    a = list(a)
    for i in range(1, len(a)):
        k = len(a) - i
        a[k] = a[k - 1]
    a[0] = name
    return a


'''
生成并储存,参数依次为
filename文件名,
abc选取比例,
listCsv总的数据集,
pos正例数据集,
neg负例数据集,
method取0123分别为4种算子,
var为1则变异,
var_rate为变异的幅度比例
'''
def generating_new_data(filename,a,b,c,method,var,var_rate):
    read_file(filename)
    while (float((len(pos))/float(len(listCsv))))<rate:
        temp=choose(a,b,c,listCsv,pos,neg)
        print temp
        c=convert(temp)
        print c
        print type(c[0][2])
        if(method==0):
            result=linear_recom(c[0], c[1])
        elif(method==1):
            result=single_point(c[0],c[1])
        elif(method==2):
            result=discrete_recom(c[0],c[1])
        elif(method==3):
            result=intermediate_rec(c[0],c[1])
        if var==1:
            variation(result,var_rate)
        result=list(result)
        result=convert_(result,temp[0][0])
        print result
        a=[]
        a.append(result)
        a=convert(a)
        print "a",a[0]
        b=convert(pos)
        print "b",b[1]
        print linear_recom(a[0],b[1])
        if int(result[len(result)-1])>0:
            pos.append(result)
            listCsv.append(result)
        else:
            neg.append(result)
            listCsv.append(result)
    output=filename.split(".csv")[0]+'-'+string(method)+".csv"
    out=open(output,"w")
    for l in listCsv:
       for k in range(0,len(l)):
            if k!=len(l)-1:
              out.write(l[k])
              out.write(',')
            else:
              out.write(l[k])
       '''out.write('\n')'''
    out.close()



generating_new_data("1.lang2.2_all.csv",5,25,70,0,0,0.05)