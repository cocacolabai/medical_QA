from question_analyse import *
from translator import *
from py2neo import Graph

class FindAnwser:
    def __init__(self):
        self.g = Graph(host="127.0.0.1", http_port=7474, user='neo4j', password='123456')
        self.analyse = QuestionAnalyse()

    def find(self, cyphers):
        anwsers = []
        for cypher in cyphers:
            question_type = cypher['type']
            cypher_list = cypher['cypher']
            anwser = []
            for each in cypher_list:
                each_anwser = self.g.run(each).data()
                anwser += each_anwser
            anwsers.append(anwser)
        return anwsers
    def anwser(self, question):
        type_result = self.analyse.get_type(question)
        translator_result = translator(type_result[0], type_result[1], type_result[2])
        result = self.find(translator_result)
        question_types = type_result[2]
        """for i in range(0,len(question_types)):
            anwser = result[i]
            question_type = question_types[i]
            if question_type=='alias':
                alias = [j['n.alias'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}:{}".format(entity, ";".join(temp))
            elif question_type=='medicare':
                medicare = anwser[0]['n.medicare']
                entity = anwser[0]['n.name']
                if medicare==True:
                    process_anwser = ""
                else:
                    process_anwser = ""
            elif question_type=='money':
                money = anwser[0]['n.money']
                entity = anwser[0]['n.name']

"""
        return result


#if __name__ == '__main__':
#    analyse = QuestionAnalyse()
#    result = analyse.get_type('治疗糖尿病需要花多少钱')
#    finder = FindAnwser()
#    print(finder.find(translator(result[0], result[1], result[2])))

