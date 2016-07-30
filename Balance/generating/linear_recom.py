import random
from numpy import *
def linear_recom(vector1,vector2):
    r = random.uniform(0.3,0.7)
    new_bug = []
    array(new_bug)
    new_bug = r * vector1 +(1.0-r)*vector2
    import judge
    new_bug = judge.judge_lable(vector1,vector2,new_bug)
    return (new_bug)
    
'''测试部分'''
from basic_method import MORPH
vec1 = MORPH.all_inputs_vector[2]
print "type(vec1):\n",type(vec1)
vec2 = MORPH.bug_inputs_vector[2]
print "type(vec2):\n",type(vec2)
vec3 = linear_recom(vec1,vec2)
print vec3
print "type(vec3):\n",type(vec3)
