import json


with open('/home/praveen/Desktop/Untitled Folder/task4and5/task4s.json','r') as d:
    details=json.load(d)
d={}
for i in range(50):
    for daract in details[i]['director']:
        if daract not in d:
            d[daract]=1
        else:
            d[daract]+=1
with open('task7s.json','w') as f:
    json.dump(d,f,indent=4)
