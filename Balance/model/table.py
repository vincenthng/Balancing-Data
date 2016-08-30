
def read_txt(txtfile):
    result=[]
    f = open(txtfile)
    line = f.readline()
    while line:
        if line.find("avg / total")==0:
            temp=line.split("       ")
            temp1=temp[1].split("      ")
            result.append(temp1)
        line = f.readline()
    f.close()
    return result


def save_csv(save,a):
    out=open(save,"w")
    for i in range(0,len(a[0])):
        for j in range(0,len(a)):
            for k in range (0,len(a[j][i])):
                out.write(a[j][i][k])
                if(j!=len(a)-1 or k!=len(a[j][i])-1):
                    out.write(",")
        out.write("\n")
    out.close()



a=read_txt("result/time/0/result.txt")
b=read_txt("result/time/1/result.txt")
c=read_txt("result/time/2/result.txt")
d=read_txt("result/time/3/result.txt")
e=read_txt("result/add/time/result.txt")
f=read_txt("result/delete/time/result.txt")
g=read_txt("result/MORPH/time/result.txt")
all=[]
all.append(a)
all.append(b)
all.append(c)
all.append(d)
all.append(e)
all.append(f)
all.append(g)

save_csv("time_result.csv",all)
