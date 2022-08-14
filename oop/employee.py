from datetime import date, datetime
from xmlrpc.client import DateTime


class Date:
    import datetime
    def __init__(self) :
        self.year=(str(datetime.now()).split('-'))[0]
        self.month=(str(datetime.now()).split('-'))[1]

    def timeEpoch(self):
        return self.year,self.month




class warehouse:
 
    #_anualrevenue = 9000
    #num_employees = 0
    def get(self) :
        return self.__anualrevenue

    def set(self,newanualrevenue):
        __anualrevenue=newanualrevenue

    def __init__(self, Storagetype , Capacity, Manager, AnnualRent):
        #these are called attributes to a class
        self.Storagetype = Storagetype
        self.Capacity = Capacity
        self.Manager = Manager
        self.AnnualRent = AnnualRent
        self.expiryDate=Date()
        self.__anualrevenue=9000
    def ManagerName(self):
       managername= self.ManagerName
       return managername

    def change_anual_rent(self,newanualrent):
        self.AnnualRent=newanualrent
        print('instance_method')
        return self.AnnualRent

    def __Changeanualrevenue(self,new_anualrevenue):
        self.__anualrevenue=new_anualrevenue
        print(('class method'))
        return self.__anualrevenue

    x=__Changeanualrevenue(30000)

#inheritance 

class product(warehouse,Date):
 
    def __init__(self, Storagetype , Capacity, Manager, AnnualRent, product,producttype):
        warehouse.__init__(Storagetype , Capacity, Manager, AnnualRent)
        Date.__init__()
        self.product = product
        self.producttype=producttype
    def addproduct(self):
        print(self.product,self.producttype,self.expiryDate.month,self.expiryDate.year)

    def ManagerName(self):
        return print('this is a managername method')


products=product('food','large','Rami',15000,'chicken','frozen')
adding=products.addproduct()
print(products.ManagerName())



newwarehouse=warehouse('food','large','Rami',15000,'chicken','frozen')
print(newwarehouse.get())
warehouse.set(20000)
