import json

'''jsonData='{"name": "Frank", "age": 39, "available":true}'
jsonToPython=json.loads(jsonData)                   #_loads_-object to json
print(jsonToPython)
print(json.dumps(jsonToPython)) '''                 #_dumps_-json to objects

'''
student = '{"101":{"class":"V","Name":"Rohit","Roll_no":7},'\
           '"102":{"class":"V","Name":"Sachin","Roll_no":8},'\
           '"103":{"class":"V","Name":"Pushpendra","Roll_no":12}}'
print(json.loads(student))
print(json.dumps(student)) '''

a= '{"CenterCode":"100","Batch":[{"Name":"Sachin","Fee":2000},'\
    '{"Name":"Ravi","Fee":3000},'\
    '{"Name":"pushpendra","Fee":2000}]}'
aaa=json.loads(a)
print(aaa)
bb=json.dumps(aaa)
print(bb)





