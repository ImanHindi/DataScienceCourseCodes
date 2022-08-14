class student :
    raise_amount=4000
    def __init__(self,Name,gpa):
        self.gpa=gpa
        self.Name=Name
        
    def get_info(self):
      #  raise_amount=100
      #  def chv():
      #      raise_amount=1000
      #      return raise_amount
      #  raise_amount=chv()
      #  print(raise_amount)
        return self.Name,self.gpa
            
    @classmethod
    def change_raise_amount(cls,amount):
        cls.raise_amount=amount

students=student(['iman','rami','salem','sama','sanaa','heba'],[50,70,80,90,96,98])
#student2=student(['iman','rami','salem','sama','sanaa','heba'],[50,70,80,90,96,98])

#gpa=list(students.gpa)
#print(gpa)
#for i in range(6):
#    if gpa[i]<=90:
#        students.raise_amount=4000
#        print(students.Name[i],students.gpa[i],students.raise_amount)
#        #print(students.raise_amount)
#
#    if gpa[i]>90:
#        students.raise_amount=3000
#        print(students.Name[i],students.gpa[i],students.raise_amount)

s=student.change_raise_amount(100)
print(s)

#print(students.__dict__)
#student.raise_amount=100
#print(student.raise_amount)
#print(students.__dict__)
#print(students.raise_amount)
#print(students.Name,students.gpa,students.raise_amount)

#print(student2.__dict__)
#print(student2.raise_amount)
#print(student2.Name,student2.gpa,student2.raise_amount)

#students.get_info()