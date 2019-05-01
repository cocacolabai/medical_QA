import json

f_disease = open('disease.txt','r')
f_alias = open('name.json','r')
f_out = open('disease_alias.json','w')
f_new_disease = open('new_disease.txt','w')

alias = json.load(f_alias)
alias_set = set(alias.keys())
all_list = []
for each in f_disease.readlines():
    each = each.strip('\n')
    temp_dict = {}
    if each in alias_set:

        for i in alias[each]:
            temp_dict[i] = each
        temp_dict[each] = each
    else:
        temp_dict[each] = each
    all_list.append(temp_dict)

json.dump(all_list,f_out, ensure_ascii=False)

for each_dict in all_list:
    for each_key in each_dict.keys():
        f_new_disease.write(each_key+"\n")


        
        
