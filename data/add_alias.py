import json

f = open('illness.json','r')
f_out = open('new_ill.json','w')
f_alias = open('/home/liuchenxu/kg/QASystemOnMedicalGraph/data/name.json')

alias = json.load(f_alias)
data = json.load(f)

count = 0
for i in range(0, len(data)):
    data[i]['alias']=[]
    if data[i]['name'] in alias:
        #print(data[i]['name'])
        #print(alias[data[i]['name']])
        data[i]['alias'] = alias[data[i]['name']]

json.dump(data, f_out)
print(count)
    
