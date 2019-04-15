from question_analyse import *

def translator(entities, entities_type, question_types):

    cyphers = []
    entities_dict = {}
    for i in range(0,len(entities_type)):
        if entities_type[i] not in entities_dict:
            entities_dict[entities_type[i]] = []
        
        entities_dict[entities_type[i]].append(entities[i])


    print(entities_dict)
    for each_question_type in question_types:
        cypher= {}
        cypher['type'] = each_question_type
        cypher_list = []
        if each_question_type == 'alias':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.alias".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'medicare':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.medicare".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'money':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.money".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'easyget':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.easyget".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'desc':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.desc".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'cureprobablity':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.cureprobablity".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'prevent':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.prevent".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'lasttime':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.lasttime".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'cause':
            cypher_list = ["MATCH (n:Disease) where n.name = '{}' return n.name, n.cause".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_symptom':
            cypher_list = ["MATCH (n:Disease)-[r:has_symptom]->(m:Symptom) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_check':
            cypher_list = ["MATCH (n:Disease)-[r:need_check]->(m:Check) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_department':
            cypher_list = ["MATCH (n:Disease)-[r:belongs_to]->(m:Department) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_drug':
            cypher_list = ["MATCH (n:Disease)-[r:recommand_drug]->(m:Drug) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_not_food':
            cypher_list = ["MATCH (n:Disease)-[r:no_eat]->(m:Food) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'disease_good_food':
            cypher_list = ["MATCH (n:Disease)-[r:good_eat]->(m:Food) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
        elif each_question_type == 'drug_disease':
            cypher_list = ["MATCH (n:Disease)-[r:recommand_drug]->(m:Drug) where m.name = '{}' return n.name, m.name".format(i) for i in entities_dict['drug']]
        elif each_question_type == 'food_disease':
            cypher_list = ["MATCH (n:Disease)-[r:good_eat]->(m:Food) where m.name = '{}' return n.name, m.name".format(i) for i in entities_dict['food']]
        elif each_question_type == 'disease_acompany':
            cypher_list1 = ["MATCH (n:Disease)-[r:acompany_with]->(m:Disease) where n.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
            cypher_list2 = ["MATCH (n:Disease)-[r:acompany_with]->(m:Disease) where m.name = '{}' return n.name, m.name".format(i) for i in entities_dict['disease']]
            cypher_list = cypher_list1+cypher_list2
            print(cypher_list)
        elif each_question_type == 'symptom_disease':
            cypher_ = "MATCH (n:Disease)-[r0:has_symptom]->(m0:Symptom){} where m0.name = '"+entities_dict['symptom'][0]+"' {} return n.name"
            part1=""
            part2=""
            for i in range(1,len(entities_dict['symptom'])):
                part1+=", (n:Disease)-[r{}:has_symptom]->(m{}:Symptom)".format(i,i)
                part2+="and m{}.name='{}' ".format(i,entities_dict['symptom'][i])
            cypher_ = cypher_.format(part1, part2)
            cypher_list = [cypher_]
        cypher['cypher'] = cypher_list
        cyphers.append(cypher)
    
    return cyphers

if __name__ == '__main__':
    analyse = QuestionAnalyse()
    result = analyse.get_type('治疗糖尿病需要花多少钱')
    print(translator(result[0], result[1], result[2]))

