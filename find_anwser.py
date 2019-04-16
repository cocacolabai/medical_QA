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
        final = ""
        question_types = type_result[2]
        for i in range(0,len(question_types)):
            anwser = result[i]
            question_type = question_types[i]
            if question_type=='alias':
                alias = anwser[0]['n.alias']
                entity = anwser[0]['n.name']
                process_anwser = "{}的别名有:{}".format(entity, ";".join(alias))
            elif question_type=='medicare':
                medicare = anwser[0]['n.medicare']
                entity = anwser[0]['n.name']
                if medicare==True:
                    process_anwser = "{}是医保疾病，可以报销".format(entity)
                else:
                    process_anwser = "{}不是医保疾病，不可以报销".format(entity)
            elif question_type=='money':
                money = anwser[0]['n.money']
                entity = anwser[0]['n.name']
                process_anwser = "治疗{}的花费:{}".format(entity, money)
            elif question_type=='easyget':
                easy = anwser[0]['n.money']
                entity = anwser[0]['n.name']
                process_anwser = "{}的易感人群有:{}".format(entity, easy)
            elif question_type=='desc':
                desc = anwser[0]['n.desc'].replace("\n","")
                entity = anwser[0]['n.name']
                process_anwser = "{}:{}".format(entity, desc)
            elif question_type=='cureprobablity':
                cureprobablity = anwser[0]['n.cureprobablity']
                entity = anwser[0]['n.name']
                process_anwser = "{}的治愈率为:{}".format(entity, cureprobablity)
            elif question_type=='prevent':
                prevent = anwser[0]['n.prevent'].replace("\n", "")
                entity = anwser[0]['n.name']
                process_anwser = "预防{}的方法为:{}".format(entity, prevent)
            elif question_type=='lasttime':
                lasttime = anwser[0]['n.lasttime']
                entity = anwser[0]['n.name']
                process_anwser = "{}的治愈时间大约为:{}".format(entity, lasttime)
            elif question_type=='cause':
                cause = anwser[0]['n.cause'].replace("\n","")
                entity = anwser[0]['n.name']
                process_anwser = "{}的患病原因为:{}".format(entity, cause)
            elif question_type=='disease_symptom':
                symptom = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}的症状有:{}".format(entity, ";".join(symptom))
            elif question_type=='disease_check':
                check = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}需要的检查有:{}".format(entity, ";".join(check))
            elif question_type=='disease_department':
                department = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}属于{}".format(entity, ";".join(department))
            elif question_type=='disease_drug':
                print(anwser)
                drug = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}可服用{}".format(entity, ";".join(drug))
            elif question_type=='disease_not_food':
                food = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}不宜吃{}".format(entity, ";".join(food))
            elif question_type=='disease_good_food':
                food = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}宜吃{}".format(entity, ";".join(food))
            elif question_type=='drug_disease':
                disease = [j['n.name'] for j in anwser]
                entity = anwser[0]['m.name']
                process_anwser = "{}可治疗的疾病有{}".format(entity, ";".join(disease))
            elif question_type=='food_disease':
                disease = [j['n.name'] for j in anwser]
                entity = anwser[0]['m.name']
                process_anwser = "{}对以下疾病有益:{}".format(entity, ";".join(disease))
            elif question_type=='disease_acompany':
                disease = [j['m.name'] for j in anwser]
                entity = anwser[0]['n.name']
                process_anwser = "{}的并发症有{}".format(entity, ";".join(disease))
            elif question_type=='symptom_disease':
                disease = [j['n.name'] for j in anwser]
                #entity = anwser[0]['n.name']
                process_anwser = "可能有以下疾病:{}".format(";".join(disease))
            final+=process_anwser

        return final


#if __name__ == '__main__':
#    analyse = QuestionAnalyse()
#    result = analyse.get_type('治疗糖尿病需要花多少钱')
#    finder = FindAnwser()
#    print(finder.find(translator(result[0], result[1], result[2])))

