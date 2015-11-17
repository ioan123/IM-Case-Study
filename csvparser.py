####################### CSV PARSER - DATABASE CREATOR #############################
#					    --- Name: Ioannis Nianios ---  							  #  
#					--- email: ioan.nianios@gmail.com ---                         #



import csv
import MySQLdb
import sys
import json
from pprint import pprint
#from unicode import unicode

mydb = MySQLdb.connect(host='173.194.86.97',
    user='root',
    passwd='fudge',
    db='IOAN')
	

cursor = mydb.cursor()

### execute the SQL query using execute() method. ###
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print "\n\tServer version:", row[0]
print "\n\t up and running ...\n\n"


##################### CREATING TABLES FOR DATABASE ############################
create_tables = """
					
					CREATE TABLE COUNTRIES(
					id INT NOT NULL,
					alpha2 VARCHAR(2),
					alpha3 VARCHAR(3),
					name VARCHAR(50),
					targetable INT,
					
					PRIMARY KEY (id)
					);
					
					CREATE TABLE REGIONS(
					id INT NOT NULL,
					country_id INT NOT NULL,
					name VARCHAR(30),
					iso_code VARCHAR(5),
					
					PRIMARY KEY (id)
					);
					
					CREATE TABLE CITIES(
					id INT NOT NULL,
					country_id INT NOT NULL,
					region_id INT,
					name VARCHAR(30),
					iso_code VARCHAR(5),
					
					PRIMARY KEY (id)
					);				
					"""
					

#cursor.execute(create_tables);


### print all the first cell of all the rows ###
cursor.execute("USE IOAN")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
		
### PRINTING THE TABLES OF THE DATABASE ###
for (table_name,) in cursor:
    print(table_name)
"""
### Trying to print out values from column
cursor.execute("SELECT id FROM COUNTRIES")
csv_file = cursor.fetchall()
for row in csv_file:
		print"in for"
		print "%s"% (row[id])
"""	

##### INSERTING THE FILES INTO THE DATABASE ####################################
csv_countries = csv.reader(file('countries.csv'))
csv_regions = csv.reader(file('regions.csv'))


"""CREATE TABLE CITIES(
					id INT NOT NULL,
					country_id INT,
					region_id INT,
					name VARCHAR(30),
					iso_code VARCHAR(5),
					
					PRIMARY KEY (id)
					);	"""

"""
firstline = True
for row in csv_countries:
	if firstline:
		firstline=False
		continue
	#print "\ninserting rows..."
	ins = ("INSERT INTO COUNTRIES"
			"(id, alpha2, alpha3, name, targetable)"
			"VALUES(%s,%s,%s,%s,%s);"
			)
	cursor.execute(ins,row)
		
"""

#cursor.execute("DROP TABLE REGIONS")
"""
firstline = True
for row in csv_regions:
	if firstline:
		firstline=False
		continue
	try:
	#print "\ninserting rows..."
		ins = ("INSERT INTO REGIONS"
			"(id, country_id, name, iso_code)"
			"VALUES(%s,%s,%s,%s);"
			)
		
		cursor.execute(ins, row)
		mydb.commit()
	except:
		mydb.rollback()
		print"ROW: ",row
		sys.exit()

"""
###################### PARSING JSON FILE #####################################
data = []
with open('cities') as f:
	for line in f:
		#print line
		#for key in 
		data.append(json.loads(line))		
		
################# INSERTING CITIES FILE INTO DATABASE  #######################		
"""
i=0
for line in data:
	
	if 'id' in line:
		id =  data[i]["id"]
	else: 
		id = 0		
	if 'country_id' in line:
		cid = data[i]["country_id"]
	else: 
		cid = 0		
	if 'region_id' in line:
		rid = data[i]["region_id"]
	else: 
		rid = 0
	if 'name' in line:
		name = data[i]["name"]
	else: 
		name = "None"			
	if 'iso_code' in line:
		iso = data[i]["iso_code"]
	else: 
		iso = "None"	
	#print id, cid, rid, name, iso
	try:		
	cursor.execute("INSERT INTO CITIES"
		"(id,country_id,region_id,name,iso_code)" 
		"VALUES(%s,%s,%s,%s,%s);",(id,cid,rid,name,iso))
	except:
		print"ERROR INSERTING DATA AT ROW:",i,line
		sys.exit()	
	i+=1
"""

##### CREATING USER #####
#cursor.execute("FLUSH PRIVILEGES;")
#cursor.execute("CREATE USER 'v_user'@'173.194.86.97' IDENTIFIED BY '123'; ")
#cursor.execute("GRANT SHOW VIEW ON IOAN.* TO 'v_user'@'173.194.86.97'; ")


########################### CITY INFORMATION #########################
#Input from user
user_input = raw_input("Type in City of preference: ")

cursor.execute(""" 
 SELECT * FROM CITIES c JOIN COUNTRIES n ON c.country_id=n.id JOIN REGIONS r ON c.region_id = r.id AND c.name=%s;
 """, (user_input,))
 
#cursor.execute("SELECT * FROM CITIES c WHERE c.name=%s;",(user_input,))

#Fetch the result and put into an array
results = cursor.fetchall()

for line in results:
	print line
#################################################################	
	
mydb.commit()
cursor.close()
# close the connection
mydb.close()



