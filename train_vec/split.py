
import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs, sys
def cut_words(sentence):
    #print sentence
    return " ".join(jieba.cut(sentence))
 
 
f = codecs.open('test_class_question.txt', 'r', encoding="utf8")
target = codecs.open("test_class_question_seg.txt", 'w', encoding="utf8")
print('open files')
line_num = 1
line = f.readline()
while line:
    print('---- processing ', line_num, ' article----------------')
    label = line.split(" ")[0]
    sentence = line.split(" ")[-1]
    result = cut_words(sentence)
    target.write(label+" "+result)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()

