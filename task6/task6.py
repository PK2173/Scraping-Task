from itertools import count
import json


with open('/home/praveen/Desktop/Untitled Folder/task4and5/task4s.json','r') as d:
    data=json.load(d)
# counter=0
# a=[]
# for i in data:
#     if counter<50:
#         a.extend(i['language'])
#         counter+=1
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# t={}
# for i in b:
#     c=a.count(i)
#     t[i]=c
dic = {}

for i in range(50):
    for lang in data[i]['language']:
        if lang not in dic:
            dic[lang] = 1
        else:
            dic[lang]+=1

with open('task6s.json','w') as d:
    json.dump(dic,d,indent=4)

# print(dic)