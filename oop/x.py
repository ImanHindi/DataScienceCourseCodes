class student :
    raise_amount=4000
    def __init__(self,Name,gpa):
        self.gpa=gpa
        self.Name=Name

    @classmethod
    def change_raise_amount(cls,amount):
        cls.raise_amount=amount


students=student('iman',70)     
student.change_raise_amount(100)
print(students.raise_amount)


