import requests
import OwnersDetails
import VillasInfo
import json




class DbRequests:
    def get_data(self):
        try:
            res=requests.get('http://127.0.0.1:5000/ResidenceDetails/Get')
            return res
        except:
            return "error!"

    def creat_table(self,table_name,values):
        try:
            res=requests.get('http://127.0.0.1:5000/ResidenceDetails/CreateTable?',{'ref':table_name,'x':values})
            return res
        except:
            return "error!"


    def insert_to_table(self,table_name,values):
        try:
            res=requests.get('http://127.0.0.1:5000/ResidenceDetails/InsertToTable',{'ref':table_name,'x':values})
            return res
        except:
            return "error!"
    def updete_table(self,table_name,newvalues):
        try:
            res=requests.get('http://127.0.0.1:5000/'+'ResidenceDetails/UpdateTable',{'ref':table_name,'x':newvalues})
            return res
        except:
            return "error!"

    def  select_from_tables(self,table_name,id):
        try:
            data=requests.get('http://127.0.0.1:5000/'+'ResidenceDetails/GetOwnerVillas',{'ref':table_name,'id':id})
            return data
        except:
            return "error!"
   
    def delet_from_table(self,id):
        res=requests.get('http://127.0.0.1:5000/ResidenceDetails/Delete',{'ref':id})
    
        return res
#    
    





class Real_estate_office:
    dprequests=DbRequests()

    #VillasDataInitialization
    new_villa1=VillasInfo.VillasInfo(1,'A86959433','Amman','A',700000,1)
    new_villa2=VillasInfo.VillasInfo(2,'A86959433','Amman','A',700000,2)
    new_villa3=VillasInfo.VillasInfo(3,'A86959433','Amman','A',700000,1)
    new_villa4=VillasInfo.VillasInfo(4,'A86959433','Amman','A',700000,5)
    new_villa5=VillasInfo.VillasInfo(5,'A86959433','Amman','A',700000,7)
    new_villa6=VillasInfo.VillasInfo(6,'A86959433','Amman','A',700000,3)
    new_villa7=VillasInfo.VillasInfo(7,'A86959433','Amman','A',700000,1)
    new_villa8=VillasInfo.VillasInfo(8,'A86959433','Amman','A',700000,2)
    new_villa9=VillasInfo.VillasInfo(9,'A86959433','Amman','A',700000,1)
    new_villa10=VillasInfo.VillasInfo(10,'A86959433','Amman','A',700000,4)
    new_villa11=VillasInfo.VillasInfo(11,'A86959433','Amman','A',700000,1)
    new_villa12=VillasInfo.VillasInfo(12,'A86959433','Amman','A',700000,3)
    new_villa13=VillasInfo.VillasInfo(13,'A86959433','Amman','A',700000,6)

    ##create villasInfo table
    print('***************************************************************************')
    print('**********************CreateVillsInfoTable*********************************')

    villas=json.dumps(dict(VillasInfo.VillasInfo.get_villas_json()))
    dprequests.creat_table('VillasInfo',villas)

    ##insert a new villa to the villasInfo table
    print('***************************************************************************')
    print('**********************InsertNewVilla*********************************')
    new_villa14=VillasInfo.VillasInfo(5,'A86959433','Amman','A',700000,1)
    villa=json.dumps(new_villa14.get_villa_json())
    villa_id=new_villa14.get_villa_id()
    dprequests.insert_to_table('VillasInfo/'+str(villa_id),villa)

    ##update villa in a table
    print('***************************************************************************')
    print('**********************UpdateVilla13Info*********************************')
    villa = new_villa13.set_villa_location('Aqaba')
    villa=json.dumps(new_villa13.get_villa_json())
    villa_id=new_villa13.get_villa_id()
    dprequests.updete_table('VillasInfo/'+str(villa_id),villa)



    ##delete villa from table
    print('***************************************************************************')
    print('**********************DeleteVilla14sInfo**********************************')
    dprequests.delet_from_table('VillasInfo/'+str(new_villa14.get_villa_id()))

    ## return All Data:
    print('***************************************************************************')
    print('**********************ReturnAllInfo**********************************')
    dprequests.get_data()


    #OwnersDataInitialization
    new_owner_1=OwnersDetails.OwnersDetails(1,'Ahmad','salameh','07495403023','Amman',2,{new_villa1.get_villa_id():new_villa1.get_villa_json(),new_villa10.get_villa_id():new_villa10.get_villa_json()})
    new_owner_2=OwnersDetails.OwnersDetails(2,'rami','maani','07495407923','jerrash',1,{new_villa11.get_villa_id():new_villa11.get_villa_json()})
    new_owner_3=OwnersDetails.OwnersDetails(3,'mohammad','mahasneh','074765403023','maan',3,{new_villa5.get_villa_id():new_villa5.get_villa_json(),new_villa6.get_villa_id():new_villa6.get_villa_json(),new_villa14.get_villa_id():new_villa14.get_villa_json()})
    new_owner_4=OwnersDetails.OwnersDetails(4,'iman','hindi','07496543023','Amman',2,{new_villa12.get_villa_id():new_villa12.get_villa_json(),new_villa7.get_villa_id():new_villa7.get_villa_json()})
    new_owner_5=OwnersDetails.OwnersDetails(5,'Ghaith','hussein','074565403023','zarqa',1,{new_villa8.get_villa_id():new_villa8.get_villa_json()})
    new_owner_6=OwnersDetails.OwnersDetails(6,'salam','badi','074954055623','Amman',2,{new_villa9.get_villa_id():new_villa9.get_villa_json(),new_villa2.get_villa_id():new_villa2.get_villa_json()})

    #create Owners Details Table:
    print('***************************************************************************')
    print('**********************CreateOwnersDetailsTable*****************************')

    owners=json.dumps(dict(OwnersDetails.OwnersDetails.get_owners_json()))
    res=dprequests.creat_table('OwnerDetails',owners)
    print(res.text)

 
    
    #insert a new owner to the OwnerDetails table
    print('**************************************************************************')
    print('**********************insertOwnerofId7Details*****************************')

    new_owner_8=OwnersDetails.OwnersDetails(7,'salem','saleem','07495403023','mafraq',1,{new_villa8.get_villa_id():json.dumps(new_villa8.get_villa_json())})
    owner=json.dumps(new_owner_8.get_owner_json())
    owner_id=new_owner_8.get_owner_id()
    res=dprequests.insert_to_table('OwnerDetails/'+str(owner_id),owner)
    print(res.text)

    #update owner in a table
    print('*********************************************************************')
    print('**********************UpdatOwner6Details*****************************')

    owner=OwnersDetails.OwnersDetails(6,'Maram','saleem','07495403023','Karak',4,[json.dumps(new_villa8.get_villa_json())])
    owner=json.dumps(owner.get_owner_json())
    owner_id=new_owner_6.get_owner_id()
    res=dprequests.updete_table('OwnerDetails/'+str(owner_id),owner)
    print(res.text)


    #delete owner from table
    print('**********************************************************************')
    print('**********************DeleteOwner3Details*****************************')

    dprequests.delet_from_table('OwnerDetails/'+str(new_owner_3.get_owner_id()))
    print(res.text)

    #select and return villas for a specific owner:
    print('****************************************************************')
    print('**********************Owner4Details*****************************')

    res=dprequests.select_from_tables('OwnerDetails',new_owner_4.get_owner_id())
    print(res.text)


re=Real_estate_office()