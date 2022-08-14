import json
from firebase_admin import credentials

import firebase_admin

x='{"key1": "Iman", "key2":30, "key3":"Amman"}'

y=json.loads(x)


print(y["key1"])

print(y)
x={"key1": "'key2':Iman", "key2":30, "key3":"Amman"}

y=x["key1['key2']"]
print(y)

y = json.dumps(x)

