class student :
    raise_amount=4000
    def __init__(self,Name,gpa):
        self.gpa=gpa
        self.Name=Name

    
    def get_info(self):
        return self.Name,self.gpa
    
    def student_payments(self):
        print(self.Name,self.gpa)

students=[]
students.append(student('iman',50))
students.append(student('rami',70))
students.append(student('salem',80))
students.append(student('sama',90))
students.append(student('sanaa',96))
students.append(student('heba',98))


print(students[0])
#students[0]=student('iman',50)
#students[1]=student('rami',70)
#students[2]=student('salem',80)
#students[3]=student('sama',90)
#students[4]=student('sanaa',96)
#students[5]=student('heba',98)

for s in students:
    if students[s].gpa<90:
        students[s].raise_amount=4000
        print(students[s].raise_amount)

    if students[s].gpa>90:
        students[s].raise_amount=3000
        print(students[s].raise_amount)


#print(students.get_info())
#print(students.get_info())
#
#print(students.Name)
#print(students.Name)



#students[0].raise_amount=2000
#print(students[0].raise_amount)
#
#student.raise_amount=3000
#print(students[0].raise_amount)
