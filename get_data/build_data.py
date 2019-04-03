#!/usr/bin/env python3
# coding: utf-8
import json
import os
from max_cut import *

class MedicalGraph:
    def __init__(self):
        f_data = open("../data/new_all_data.json",'r')
        self.f_out = open("illness.json","w")
        self.all_data = json.load(f_data)
        f_data.close()
        self.all_illness = list()
        first_words = open('first_name.txt').readlines()[0].split(' ')
        alphabets = list("abcdefghijklmnopqrstuvwxyz0123456789")
        self.stop_words = set(first_words + alphabets)
        self.key_dict = {
            '医保疾病' : 'medicare',
            "患病比例" : "get_proportion",
            "易感人群" : "easy_get",
            "传染方式" : "get_way",
            "就诊科室" : "cure_department",
            "治疗方式" : "cure_way",
            "治疗周期" : "cure_time",
            "治愈率" : "cured_probability",
            '药品明细': 'drug_detail',
            '药品推荐': 'recommand_drug',
            '推荐': 'recommand_eat',
            '忌食': 'not_eat',
            '宜食': 'good_eat',
            '症状': 'symptom',
            '检查': 'check',
            '成因': 'cause',
            '预防措施': 'prevent',
            '所属类别': 'category',
            '简介': 'description',
            '名称': 'name',
            '常用药品' : 'common_drug',
            '治疗费用': "money",
            '并发症': 'acompany'
        }
        self.cuter = CutWords()

    def collect_medical(self):
        cates = []
        inspects = []
        count = 0
        for item in self.all_data:

            data = {}
            basic_info = item['basic_info']
            name = basic_info['name']
            if not name:
                continue
            # 基本信息
            data['名称'] = name
            data['简介'] = '\n'.join(basic_info['desc']).replace('\r\n\t', '').replace('\r\n\n\n','').replace(' ','').replace('\r\n','\n')
            category = basic_info['category']
            #data['所属类别'] = category
            cates += category
            inspect = item['inspect_info']
            inspects += inspect
            attributes = basic_info['attributes']
            # 成因及预防
            data['预防措施'] = item['prevent_info']
            data['成因'] = item['cause_info']
            # 并发症
            data['症状'] = list(set([i for i in item["symptom_info"][0] if i[0] not in self.stop_words]))
            for attr in attributes:
                attr_pair  = attr.split('：')
                if len(attr_pair) == 2:
                    key = attr_pair[0]
                    value = attr_pair[1]
                    data[key] = value
            # 检查
            inspects = item['inspect_info']

            data['检查'] = inspects
            # 食物
            food_info = item['food_info']
            if food_info:
                data['宜食'] = food_info['good']
                data['忌食'] = food_info['bad']
                data['推荐'] = food_info['recommand']
            # 药品
            drug_info = item['drug_info']
            data['药品推荐'] = list(set([i.split('(')[-1].replace(')','') for i in drug_info]))
            data['药品明细'] = drug_info
            data_modify = {}
            for attr, value in data.items():
                if attr[0]==' ':
                    attr = attr[1:]
                attr_en = self.key_dict.get(attr)
                print(attr_en)
                if attr_en:
                    data_modify[attr_en] = value
                if attr_en in ['medicare', 'get_proportion', 'easy_get', 'get_way', "cure_time", "cured_probability"]:
                    data_modify[attr_en] = value.replace(' ','').replace('\t','')
                elif attr_en in ['cure_department', 'cure_way', 'common_drug']:
                    data_modify[attr_en] = [i for i in value.split(' ') if i]
                
                elif attr_en in ['acompany']:
                    acompany = [i for i in self.cuter.max_biward_cut(data_modify[attr_en]) if len(i) > 1]
                    data_modify[attr_en] = acompany

            try:
                #self.db['medical'].insert(data_modify)
                count += 1
                print(count)
                #print(data_modify)
                self.all_illness.append(data_modify)
            except Exception as e:
                print(e)
            
        json.dump(self.all_illness, self.f_out)
        self.f_out.close()


        return



if __name__ == '__main__':
    handler = MedicalGraph()
    handler.collect_medical()
    
