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
  x = str(x)
  data_bases.append(x)

if "('library',)" in data_bases:
  print("Welcome to the Library database!")
  print("What do you want to do?")
  print("1. Show book list.")
  print("2. Add new book.")


else:
  mycursor.execute("CREATE DATABASE library")
  
  mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="library"
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255))")
print("Welcome to the Library database!" /n "What do you want to do?" /n "1. Show book list." /n "2. Add new book.")