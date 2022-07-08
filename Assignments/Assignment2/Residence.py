


#this module is user defined module that is imported to calculate the rebitition of the items in a list (for q2 of the assignment)
#in this code it is used to show the locations destripution of the apartments and villas
import Categorization

#this class initializes location of the place of residence , it has two methods to get and set the location value 
#and has one atribute used to hold the location value 
class Location:
    def __init__(self,location):
        self.__location=location

    def get_location(self) :
        return self.__location

    def set_location(self,newlocation):
        self.__location=newlocation




#this class is a parent class used to save the common atributes in both (villas and apartments)and also can be used as a class for the sites or grounds that don't include a building yet.
#attribute:
# 1.plant type: classification of the site (A or B or C)
# 2.sitearea: which returns the ground area 
# 3.the sitelocation: which used to save the location of residence

#  methods of the class: 
#1. get and set methods : to assign the value instance to the attributes
#2. ResidenceCategorization : that is used to classify the residence upon the class (A, B, C) of each to (high,medium,low) 
# this method will be used later to select the (price per meter) value of the site.
#2. Calculate_price : this method is used to calculate the price upon request depending on it's area and the price per meter of the selected site
class Residence:
    
    #initialize the residence class variables
    __residenceprice=0
    __residenceclass=''
    
    #this list for the prices of the gound per meter the selection of the price is depend on the type classifications of the ground(price per meter for A class is 100 price for example)
    __gorundpricepermeter=[100,50,20]
    def __init__(self,plantype,sitearea,sitelocation):

        self.__plantype=plantype
        self.__sitearea=sitearea
        self.__Sitelocation=Location(sitelocation).get_location()
        
    #get and set methods:
    def get_plantype(self) :
        return self.__plantype

    def set_plantype(self,newplantype):
        self.__plantype=newplantype

    def get_residenceprice(self) :
        return self.__residenceprice

    def set_residenceprice(self,newresidenceprice):
        self.__residenceprice=newresidenceprice

    def get_sitearea(self) :
        return self.__sitearea

    def set_sitearea(self,newsitearea):
        self.__sitearea=newsitearea


    def get_Sitelocation(self) :
        return self.__Sitelocation

    def set_Sitelocation(self,newSitelocation):
        self.__Sitelocation=newSitelocation

    #this method is used to classify the residence upon the class (A, B, C) of each to (high,medium,low) 
    # this method will be used later to select the (price per meter) value of the site.  
    def ResidenceCategorization(self):
        if self.__plantype=='A':
            self.__residenceclass='High'
            return self.__residenceclass,self.__gorundpricepermeter[0]
        elif self.__plantype=='B':
            self.__residenceclass='Medium'
            return self.__residenceclass,self.__gorundpricepermeter[1]
        elif self.__plantype=='C':
            self.__residenceclass='Low'
            return self.__residenceclass,self.__gorundpricepermeter[2]
        else:
            self.__residenceclass='Undefiend'
            return self.__residenceclass

    #this method is used to calculate the price upon request depending on it's area and the price per meter of the selected site
    def calculate_price(self):
        if self.__plantype=='A':
            self.__residenceprice=self.__sitearea*self.__gorundpricepermeter[0]
            
        elif self.__plantype=='B':
            self.__residenceprice=self.__sitearea*self.__gorundpricepermeter[1]
            
        elif self.__plantype=='C':
            self.__residenceprice=self.__sitearea*self.__gorundpricepermeter[2]
            
        else:
            self.__residenceprice=0
        
        return self.__residenceprice







#this is child class that is inheret from the parent class (Residence)
#used to deal only with data related to villas specifically
#attributes: villa size, no of floors, garden size , classification type of the plan(A ,B, or C) ,area of the site(garden size+building size), and the location of the villa
#method :
#1.get and set methods
#2. calculate_price method that is overriding of the parent class method
#3. add villa method that is used to add the information of villa to the list of villas saved before
#4. class method categorization filter that is used to filter the list of villas depending on user selection for the classification type of the villa (high, medium, low) that return the villa's info. related to the selected class
#5.class method villas_locations_distribution that is used to show the location distribution for villas 


