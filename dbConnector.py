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
  print("Welcome to the Library database!")
  print("What do you want to do?")
  print("1. Show book list.")
  print("2. Add new book.")
  
decision1 = input()
decision1 = int(decision1)

if decision1==2:
  print("What is the title?:")
  title = input()
  print("Who is an author ?:")
  author = input()
  sql = "INSERT INTO books (title, author) VALUES (%s, %s)"
  val = (title, author)
  mycursor.execute(sql, val)

  mydb.commit()
