



import firebase_admin

from firebase_admin import credentials

from firebase_admin import db



# logging in using private key

cred = credentials.Certificate('C:\\Users\\user\\Downloads\\newproject-65527-firebase-adminsdk-mnt08-7af112b82e.json')

firebase_admin.initialize_app(cred, {'databaseURL' : 'https://newproject-65527-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})

print('logged in to firebase')



# writing on the database
#way1:
#ref = "Employee"
#root = db.reference(ref)
#x =  {"position":"1200"}
#root.update(x)
#way2:
ref = "Employee/stm"
root = db.reference(ref)
x="23"
root.set(x)
#root.push(x)
#Reading from database
data=root.get()
print(data)
