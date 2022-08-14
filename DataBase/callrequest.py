import requests

res=requests.get('http://127.0.0.1:5000/employeedetails',{'n1':'70','no2':'2'})

print(res)