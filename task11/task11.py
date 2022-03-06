import json


with open('/home/praveen/Desktop/web scraping tasks/task4and5/task4s.json','r') as f:
    details=json.load(f)
    dic={}
    for i in details:
        if i["genre"] not in dic:
            dic[i["genre"]]=1
        else:
            dic[i["genre"]]+=1
with open('task10s.json','w') as t:
    json.dump(dic,t,indent=4)