class Villa(Residence):
    __residenceprice=0
    __villaclass=''
    __villainfo=[]
    __listofvillas=[]
    __villaspricepermeter=150

    def __init__(self,villasize,floors,gardensize,plantype,sitearea,villalocation):
        super().__init__(plantype,sitearea,villalocation)
        self.__villasize=villasize
        self.__floors=floors
        self.__gardensize=gardensize
        #self.calculate_price()
        self.__add_villa()

    def get_villasize(self) :
        return self.__villasize

    def set_villasize(self,newvillasize):
        self.__villasize=newvillasize

    def get_floors(self) :
        return self.__floors

    def set_floors(self,newfloors):
        self.__floors=newfloors

    def get_gardensize(self) :
        return self.__gardensize

    def set_gardensize(self,newgardensize):
        self.__gardensize=newgardensize

    
    def get_villainfo(self) :
        return self.__villainfo

    def set_villainfo(self,newvillainfo):
        self.__villainfo=newvillainfo
    
    #this method overrides the method in the parent class , used to calculate the price for villas specifically
    def calculate_price(self):

            __residenceprice = Residence.calculate_price(self)+self.__floors*self.__villasize*self.__villaspricepermeter
            return __residenceprice

        
    #this method to add the info. of new villa to the list of villas 
    def __add_villa(self):
        self.__villaclass=Residence.ResidenceCategorization(self)[0]
        self.__villainfo=[self.__villaclass,Residence.get_plantype(self),self.__villasize,Residence.get_Sitelocation(self),self.__residenceprice,self.__gardensize,self.__floors]
        self.__listofvillas.append(self.__villainfo)
    
    #class method that is used to return the villas that has the same class depending on the user class filter selection(high,low,medium)
    @classmethod
    def categorization_filter(cls,classfilter):
        filter=[]
        for villa in cls.__listofvillas:
            if classfilter==villa[0]:
                filter.append(villa)
            else:
                pass

        return filter
    
    #class method is used to show the disribution of villas in each location
    # this method uses the imported Categorization module that is built for the Q2 of the Assignment  
    @classmethod
    def villas_locations_distribution(cls):
            locations=[]
            for v in cls.__listofvillas:
                locations.append(v[3])
            
            locationsdistribution=Categorization.Categorization.categorize(locations)
            return locationsdistribution



#this is child class that is inheret from the parent class (Residence)
#used to deal only with data related to apartments specifically
#attributes: apartment size, no. of rooms, apartment number in the building,floor no., classification type of the plan(A ,B, or C) ,area of the site(garden size+building size), and the location of the villa
#method :
#1.get and set methods
#2. calculate_price method that is overriding of the parent class method
#3. add apartment method that is used to add the information of apartment to the list of apartments saved before
#4. class method categorization filter that is used to filter the list of apartments depending on user selection for the classification type of the apartment (high, medium, low) that return the apartments info. related to the selected class
#5.class method apartments_locations_distribution that is used to show the location distribution for apartments 

