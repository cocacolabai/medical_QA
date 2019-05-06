import json
import numpy as np
from sklearn import svm
def cos_sim(vector_a, vector_b):

    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

f = open("result_vector.json",'r')
f_test = open("test_result_vector.json",'r')

data = json.load(f)
test_data = json.load(f_test)
for each_key in data.keys():
    for i in range(0,len(data[each_key])):
        for j in range(0, len(data[each_key][i])):
            data[each_key][i][j] = float(data[each_key][i][j])

for each_key in test_data.keys():
    for i in range(0,len(test_data[each_key])):
        for j in range(0, len(test_data[each_key][i])):
            test_data[each_key][i][j] = float(test_data[each_key][i][j])



train_list= list()
for each_key in data.keys():
    temp = np.array(data[each_key][0])
    for i in range(1, len(data[each_key])):
        temp+=np.array(data[each_key][i])
    temp = temp/len(data[each_key])
    train_list.append(temp)

right=0
count=0
for each_key in test_data.keys():
    for i in range(0, len(test_data[each_key])):
        test_data[each_key][i] = np.array(test_data[each_key][i])
        max_sim = 0
        max_index = 0
        for j in range(0, len(train_list)):
            sim = cos_sim(test_data[each_key][i], train_list[j])
            if sim > max_sim:
                max_sim = sim
                max_index = j
        if str(max_index)==each_key:
            right+=1
        count+=1
print(count)
print(right)
print(right*1.0/count)


