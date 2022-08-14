from datetime import date, datetime
from typing_extensions import Self
from xmlrpc.client import DateTime

class Date:
    import datetime
    def __init__(self) :
        self.year=(str(datetime.now()).split('-'))[0]
        self.month=(str(datetime.now()).split('-'))[1]

    def timeEpoch(self):
        return self.year,self.month








class vehicles:

    def __init__(self,vehicletype,vehiclesize):
            self.__vehicletype=vehicletype
            self.__vehiclesize=vehiclesize

    
    def get_vehicletype(self) :
        return self.__vehicletype

    def set_vehicletype(self,newvehicletype):
        __vehicletype=newvehicletype

    def get_vehiclesize(self) :
        return self.__vehiclesize

    def set_vehiclesize(self,newvehiclesize):
        __vehiclesize=newvehiclesize

    


class cars(vehicles):
    __carslist=[]
    __category={}
    
    def __init__(self,carname,countryofogigin,vehicletype,vehiclesize):
            super().__init__(vehicletype,vehiclesize)
            self.__carname=carname
            self.__countryofogigin=countryofogigin
            self.__productionyear=Date().year
            self.__addcartocars()
    def get_carname(self) :
        return self.__carname

    def set_carname(self,newcarname):
        __carname=newcarname

    def get_countryofogigin(self) :
        return self.__countryofogigin

    def set_countryofogigin(self,newcountryofogigin):
        __countryofogigin=newcountryofogigin

    def __addcartocars(self):
        
        self.__carslist.append(self.__carname)
        repitition=0
        for i,car in enumerate(self.__carslist):
            if self.__carslist[i]==self.__carname:
                repitition+=1
        print(repitition)
        if repitition>=1:
            self.__category[self.__carname]=repitition 
        print(self.__carslist) 
        print(self.__category)
        #return self.__carslist

    


    def categorization(self):
      #  for i,car in enumerate(self.__carslist):
         # if  self.__carname==car:
            #self.__category[self.__carname]+=1
        return self.__category[self.__carname]

class main:

    newcar=cars('BMW','Germany','electric','small')
    newcar=cars('BMW','Germany','electric','small')
    newcar=cars('BMW','Germany','electric','small')
    newcar=cars('BMW','Germany','electric','small')
    newcar2=cars('Marcedes','Germany','electric','small')
    newcar2=cars('Marcedes','Germany','electric','small')
    newcar2=cars('Marcedes','Germany','electric','small')

    print(newcar.categorization())
    print(newcar2.categorization())
