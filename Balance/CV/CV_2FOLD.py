
# coding=utf-8
from basic_method.add_data import *
from basic_method.delete_data import *
from basic_method.MORPH import *
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


'''a表示选择2个负例的比例,b为两个正例的比例,c为一正一负的比例'''
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
    a.insert(0,name)
    a[len(a)-1]=str(a[len(a)-1])+"\r\n"
    return a


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
def generating_new_data(filename,a,b,c,method,var,var_rate,times):
    read_file(filename)
    atf=two_fold(listCsv)

    output = "result/" + filename.split('/')[0] + '/' + str(method) + '/' + filename.split('/')[1]
    output=output.split(".csv")[0]+"_"+str(times)+"_0_1.csv"
    out = open(output, "w")
    for l in atf[0]:
        for k in range(0, len(l)):
            if k != len(l) - 1:
                out.write(str(l[k]))
                out.write(',')
            else:
                out.write(str(l[k]))
                # out.write('\n')
    out.close()


    output = "result/" + filename.split('/')[0] + '/' + str(method) + '/' + filename.split('/')[1]
    output=output.split(".csv")[0]+"_"+str(times)+"_1_1.csv"
    out = open(output, "w")
    for l in atf[1]:
        for k in range(0, len(l)):
            if k != len(l) - 1:
                out.write(str(l[k]))
                out.write(',')
            else:
                out.write(str(l[k]))
                # out.write('\n')
    out.close()

    ng0=distinguish(atf[0])
    ng1=distinguish(atf[1])

    while (float((len(ng0[0]))/float(len(atf[0]))))<rate:
        temp=choose(a,b,c,atf[0],ng0[0],ng0[1])
        c=convert(temp)
        do_nothing=1
        if(method==0):
            result=linear_recom(c[0], c[1])
            do_nothing = 0
        elif(method==1):
            result=single_point(c[0],c[1])
            do_nothing = 0
        elif(method==2):
            result=discrete_recom(c[0],c[1])
            do_nothing = 0
        elif(method==3):
            result=intermediate_rec(c[0],c[1])
            do_nothing = 0

        if do_nothing==0:
            if var==1:
                variation(result,var_rate)
            result=convert_(result,temp[0][0])
            if float(result[len(result)-1])>0:
                ng0[0].append(result)
                atf[0].append(result)
            else:
                ng0[1].append(result)
                atf[0].append(result)
        else:
            break


    while (float((len(ng0[0]))/float(len(atf[0]))))<rate:
        temp=choose(a,b,c,atf[1],ng1[0],ng1[1])
        c=convert(temp)
        do_nothing = 1
        if (method == 0):
            result = linear_recom(c[0], c[1])
            do_nothing = 0
        elif (method == 1):
            result = single_point(c[0], c[1])
            do_nothing = 0
        elif (method == 2):
            result = discrete_recom(c[0], c[1])
            do_nothing = 0
        elif (method == 3):
            result = intermediate_rec(c[0], c[1])
            do_nothing = 0

        if do_nothing==0:
            if var==1:
                variation(result,var_rate)
            result=convert_(result,temp[0][0])
            if float(result[len(result)-1])>0:
                ng1[0].append(result)
                atf[1].append(result)
            else:
                ng1[1].append(result)
                atf[1].append(result)

        else:
            break


    output = "result/" + filename.split('/')[0] + '/' + str(method) + '/' + filename.split('/')[1]
    output=output.split(".csv")[0]+"_"+str(times)+"_0_0.csv"
    out = open(output, "w")
    for l in atf[1]:
        for k in range(0, len(l)):
            if k != len(l) - 1:
                out.write(str(l[k]))
                out.write(',')
            else:
                out.write(str(l[k]))
                # out.write('\n')
    out.close()


    output = "result/" + filename.split('/')[0] + '/' + str(method) + '/' + filename.split('/')[1]
    output=output.split(".csv")[0]+"_"+str(times)+"_1_0.csv"
    out = open(output, "w")
    for l in atf[0]:
        for k in range(0, len(l)):
            if k != len(l) - 1:
                out.write(str(l[k]))
                out.write(',')
            else:
                out.write(str(l[k]))
                # out.write('\n')
    out.close()



import glob
for filename in glob.glob(r'promise/*.csv'):
    i=0
    while i<10:
        generating_new_data(filename, 5, 70, 25, 0, 0, 0.05,i)
        generating_new_data(filename, 5, 70, 25, 1, 0, 0.05,i)
        generating_new_data(filename, 5, 70, 25, 2, 0, 0.05,i)
        generating_new_data(filename, 5, 70, 25, 3, 0, 0.05,i)
        generating_new_data(filename, 5, 70, 25, 4, 0, 0.05,i)
        i=i+1