class apartment(Residence):
    __category=0
    __residenceprice=0
    __apartmentclass=''
    __apartmentinfo=[]
    __listofapartments=[]
    __apartmentspricepermeter=[30,50,65,75,100]

    def __init__(self,apartmentsize,rooms,apartmentno,floor,plantype,sitearea,apartmentlocation):
        super().__init__(plantype,sitearea,apartmentlocation)
        self.__apartmentsize=apartmentsize
        self.__apartmentsize

        self.__rooms=rooms
        self.__apartmentno=apartmentno
        self.__floor=floor
        #self.calculate_price()
        self.add_aparment()

    def get_apartmentsize(self) :
        return self.__apartmentsize

    def set_apartmentsize(self,newapartmentsize):
        self.__apartmentsize=newapartmentsize

    def get_rooms(self) :
        return self.__rooms

    def set_rooms(self,newrooms):
        self.__rooms=newrooms

    def get_apartmentno(self) :
        return self.__apartmentno

    def set_apartmentno(self,newapartmentno):
        self.__apartmentno=newapartmentno

    def get_floor(self) :
        return self.__floor

    def set_floor(self,newfloor):
        self.__floor=newfloor
        
    def get_apartmentinfo(self) :
        return self.__apartmentinfo

    def set_apartmentinfo(self,newapartmentinfo):
        self.__apartmentinfo=newapartmentinfo
    
    #this method is used to classify the apartments upon the class (A, B, C) of each to categories (0-5) 
    # this method will be used later to select the (price per meter) value of the apartment. 
    def apartmentcategorization(self):
        if self.__floor==1 or self.__floor==0 :
            if self.__rooms>=4:
                self.__category=5
            else:
                self.__category=4
        elif self.__floor>1 :
            if self.__rooms>=4:
                self.__category=3
            else:
                self.__category=2
        elif self.__floor>1 :
            if self.__rooms>=4:
                self.__category=1
            else:
                self.__category=0
        return self.__category
    
    #this method overrides the method in the parent class , used to calculate the price for apartments specifically
    def calculate_price(self):
        self.__residenceprice = Residence.calculate_price(self)+self.__apartmentsize*self.__apartmentspricepermeter[self.apartmentcategorization()]
        return self.__residenceprice
    
    #this method to add the info. of new apartment to the list of apartments 
    def add_aparment(self):
        self.__apartmentclass=Residence.ResidenceCategorization(self)[0]
        self.__apartmentinfo=[self.__apartmentclass,self.__apartmentno,Residence.get_Sitelocation(self),Residence.get_plantype(self),self.__residenceprice,self.__apartmentsize,self.__rooms]
        self.__listofapartments.append(self.__apartmentinfo)
        
    #class method that is used to return the apartment that has the same class depending on the user class filter selection(high,low,medium)
    @classmethod
    def categorization_filter(cls,classfilter):
        filter=[]
        #print(cls.__listofapartments)
        for apartment in cls.__listofapartments:
            if classfilter==apartment[0]:
                filter.append(apartment)
            else:
                pass
        #print(filter)
        return filter
    
    #class method used show the disribution of apartments in each location
    # this method used the imported Categorization module that is built for the Q2 of the Assignment 
    @classmethod
    def apartments_locations_distribution(cls):
            locations=[]
            for v in cls.__listofapartments:
                locations.append(v[2])
            
            locationsdistribution=Categorization.Categorization.categorize(locations)
            return locationsdistribution



newapartment1=apartment(150,5,10,3,'B',150,'Amman')
newapartment2=apartment(250,6,2,0,'B',250,'Madaba')
newapartment3=apartment(190,5,1,0,'C',190,'Jerrash')
newapartment4=apartment(110,2,3,1,'B',110,'Amman')
newapartment5=apartment(300,6,5,2,'A',300,'Irbid')
newapartment6=apartment(110,3,3,1,'C',110,'Zarqa')

newresidence1=Residence('A',1500,'Aqapa')
newresidence2=Residence('B',1500,'Amman')
newresidence3=Residence('C',1000,'Deadsea')
newresidence4=Residence('A',2500,'Jerash')
newresidence5=Residence('B',900,'Amman')

newvilla1=Villa(450,2,400,'A',850,'Jerash')
newvilla2=Villa(700,3,400,'A',1100,'Ajloun')
newvilla3=Villa(500,1,300,'B',800,'Amman')
newvilla4=Villa(600,2,400,'C',1000,'Amman')

print('apartment2 information')
print(newapartment2.get_apartmentinfo())


print('newapartment 1 no.')
print(newapartment1.get_apartmentno())

print('newvilla 1 gardensize')
print(newvilla1.get_gardensize())


print('villa filter is High')
newfilter=Villa.categorization_filter('High')
print(newfilter)

print('apartments filter is medium')
newfilter=apartment.categorization_filter('Medium')
print(newfilter)

print('siteprice')
print(newresidence1.calculate_price())

print('Villa price')
print(newvilla1.calculate_price())

print('apartment Price')
print(newapartment1.calculate_price())

print('apartment1 info')
print(newapartment1.get_apartmentinfo())

print('find the distripution of the apartments on each location')
print(apartment.apartments_locations_distribution())

print('find the distripution of the villas on each location')
print(Villa.villas_locations_distribution())