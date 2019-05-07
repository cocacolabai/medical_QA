from gensim.models import Word2Vec
model = Word2Vec.load("../medical.model")
f = open("./symptom_split.txt","r")
f_out = open("exist_symptom.txt","w")

for line in f.readlines():
    line = line.strip()
    words = line.split(" ")
    is_exists = True
    for word in words:
        if word not in model:
            is_exists = False
    if is_exists:
        f_out.write(line+"\n")

f.close()
f_out.close()
