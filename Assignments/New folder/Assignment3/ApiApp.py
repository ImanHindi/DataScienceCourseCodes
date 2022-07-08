
from logging import exception
from time import sleep
import traceback
from flask import Flask, Request, request

import json

import firebase_admin

from firebase_admin import credentials

from firebase_admin import db

# logging in using private key









app=Flask(__name__)


#Fetch All DB Data
@app.route('/ResidenceDetails/Get',methods=['GET'])         
def GET_DATA():

    ref="/"
    root = db.reference(ref)
    try:
        data=root.get()
        
        return data
    except:
        return  "error!"

#get list of villas for a specified Owner      
@app.route('/ResidenceDetails/GetOwnerVillas',methods=['GET'])           
def GetOwnerVillas():
    ref = str(request.args.get("ref")+"/"+str(request.args.get("id")+"/listofvillas"))
    root = db.reference(ref)
    try:
        data=root.get()
        print(data)  
        return data
    except:
        return "error"

#delete from DB
@app.route("/ResidenceDetails/Delete",methods=['GET','DELET'])
def DELET_DATA():
    ref = str(request.args.get("ref"))
    root = db.reference(ref)
    try:
        root.delete()     
        return "Deleted Successfully"
    except:
        return "Error!" 

#Update Data
@app.route("/ResidenceDetails/UpdateTable",methods=['POST','GET','UPDATE'])
def UPDATE():
    ref = str(request.args.get("ref"))
    root = db.reference(ref)
    x =  request.args.get("x")
    x=json.loads(x)
    try:
        root.update(x)
        return "Updated successfully"
    except:
         
        return "error!"


#create tables
@app.route('/ResidenceDetails/CreateTable',methods=['POST','GET'])
def POST_DATA():
    ref =str(request.args.get("ref"))
    x=request.args.get("x")
    x=json.loads(x)
    root = db.reference(ref)
    try:
        root.set(x)
        return "added successfully"
    except:
        return "error"
     

#Insert new item to DB
@app.route('/ResidenceDetails/InsertToTable',methods=['POST','GET'])
def ADD_DATA():
    ref =str(request.args.get("ref"))
    x=request.args.get("x")
    x=json.loads(x)  
    root = db.reference(ref)
    try:
        root.set(x)
        return "added successfully"
    except:
        return "error"
     

#Connections Initializer: i searched for the best way to connect to database the best practice is to call the connection method each time 
#you need to access the data but i used the second way because it's faster and i can avoide multi connections easily because the code is simple and 
#perform a a specific sequence but it's not a good practice.
#reference : https://softwareengineering.stackexchange.com/questions/142065/creating-database-connections-do-it-once-or-for-each-query
try:
    cred = credentials.Certificate('C:\\Users\\user\\Desktop\\iman\\Assignments\\Assignment3\\newproject-65527-firebase-adminsdk-mnt08-7af112b82e.json')

    firebase_admin.initialize_app(cred, {'databaseURL' : 'https://newproject-65527-default-rtdb.firebaseio.com/' , 'httpTimeout' : 30})
    print('logged in to firebase')

except:

    print("please check your connection to the internet and try again!")


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except:
        print("error")
        print(traceback.TracebackException)



