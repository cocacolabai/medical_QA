import json
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split as ts
from sklearn.externals import joblib
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


label_list = list()
train_list = list()
for each_key in data.keys():
    for i in range(0, len(data[each_key])):
        train_list.append(data[each_key][i])
        label_list.append(int(each_key))

label = np.array(label_list)
train = np.array(train_list)

test_label_list = list()
test_train_list = list()
for each_key in test_data.keys():
    for i in range(0, len(test_data[each_key])):
        test_train_list.append(test_data[each_key][i])
        test_label_list.append(int(each_key))

test_label = np.array(test_label_list)
test_train = np.array(test_train_list)

#X_train,X_test,y_train,y_test = ts(train,label,test_size=0.2)
clf_rbf = svm.SVC(kernel='linear')
clf_rbf.fit(train, label)
score_rbf = clf_rbf.score(test_train, test_label)
print(score_rbf)

joblib.dump(clf_rbf, "svm.m")
