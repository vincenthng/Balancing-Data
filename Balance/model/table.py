#coding=utf-8
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



a=read_txt("result/xerces/0/result.txt")
b=read_txt("result/xerces/1/result.txt")
c=read_txt("result/xerces/2/result.txt")
d=read_txt("result/xerces/3/result.txt")
e=read_txt("result/add/xerces/result.txt")
f=read_txt("result/delete/xerces/result.txt")
g=read_txt("result/MORPH/xerces/result.txt")
all=[]
all.append(a)
all.append(b)
all.append(c)
all.append(d)
all.append(e)
all.append(f)
all.append(g)

save_csv("xerces_result.csv",all)

'''
import matplotlib.pyplot as plt
import numpy as np
data_plot=[]

l=[x[2] for x in a]
data_plot.append(l)
l=[x[2] for x in b]
data_plot.append(l)
l=[x[2] for x in c]
data_plot.append(l)
l=[x[2] for x in d]
data_plot.append(l)
l=[x[2] for x in e]
data_plot.append(l)
l=[x[2] for x in f]
data_plot.append(l)
l=[x[2] for x in g]
data_plot.append(l)


print type(data_plot)





fig = plt.figure(1, figsize=(9, 6))
# Create an axes instance
ax = fig.add_subplot(111)

## add patch_artist=True option to ax.boxplot()
## to get fill color
bp = ax.boxplot(data_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='y', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']: # 上下的帽子
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']: #中值
    median.set(color='r', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']: #异常值
    flier.set(marker='o', color='k', alpha=0.5)

plt.show()
'''

