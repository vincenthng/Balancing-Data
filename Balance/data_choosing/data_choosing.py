from pre_solving.pre_solving import *
import random


def choosing_neg_neg(neg):
    choosing_2_element=[]
    rand = random.randint(0, len(neg) - 1)
    temp=neg[rand]
    choosing_2_element.append(temp)
    neg.remove(temp)
    choosing_2_element.append(get_min_dis(temp,neg))
    neg.append(temp)
    return choosing_2_element

def choosing_pos_pos(pos):
    choosing_2_element=[]
    rand = random.randint(0, len(pos) - 1)
    temp=pos[rand]
    choosing_2_element.append(temp)
    pos.remove(temp)
    if(len(pos)>0):
        choosing_2_element.append(get_min_dis(temp,pos))
        pos.append(temp)
    else:
        choosing_2_element.append(temp)
        pos.append(temp)
    return choosing_2_element

def choosing_pos_neg(listCsv,pos,neg):
    choosing_2_element=[]
    rand =random.randint(1,len(listCsv)-1)
    choosing_2_element.append(listCsv[rand])
    if int(listCsv[rand][len(listCsv[rand])-1])>0:
        choosing_2_element.append(get_min_dis(listCsv[rand],neg))
    else:
        choosing_2_element.append(get_min_dis(listCsv[rand],pos))
    return choosing_2_element


'''test'''
'''
read_file("1.lang2.2_all.csv")
print choosing_neg_neg(neg)
print choosing_pos_pos(pos)
print choosing_pos_neg(listCsv,pos,neg)
'''