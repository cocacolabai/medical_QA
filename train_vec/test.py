from gensim.models import Word2Vec

medical_model = Word2Vec.load("./medical.model")

testwords = ['头疼','乏力','失眠','眼神','异常','复方']
for i in testwords:
    res = medical_model.most_similar(i)
    print(res)
