import os
from pyltp import Postagger, Segmentor

LTP_DATA_DIR='/home/liuchenxu/pyltp/model'

pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径

postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型
segmentor = Segmentor()
segmentor.load(cws_model_path)

f = open('symptoms.txt','r')
f_out = open('symptom_split.txt','w')
for each in f.readlines():
    each = each.strip('\n')
    words = list(segmentor.segment(each))
    postags = list(postagger.postag(words))
    f_out.write(" ".join(words+postags))
    f_out.write("\n")

#words=segmentor.segment('我骨质疏松怎么办?')
#words = list(words)
#postags = postagger.postag(words)
#print(list(postags))
postagger.release()  # 释放模型
segmentor.release()
