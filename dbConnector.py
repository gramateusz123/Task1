import mysql.connector
data_bases = []
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  data_bases.append(x)

for x in data_bases:
  print(x)
  
if "library" in data_bases:
  print("This library already exist!")