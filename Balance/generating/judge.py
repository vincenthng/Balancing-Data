# coding=UTF-8
#from basic_method import MORPH
'''在各种算法子中使用的lable生成函数，son的距离跟父母谁近那么lable就跟谁
    本来想着是直接添加的但是array不支持 + 重载，于是只好直接修改'''
def get_deances(inputs1,inputs2):
    arr1 = inputs1
    arr2 = inputs2
    arr_difference = arr1 - arr2
    arr_difference = arr_difference ** 2
    arr_difference = arr_difference.sum()
    arr_difference = arr_difference ** 0.5
    return arr_difference
def judge_lable(vector1,vector2,vector_son):
    if get_deances(vector1,vector_son) > get_deances(vector2,vector_son): #儿子跟vector2姓
        v2_len = len(vector2)
        vson_len = len(vector_son)
        vector_son[vson_len] = vector2[v2_len]
    else:
        v1_len = len(vector1)
        vson_len = len(vector_son)
        vector_son[vson_len] = vector1[v1_len]
    return vector_son

#print "judge:\n",judge_lable(MORPH.all_inputs_vector[2],MORPH.all_inputs_vector[3],MORPH.all_inputs_vector[4])
