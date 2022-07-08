import collections
import json
from typing import ChainMap

from VillasInfo import VillasInfo


class OwnersDetails:
    __owners_json=collections.ChainMap()
    #__owners_json={}
    __owner_json={}
    __firstitem=0
    def __init__(self,owner_id,first_name,last_name,phone,address,no_of_villas,villas={}):
        self.__owner_id=owner_id
        self.__first_name=first_name
        self.__last_name=last_name
        self.__phone=phone
        self.__address=address
        self.__no_of_villas=no_of_villas
        self.__villas=villas

        self.__create_owner_details_json()
        #print(self.__owner_json)
        
        #self.__add_owner_to_owners_jason(self.__owner_json)
        #print(self.get_owners_json())
        #print(self.get_owner_json())
        #print(self.__owner_json)


    def get_owner_id(self) :
        return self.__owner_id
    def set_owner_id(self,newowner_id):
        self.__owner_id=newowner_id

    def get_first_name(self) :
        return self.__first_name
    def set_first_name(self,newfirst_name):
        self.__first_name=newfirst_name

    def get_last_name(self) :
        return self.__last_name
    def set_last_name(self,newlast_name):
        self.__last_name=newlast_name
        
    def get_phone(self) :
        return self.__phone
    def set_phone(self,newphone):
        self.__phone=newphone
        
    def get_address(self) :
        return self.__address
    def set_address(self,newaddress):
        self.__address=newaddress
        
    def get_no_of_villas(self) :
        return self.__no_of_villas
    def set_no_of_villas(self,newno_of_villas):
        self.__no_of_villas=newno_of_villas


    @classmethod
    def get_owners_json(self) :
        return self.__owners_json

        
    def get_owner_json(self) :
        return self.__owner_json

    
    
    def __create_owner_details_json(self):
        self.__owner_json=dict(owner_id=self.__owner_id,
                        first_name=self.__first_name,
                        last_name=self.__last_name,
                        phone=self.__phone,
                        address=self.__address,
                        no_of_villas=self.__no_of_villas,
                        listofvillas=self.__villas)
        owner_json={self.get_owner_id():self.__owner_json}
      
        self.__add_owner_to_owners_jason(owner_json)
        #self.__owner_json=json.dumps(self.__owner_json) 
        #print(self.__owner_json)
       # return self.__owner_json
    @classmethod
    def __add_owner_to_owners_jason(cls,ownerjson):
        if cls.__firstitem==0:
            cls.__firstitem+=1
            cls.__owners_json=collections.ChainMap(ownerjson)
        else:
            cls.__owners_json=collections.ChainMap.new_child(cls.__owners_json,ownerjson)
         





#new_owner_1=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#new_owner_2=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#new_owner_3=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#new_owner_4=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#new_owner_5=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#new_owner_6=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#owners=json.dumps(str(OwnersDetails.get_owners_json()).replace('ChainMap(','').replace(')',''))


#print(owners)
##owner=new_owner_1.get_owner_json()
#print(owner)
#insert a new owner to the OwnerDetails table
#new_owner_8=OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',5)
#owner=new_owner_1.get_owner_json()
#owner_id=new_owner_1.get_owner_id()
