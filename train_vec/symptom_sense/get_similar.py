from gensim.models import Word2Vec
import numpy as np
def norm(s1,s2,alpha):
    return alpha*s1+(1-alpha)*s2
def cos_sim(vector_a, vector_b):

    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

model = Word2Vec.load("../medical.model")
f = open("symptom_split.txt","r")
obj = input("object:")
desc = input("description:")
split_max_sim = 0
split_get_words = []
merge_max_sim = 0
merge_get_words = []
for line in f.readlines():
    line = line.strip("\n")
    words = line.split(" ")
    try:
        merge_vec = np.array(model[words[0]])
        for i in range(1,len(words)):
            merge_vec+=model[words[i]]
        merge_vec = merge_vec/len(words)
        user_vec = (model[obj]+model[desc])/2
        merge_sim = cos_sim(merge_vec, user_vec)
        if merge_sim>merge_max_sim:
            merge_max_sim = merge_sim
            merge_get_words = words
    except KeyError:
        continue

    if len(words)!=2:
        continue
    try:
        split_sim = norm(model.similarity(obj,words[0]), model.similarity(desc,words[1]), 0.6)
        if split_sim > split_max_sim:
            split_max_sim = split_sim
            split_get_words = words
    except KeyError:
        continue
   
print(merge_get_words)
print(split_get_words)


