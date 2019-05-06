from gensim.models import Word2Vec

model = Word2Vec.load("../medical.model")

while True:
    word = input("input words:")
    try:
        print(model.similar_by_word(word))
    except KeyError:
        print("no")

