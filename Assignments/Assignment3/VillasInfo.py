import json
from typing_extensions import Self
import collections

class VillasInfo:

    __villas_json=collections.ChainMap()
    __villa_json={}
    __firstitem=0

    def __init__(self,villa_id,Villa_no,villa_location,villa_class,villa_price,owner_id):

        self.__villa_id=villa_id
        self.__Villa_no=Villa_no
        self.__villa_location=villa_location
        self.__villa_class=villa_class
        self.__villa_price=villa_price
        self.__owner_id=owner_id
        self.__create_villa_json()
        #self.__add_villa_to_villas_jason()


    def get_villa_id(self) :
        return self.__villa_id
    def set_villa_id(self,newvilla_id):
        self.__villa_id=newvilla_id
        
    def get_Villa_no(self) :
        return self.__Villa_no
    def set_Villa_no(self,newVilla_no):
        self.__Villa_no=newVilla_no

    def get_villa_location(self) :
        return self.__villa_location
    def set_villa_location(self,newvilla_location):
        self.__villa_location=newvilla_location

    def get_villa_class(self) :
        return self.__villa_class
    def set_villa_class(self,newvilla_class):
        self.__villa_class=newvilla_class

    def get_villa_price(self) :
        return self.__villa_price
    def set_villa_price(self,newvilla_price):
        self.__villa_price=newvilla_price
    
    def get_owner_id(self) :
        return self.__owner_id
    def set_owner_id(self,newowner_id):
        self.__owner_id=newowner_id

    @classmethod        
    def get_villas_json(self) :
        return self.__villas_json

        
    def get_villa_json(self) :
        return self.__villa_json


    #this method to add the info. of new villa to the list of villas 
    def __create_villa_json(self):
        self.__villa_json=dict(villaid=self.__villa_id,
                        Villa_no=self.__Villa_no,
                        villa_location=self.__villa_location,
                        villa_class=self.__villa_class,
                        villa_price=self.__villa_price,
                        owner_id=self.__owner_id)
        
        #__villa_json=json.dumps(__villa_json) 

        self.__villa_json={self.get_villa_id():self.__villa_json}

        self.__add_villa_to_villas_jason(self.__villa_json)
        
        #return __villa_json



    @classmethod
    def __add_villa_to_villas_jason(cls,villajson):
        if cls.__firstitem==0:
            #print('1')
            cls.__firstitem+=1
            cls.__villas_json=collections.ChainMap(villajson)
        else:
            cls.__villas_json=collections.ChainMap.new_child(cls.__villas_json,villajson)
            #print('2')
        
        #return cls.__villas_json


#new_villa1=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa2=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa3=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa4=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa5=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa6=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa7=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa8=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa9=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa10=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa11=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa12=VillasInfo(5,'A86959433','Amman','A',700000,1)
#new_villa13=VillasInfo(5,'A86959433','Amman','A',700000,1)
#
#
#create villasInfo table(json)

#villas=json.dumps(str(VillasInfo.get_villas_json()).replace('ChainMap(','').replace(')',''))

#print(villas)