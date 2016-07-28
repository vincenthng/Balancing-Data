from basic_method.add_data import *
from basic_method.delete_data import *
from generating.linear_recom import *
from generating.discrete_recom import *
from generating.single_point import *
from generating.variation import *
from data_choosing.data_choosing import *



'''bug的比例'''
rate = 0.2

'''将list转为array'''
def convert(selected):
    i=0
    for i in range(0,len(selected)):
        k=0
        for k in range(0,len(selected[i]-1)):
            selected[i][k]=selected[k+1]
    return array(selected)


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

'''
生成并储存,参数依次为
filename文件名,
abc选取比例,
listCsv总的数据集,
pos正例数据集,
neg负例数据集,
method取012分别为3种算子,
var为1则变异,
var_rate为变异的幅度比例
'''
def generating_new_data(filename,a,b,c,listCsv,pos,neg,method,var,var_rate):
    read_file(filename)
    while (float((len(pos))/float(len(listCsv))))<rate:
        temp=choose(a,b,c,listCsv,pos,neg)
        c=convert(temp)
        if(method==0):
            result=linear_recom(c[0], c[1])
        elif(method==1):
            result=single_point(c[0],c[1])
        else:
            result=discrete_recom(c[0],c[1])
        if var==1:
            variation(result,var_rate)
        list(result)
        for i in range(0,len(result)):
            k=len(result)-i
            result[k+1]=result[k]
        result[0]=temp[0][0]
        if int(result[len(len(result))])>0:
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