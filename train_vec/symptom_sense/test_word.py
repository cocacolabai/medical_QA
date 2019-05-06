from gensim.models import Word2Vec

model = Word2Vec.load("../medical.model")
f = open("symptom_split.txt")
count = 0
all = 0
for line in f.readlines():
    line = line.strip("\n")
    words = line.split(" ")
    for each in words:
        all+=1
        try:
            temp = model[each]
        except KeyError:
            print(each)
            count+=1
print(model.similar_by_word("痉挛"))
print(all)
print(count)
f.close()
