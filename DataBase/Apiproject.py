import requests
import json
from flask import Flask,request,render_template
#default host 127.0.0.1 and port =5000
#app=Flask(__name__)
#@app.route("/employeedetails/<name>",)
#def hello(name):
#    return "Hello %s!" %name
#
#@app.route("/")
#
#
#def index():
#    return render_template("index.html")

#app=Flask(__name__)
#app.route('/employeedetails', methods=['POST'])
#
#def index():
#    return json.dumps({'name':'iman','email':'eng.eman.hindi@gmail.com'})
#
#app.run()



    
app=Flask(__name__)
@app.route("/employeedetails", methods=['POST','GET'])
def func1():
    no1= int(request.args.get("n1"))
    no2=int(request.args.get("no2"))
    return str(no1*no2)

if __name__=="__main__":
    app.run()
#@app.route("/")


#def index():
#    return render_template("index.html")
#
#
#
#
#if __name__=="__main__":
#    app.run(debug=True)

#res=requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'}, headers={'Accept': 'application/vnd.github.v3.text-match+json'},)
#
#print(res.status_code)
#
##print(res.text)
#
#print(res.json().keys())
#
#print(res.json()['items'][0])

#res=requests.post('http://127.0.0.1:5000/employeedetails?', {'n1':'70','no2':'2'})
#res=requests.get('http://127.0.0.1:5000/employeedetails',{'n1':'70','no2':'2'})

#print(res)