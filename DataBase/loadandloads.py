import json
 
file_object = open("json.txt", "r") 
# Load JSON file data to a python dict object. 
dict_object = json.load(file_object) 
print(dict_object) 



[ {"name": "Fred", "age": 32}, {"name": "Bob", "age": 21 } ] 

[{u'age': 32, u'name': u'Fred'}, {u'age': 21, u'name': u'Bob'}] 
 
# Now using strings 
with open("json.txt") as f: 
    txt = f.read() 
    data=json.loads(txt) 

