#coding=utf-8

def read_txt(txtfile):
    result=[]
    f = open(txtfile)
    line = f.readline()
    while line:
        if line.find("result/promise/") == 0:
            temp3=line.split('/')[2]
            temp4=line.split('/')[3].split('_')[0]
        if line.find("        pos")==0:
            temp=line.split("       ")
            temp1=temp[2].split("      ")
            temp1.insert(0,temp3)
            temp1.insert(1,temp4)
            result.append(temp1)
        line = f.readline()
    f.close()
    return result


def save_csv(save,a):
    out=open(save,"w")
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            for k in range(0,len(a[i][j])):
                out.write(a[i][j][k])
                if k!=len(a[i][j])-1:
                    out.write(",")
                else:
                    out.write("\n")
    out.close()



a=read_txt("result/promise/0/result.txt")
b=read_txt("result/promise/1/result.txt")
c=read_txt("result/promise/2/result.txt")
d=read_txt("result/promise/3/result.txt")
#e=read_txt("result/promise/add/result.txt")
#f=read_txt("result/promise/delete/result.txt")
#g=read_txt("result/MORPH/promise/result.txt")
h=read_txt("result/promise/4/result.txt")
all=[]
all.append(a)
all.append(b)
all.append(c)
all.append(d)
#all.append(e)
#all.append(f)
#all.append(g)
all.append(h)

save_csv("promise_result.csv",all)