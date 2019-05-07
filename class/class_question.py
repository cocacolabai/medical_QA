import jieba
from gensim.models import Word2Vec
from sklearn import svm
from sklearn.externals import joblib
import numpy as np
import json
jieba.load_userdict("../data/all_entity.txt")
model = Word2Vec.load("/home/liuchenxu/Downloads/word2vec/word2vec_wx")
medical_model = Word2Vec.load("../train_vec/medical.model")
entity = set([i.strip() for i in open("../data/all_entity.txt").readlines()])
svm_class_meachine=joblib.load("svm.m")
stop_words = set([i.strip("\n") for i in open("stop_words.txt").readlines()])
f = open("result_vector.json",'r')
f_symptom = open("../train_vec/symptom_sense/exist_symptom.txt")
symptom_words = list()
for line in f_symptom:
    line = line.strip()
    word = line.split(" ")
    symptom_words+=word

data = json.load(f)
for each_key in data.keys():
    for i in range(0,len(data[each_key])):
        for j in range(0, len(data[each_key][i])):
            data[each_key][i][j] = float(data[each_key][i][j])

train_list= list()
for each_key in data.keys():
    temp = np.array(data[each_key][0])
    for i in range(1, len(data[each_key])):
        temp+=np.array(data[each_key][i])
    temp = temp/len(data[each_key])
    train_list.append(temp)


def cut_words(sentence):
    return " ".join(jieba.cut(sentence))

def svm_class(average_vector):
    global svm_class
    average_vector = np.array([average_vector])
    return svm_class_meachine.predict(average_vector)

def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def vector_class(average_vector):
    global train_list
    max_index = 0
    max_sim = 0
    for i in range(0, len(train_list)):
        sim = cos_sim(average_vector, train_list[i])
        if sim>max_sim:
            max_index = i
            max_sim = sim
    return max_index


while True:
    sen = input("question:")
    region_words = cut_words(sen).split(" ")
    new_words = list()
    get_entity = list()
    words = list()
    for each in region_words:
        if each in entity:
            get_entity.append(each)
        else:
            words.append(each)
    for each in words:
        if each in model:
            new_words.append(each)
        else:
            if len(each)==2:
                new_words.append(each[0])
                new_words.append(each[1])
            elif len(each)==3:
                if each[0:2] in model:
                    new_words.append(each[0:2])
                    new_words.append(each[2])
                elif each[1:3] in model:
                    new_words.append(each[0])
                    new_words.append(each[1:3])
                else:
                    new_words.append(each[0])
                    new_words.append(each[1])
                    new_words.append(each[2])
            elif len(each)==4:
                new_words.append(each[0:2])
                new_words.append(each[2:4])

    get_symptom = set()

    for each in new_words:
        if each in medical_model and each not in stop_words:
            for symptom in symptom_words:
                if medical_model.similarity(each, symptom)>=0.6:
                    get_symptom.add(each)
                    print(each)
                    print(symptom)
    new_words = list(set(new_words)-set(get_symptom))
    print(new_words)        
    x = np.zeros(256)
    for i in range(0,len(new_words)):
        x = x + model[new_words[i]]
    if len(new_words)!=0:
        x = x/len(new_words)
    svm_result = svm_class(x)
    vector_result = vector_class(x)
    print(svm_result)
    print(vector_result)

