import json

d={}
with open('/home/praveen/Desktop/Untitled Folder/task4and5/task4s.json','r') as d1:
    details=json.load(d1)

directors = []
for movie in details:
    for dir in movie['director']:
        if dir not in directors:
            directors.append(dir)

for dira in directors:
    langu={}
    for new in details:
        if dira in new['director']:
            for lang in new['language']:
                if lang not in langu:
                    langu[lang]=1
                else:
                    langu[lang]+=1
    d[dira]=langu
with open('task10s.json','w') as tas:
    json.dump(d,tas,indent=4)


    # for i in details:
    #     for daract in i['director']:
    #         for lang in i['language']:
                
# print(directors)