

def question_contain_key(keys, question):    
        for key in keys:
            if key in question:
                return True
        return False

class QuestionAnalyse:
    
    def __init__(self):

        check = [i.strip() for i in open('data/check.txt','r').readlines()]
        department = [i.strip() for i in open('data/department.txt','r').readlines()]
        disease = [i.strip() for i in open('data/disease.txt','r').readlines()]
        drug = [i.strip() for i in open('data/drug.txt','r').readlines()]
        food = [i.strip() for i in open('data/food.txt','r').readlines()]
        symptom = [i.strip() for i in open('data/symptoms.txt','r').readlines()]
        self.deny_words = [i.strip() for i in open('data/deny.txt','r').readlines()]
        self.all_entity = list(set(check + department + disease + drug + food + symptom))
        self.entity_type={}
        for each in check:
            self.entity_type[each]='check'
        for each in department:
            self.entity_type[each]='department'
        for each in drug:
            self.entity_type[each]='drug'
        for each in food:
            self.entity_type[each]='food'
        for each in symptom:
            self.entity_type[each]='symptom'
        for each in disease:
            self.entity_type[each]='disease'

        


        self.symptom_key = ['症状', '表征', '现象', '症候', '表现']
        self.cause_key = ['原因','成因', '为什么', '怎么会', '怎样才', '咋样才', '怎样会', '如何会', '为啥', '为何', '如何才会', '怎么才会', '会导致', '会造成']
        self.acompany_key = ['并发症', '并发', '一起发生', '一并发生', '一起出现', '一并出现', '一同发生', '一同出现', '伴随发生', '伴随', '共现']
        self.food_key = ['饮食', '饮用', '吃', '食', '伙食', '膳食', '喝', '菜' ,'忌口', '补品', '保健品', '食谱', '菜谱', '食用', '食物','补品']
        self.drug_key= ['药', '药品', '用药', '胶囊', '口服液', '炎片']
        self.prevent_key = ['预防', '防范', '抵制', '抵御', '防止','躲避','逃避','避开','免得','逃开','避开','避掉','躲开','躲掉','绕开',
                             '怎样才能不', '怎么才能不', '咋样才能不','咋才能不', '如何才能不',
                             '怎样才不', '怎么才不', '咋样才不','咋才不', '如何才不',
                             '怎样才可以不', '怎么才可以不', '咋样才可以不', '咋才可以不', '如何可以不',
                             '怎样才可不', '怎么才可不', '咋样才可不', '咋才可不', '如何可不']
        self.lasttime_key = ['周期', '多久', '多长时间', '多少时间', '几天', '几年', '多少天', '多少小时', '几个小时', '多少年']
        self.cureway_key = ['怎么治疗', '如何医治', '怎么医治', '怎么治', '怎么医', '如何治', '医治方式', '疗法', '咋治', '怎么办', '咋办', '咋治']
        self.cureprobablity_key = ['多大概率能治好', '多大几率能治好', '治好希望大么', '几率', '几成', '比例', '可能性', '能治', '可治', '可以治', '可以医']
        self.easyget_key = ['易感人群', '容易感染', '易发人群', '什么人', '哪些人', '感染', '染上', '得上']
        self.check_key = ['检查', '检查项目', '查出', '检查', '测出', '试出']
        self.department_key = ['属于什么科', '属于', '什么科', '科室', '挂']
        self.cure_key = ['治疗什么', '治啥', '治疗啥', '医治啥', '治愈啥', '主治啥', '主治什么', '有什么用', '有何用', '用处', '用途',
                          '有什么好处', '有什么益处', '有何益处', '用来', '用来做啥', '用来作甚', '需要', '要']
        self.money_key = ['钱','花费','费用']
        self.medicare_key = ['医保','报销','医疗保险']
        self.alias_key = ['别名','学名','专业名称','其他','其它']
        self.desc_key = ['描述','介绍','简介']
        self.disease_key = ['什么病', '怎么回事', '什么情况']

    def get_type(self, question):
        entities = self.get_entity(question)
        entities_type = [self.entity_type[entity] for entity in entities]
        question_types = []
        
        if question_contain_key(self.alias_key, question) and 'disease' in entities_type:
            temp_type = 'alias'
            question_types.append(temp_type)
        if question_contain_key(self.medicare_key, question) and 'disease' in entities_type:
            temp_type = 'medicare'
            question_types.append(temp_type)
        if question_contain_key(self.money_key, question) and 'disease' in entities_type:
            temp_type = 'money'
            question_types.append(temp_type)
        if question_contain_key(self.easyget_key, question) and 'disease' in entities_type:
            temp_type = 'easyget'
            question_types.append(temp_type)
        if question_contain_key(self.desc_key, question) and 'disease' in entities_type:
            temp_type = 'desc'
            question_types.append(temp_type)
        if question_contain_key(self.cureprobablity_key, question) and 'disease' in entities_type:
            temp_type = 'cureprobablity'
            question_types.append(temp_type)
        if question_contain_key(self.prevent_key, question) and 'disease' in entities_type:
            temp_type = 'prevent'
            question_types.append(temp_type)
        if question_contain_key(self.lasttime_key, question) and 'disease' in entities_type:
            temp_type = 'lasttime'
            question_types.append(temp_type)
        if question_contain_key(self.cause_key, question) and 'disease' in entities_type:
            temp_type = 'cause'
            question_types.append(temp_type)
        if question_contain_key(self.symptom_key, question) and 'disease' in entities_type:
            temp_type = 'disease_symptom'
            question_types.append(temp_type)
        if question_contain_key(self.check_key, question) and 'disease' in entities_type:
            temp_type = 'disease_check'
            question_types.append(temp_type)
        if question_contain_key(self.department_key, question) and 'disease' in entities_type:
            temp_type = 'disease_department'
            question_types.append(temp_type)
        if question_contain_key(self.drug_key, question) and 'disease' in entities_type:
            temp_type = 'disease_drug'
            question_types.append(temp_type)
        if question_contain_key(self.food_key, question) and 'disease' in entities_type:
            is_deny = question_contain_key(self.deny_words, question)
            if is_deny:
                temp_type = 'disease_not_food'
            else:
                temp_type = 'disease_good_food'
            question_types.append(temp_type)
        if question_contain_key(self.disease_key, question) and 'symptom' in entities_type:
            temp_type = 'symptom_disease'
            question_types.append(temp_type)
        if question_contain_key(self.cure_key, question) and 'drug' in entities_type:
            temp_type = 'drug_disease'
            question_types.append(temp_type)
        if question_contain_key(self.food_key, question) and 'food' in entities_type:
            temp_type = 'food_disease'
            question_types.append(temp_type)
        if question_contain_key(self.acompany_key, question) and 'disease' in entities_type:
            temp_type = 'disease_acompany'
            question_types.append(temp_type)
        if question_types==[] and 'disease' in entities_type:
            temp_type = 'desc'
            question_types.append(temp_type)
        if question_types==[] and 'symptom' in entities_type:
            temp_type = 'symptom_disease'
            question_types.append(temp_type)

        return entities, entities_type, question_types


    def get_entity(self, question):
        entities = []
        for each in self.all_entity:
            if each in question:
                entities.append(each)
        remove_list = []
        for i in entities:
            for j in entities:
                if i in j and i !=j:
                    remove_list.append(i)
        result = [i for i in entities if i not in remove_list]

        return result
    
    
if __name__ == '__main__':
    analyse = QuestionAnalyse()
    result = analyse.get_type('治疗糖尿病需要花多少钱')
    print(result)

