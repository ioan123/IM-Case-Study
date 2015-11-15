########################################### CSV PARSER - DATABASE CREATOR ###########################################
#					    --- Name: Ioannis Nianios ---  					    #		  #  
#					--- email: ioan.nianios@gmail.com ---                                       #



import csv
import MySQLdb
import sys


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


### CREATING TABLES FOR DATABASE #####
create_tables = """
					CREATE TABLE COUNTRIES(
					id INT NOT NULL,
					alpha2 VARCHAR(5),
					alpha3 VARCHAR(5),
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
					region_id INT NOT NULL,
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

##### INSERTING THE FILES INTO THE DATABASE ######
csv_countries = csv.reader(file('countries.csv'))
csv_cities = csv.reader(file('cities.csv'))
csv_regions = csv.reader(file('regions.csv'))

#cursor.execute("DROP TABLE COUNTRIES;")
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
	#print "\ninserting rows..."
	ins = ("INSERT INTO REGIONS"
			"(id, country_id, name, iso_code)"
			"VALUES(%s,%s,%s,%s);"
			)
	cursor.execute(ins,row)
"""

##### CREATING USER #####
cursor.execute("FLUSH PRIVILEGES;")
cursor.execute("CREATE USER 'v_user'@'173.194.86.97' IDENTIFIED BY '123'; ")
cursor.execute("GRANT SHOW VIEW ON IOAN.* TO 'v_user'@'173.194.86.97'; ")


#print "The result is as follows: " ,achievement

#cursor.execute("SELECT id,answer from leftRightImages")


#Fetch the result and put into an array
#results = cursor.fetchall()

#cursor.execute("UPDATE userResult SET result=%d WHERE id=1" % (achievement))

mydb.commit()
cursor.close()
# close the connection
mydb.close()



