#coding=utf-8

def read_txt(txtfile):
    result=[]
    f = open(txtfile)
    line = f.readline()
    while line:
        if line.find("result") == 0:
            if line.split('/')[1]=="poi":
                temp3=line.split('/')[2]
            else:
                temp3=line.split('/')[1]
            temp4=line.split('->')
        if line.find("        pos")==0:
            temp=line.split("       ")
            temp1=temp[2].split("      ")
            temp1.insert(0,temp3)
            temp1.insert(1,temp4[0])
            temp1.insert(2,temp4[1].split("\n")[0])
            result.append(temp1)
        line = f.readline()
    f.close()
    return result


def save_csv(save,a):
    out=open(save,"w")
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            for k in range(0,len(a[i][j])):
                out.write(a[i][j][k])
                if k!=len(a[i][j])-1:
                    out.write(",")
                else:
                    out.write("\n")
    out.close()



a=read_txt("result/poi/0/result.txt")
b=read_txt("result/poi/1/result.txt")
c=read_txt("result/poi/2/result.txt")
d=read_txt("result/poi/3/result.txt")
e=read_txt("result/add/poi/result.txt")
f=read_txt("result/delete/poi/result.txt")
g=read_txt("result/MORPH/poi/result.txt")
h=read_txt("result/origin/poi/result.txt")
all=[]
all.append(a)
all.append(b)
all.append(c)
all.append(d)
all.append(e)
all.append(f)
all.append(g)
all.append(h)

save_csv("poi_result.csv",all)