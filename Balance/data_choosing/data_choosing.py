from pre_solving.pre_solving import *
import random

read_file('1.lang2.2_all.csv')

def choosing_neg_neg():
    choosing_2_element=[]
    rand = random.randint(0, len(neg) - 1)
    temp=neg[rand]
    choosing_2_element.append(temp)
    neg.remove(temp)
    choosing_2_element.append(get_min_dis(temp,neg))
    neg.append(temp)
    return choosing_2_element

def choosing_pos_pos():
    choosing_2_element=[]
    rand = random.randint(0, len(pos) - 1)
    temp=pos[rand]
    choosing_2_element.append(temp)
    pos.remove(temp)
    choosing_2_element.append(get_min_dis(temp,pos))
    pos.append(temp)
    return choosing_2_element

def choosing_pos_neg():
    choosing_2_element=[]
    rand =random.randint(0,len(listCsv)-1)
    choosing_2_element.append(listCsv[rand])
    if int(listCsv[rand][len(listCsv[rand])-1])>0:
        choosing_2_element.append(get_min_dis(listCsv[rand],neg))
    else:
        choosing_2_element.append(get_min_dis(listCsv[rand],pos))
    return choosing_2_element



print(choosing_pos_pos())
print(choosing_neg_neg())
print(choosing_pos_neg())