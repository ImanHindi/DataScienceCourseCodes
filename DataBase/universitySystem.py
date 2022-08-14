import sqlite3
import traceback
import pandas as pd

class connection:
    def __init__(self) :
        self.conn=self.connect_to_database()
        self.cur=self.conn.cursor()
        #self.cursor.execute("PRAGMA journal_mode=WAL")
        #self.conn.commit()

    def connect_to_database(self):
        conn=sqlite3.connect('UniversitySystem.db')
        return conn

    def creat_employees_Table(self):
        query='''CREATE TABLE IF NOT EXISTS EmployeeInfo (
        EmployeeID int NOT NULL PRIMARY KEY,
        FirstName varchar(255),
        LasName varchar(255),
        Degree varchar(255),
        Salary int,
        classes varchar(255),
        date_of_employment varchar(255),
        major varchar(255)
        ); '''
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            traceback.print_exc()
            return "error"

    def creat_Students_Table(self):

        query='''CREATE TABLE IF NOT EXISTS StudentInfo (
        StudentID int NOT NULL PRIMARY KEY,
        FirstName varchar(255),
        LasName varchar(255),
        Degree varchar(255),
        gpa int
        ); '''
        self.cur.execute(query)
        self.conn.commit()

    def insert_employee_to_table(self,EmployeeID, FirstName,LastName, Degree, Salary,classes,date_of_employment,major):
        try:
            #query = f'INSERT INTO {tablename}'
            query=f'INSERT INTO  EmployeeInfo (EmployeeID, FirstName, LasName, Degree, Salary, classes, date_of_employment, major) VALUES ({EmployeeID},"{FirstName}","{LastName}","{Degree}", {Salary},"{classes}","{date_of_employment}","{major}");'
            self.cur.execute(query)
            self.conn.commit()
            print("inserted successfully")
            return "inserted successfully"
        except:
            traceback.print_exc()
            return "error!"
        

    def get_all_employee_from_table(self):
        try:
            query="SELECT * FROM EmployeeInfo"
            data=self.cur.execute(query).fetchall()
            self.conn.commit()
            return data
        except:
            return "error!"
    def close_connection(self):
        self.conn.close()

class Major:
    def __init__(self,major):
        self.__major_name=major

        #return self.__Major_name
    



class Employees:
    def __init__(self,employeeid,first_name,last_name,salary,degree,classes,date_of_employment,major):

        self.__firstname=first_name
        self.__lastname=last_name
        self.__salary=salary
        self.__classes=classes
        self.__date_of_employment=date_of_employment
        self.__degree=degree
        self.__major=Major(major)
        self.__employeeid=employeeid
    @classmethod
    def get_all_employees_data(self):
        
        newconnection=connection()
        data =newconnection.get_all_employee_from_table()
        return data
    def set_employee_data(self):
        newconnection=connection()
        newconnection.creat_employees_Table()
        data=newconnection.insert_employee_to_table(self.__employeeid,self.__firstname,self.__lastname,self.__degree,self.__salary,self.__classes,self.__date_of_employment,self.__major)
        newconnection.close_connection()
        return data

    def calculate_new_Salary(self):#,degree,major,salary):
        if self.major=='Dean of the College':
            salary_rate=.07

        if self.major=='Head of department':
            salary_rate=.06
        if self.__major=='professor':
            salary_rate=.05
        if self.major=='Doctor':
            salary_rate=.03
        else:
            salary_rate=.02
        new_salary=self.salary+salary_rate*self.__salary


        return new_salary


class Instructor(Employees):
    def __init__(self,first_name,last_name,extra_workig_hours,salary,classes,date_of_employment,degree):
        super.__init__(first_name,last_name,salary,classes,date_of_employment,degree,0)
        self.__extra_working_hours=extra_workig_hours



    def calculate_new_Salary(self):#__workig_hours,salary,degree,major):
        new_salary=self.__salary+(self.__extra_working_hours*5)
        return new_salary
    

class Student:
    def __init__(self,first_name,last_name,gpa,major,classes_marks):
        self.__firstname=first_name
        self.__lastname=last_name
        self.__gpa=gpa
        self.__major=Major(major)
        self.__classes_marks=classes_marks



    def calculate_gpa(self):
        new_gpa=(self.__gpa+sum(self.__classes_marks)/len(self.__classes_marks))/2
        return new_gpa
    

class subject:

    def __init__(self,name,price_per_hour,major):
        self.__name=name
        self.__price_per_hour=price_per_hour
        self.__major=Major(major)




employee1=Employees(1,'Iman','Imad',1500,'Master','Datascience','10/10/2012','MechatronicsEngineering')
employee2=Employees(2,'Rami','Salameh',1000,'Master','Datascience','10/10/2012','MechatronicsEngineering')
employee3=Employees(3,'Ghaith','Rami',2500,'PHD','Datascience','10/10/2012','MechatronicsEngineering')
employee4=Employees(4,'joudi','omar',750,'Bachelor','Datascience','10/10/2012','MechatronicsEngineering')
employee5=Employees(5,'mohnad','salem',1100,'Master','Datascience','10/10/2012','MechatronicsEngineering')
employee6=Employees(6,'salam','mohmmd',3000,'PHD','Datascience','10/10/2012','MechatronicsEngineering')

data=employee1.set_employee_data()
data=employee2.set_employee_data()
data=employee3.set_employee_data()
data=employee4.set_employee_data()
data=employee5.set_employee_data()
data=employee6.set_employee_data()

data=Employees.get_all_employees_data()
df=pd.DataFrame(data)
print(df)

df.to_csv("EmployeesInfo.csv")
