
import sqlite3


conn=sqlite3.connect('ResidenceDetails.db')

cur =conn.cursor()

#query='''CREATE TABLE VillasInfo (
#    VillaID int NOT NULL PRIMARY KEY,
#    OwnerName varchar(255),
#    Location varchar(255),
#    Size int,
#    Price int,
#    floors int
#); '''
#
#cur.execute(query)
#conn.commit()


#query='''CREATE TABLE OwnersDetails (
#    OwnerID int NOT NULL PRIMARY KEY,
#    OwnerName varchar(255),
#    Phone varchar(255),
#    Address varchar(255)
#); '''
#cur.execute(query)
#conn.commit()


#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (7,'Rami',6,'Amman',450,500000,2)"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (8,'Iman',1,'Amman',750,600000,2)"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (9,'Rami',6,'Ajloun',1200,950000,3)"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (10,'Joudi',3,'Karak',300,400000,1)"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (11,'Joudi',3,'Amman',600,750000,3)"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO VillasInfo (VillaID, OwnerName,OwnerID, Location, Size,Price,floors) VALUES (12,'Ghaith',2,'Zarqa',700,500000,2)"
#cur.execute(query)
#conn.commit()








#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (1,'Iman','076965844','Amman')"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (2,'Ghaith','656777765','Amman')"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (3,'Joudi','234565433','Zarqa')"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (4,'Jamal','67886544','Madaba')"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (5,'Ghina','345678908','Aqaba')"
#cur.execute(query)
#conn.commit()
#query="INSERT INTO OwnersDetails (OwnerID, OwnerName, Phone, Address) VALUES (6,'Rami','998764433','Amman')"
#cur.execute(query)
#conn.commit()
#query='''ALTER TABLE VillasInfo
#ADD  FOREIGN KEY (OwnerID) REFERENCES OwnersDetails (OwnerID);'''

#query='''CREATE TABLE VillasInfo(
#    VillaID INT NOT NULL PRIMARY KEY,
#    OwnerName varchar(255),
#    OwnerID int,
#    Location varchar(255),
#    Size int,
#    Price int,
#    floors int,
#    CONSTRAINT fk_OwnerID
#        FOREIGN KEY (OwnerID)
#        REFERENCES OwnersDetails(OwnerID)
#);'''
#cur.execute(query)
#conn.commit()

#query='''INSERT INTO VillasInfo SELECT * FROM _VillasInfo_old;'''
#cur.execute(query)
#conn.commit()


#CREATE TABLE departments
#( department_id INTEGER PRIMARY KEY AUTOINCREMENT,
#  department_name VARCHAR
#);
#
#CREATE TABLE employees
#( employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
#  last_name VARCHAR NOT NULL,
#  first_name VARCHAR,
#  department_id INTEGER,
#  CONSTRAINT fk_departments
#    FOREIGN KEY (department_id)
#    REFERENCES departments(department_id)
#);


#query='''ALTER TABLE VillasInfo
#ADD CONSTRAINT FK_OwnerID
#FOREIGN KEY (OwnerID) REFERENCES OwnersDetails(OwnerID);'''
#
#cur.execute(query)
#conn.commit()
#query='''ALTER TABLE OwnersDetails
#DROP COLUMN FOREIGNKEY;'''
#cur.execute(query)
#conn.commit()

#CREATE TABLE IF NOT EXISTS some_table (id INTEGER PRIMARY KEY AUTOINCREMENT, ...);

#query="INSERT INTO VillasInfo (VillaID, OwnerName, Location, Size,Price,floors) VALUES (10,'Iman','Irbid',350,350000,1)"
#cur.execute(query)
#conn.commit()
#INNER JOIN OwnersDetails ON OwnersDetails.OwnerName = VillasInfo.OwnerName;'''
#query="SELECT * FROM Persons"
#query="update Persons set FirstName='Ahmad' where PersonID=1 "
print(cur.execute(query).fetchall())
#conn.commit()
#print(Data)
conn.close()


