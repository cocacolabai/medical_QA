
check = [i.strip() for i in open('data/check.txt','r').readlines()]
department = [i.strip() for i in open('data/department.txt','r').readlines()]
disease = [i.strip() for i in open('data/disease.txt','r').readlines()]
drug = [i.strip() for i in open('data/drug.txt','r').readlines()]
food = [i.strip() for i in open('data/food.txt','r').readlines()]
symptoms = [i.strip() for i in open('data/symptoms.txt','r').readlines()]

#print(len(check)+len(department)+len(disease)+len(drug)+len(food)+len(symptoms))
#print(len(list(set(check+department+disease+drug+food+symptoms))))
#print(len(symptoms)+len(check))
#print(len(list(set(symptoms+check))))
print(set(symptoms)&set(check))
