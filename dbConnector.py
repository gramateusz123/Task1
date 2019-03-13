import mysql.connector
import time
data_bases = []
from func import text
from func import end
close = 0
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

if "('library',)" not in data_bases:
  mycursor.execute("CREATE DATABASE library")
  mycursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255))")

while close == 0:
  text()
  decision1 = input()
  mydb = mysql.connector.connect(                                      #nie mogę wrzucić tego w funkcję, bo wypierdala błąd, że nie jest wskazany database
      host="localhost",
      user="admin",
      passwd="admin",
      database="library"
      )
  mycursor = mydb.cursor()
  
  if decision1=="1":
    mycursor.execute("SELECT * FROM books")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    end()
  
  elif decision1=="2":
    print("What is the title?:")
    title = input()
    print("Who is an author ?:")
    author = input()
    sql = "INSERT INTO books (title, author) VALUES (%s, %s)"
    val = (title, author)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Book successfully added!")
    end()
  
  elif decision1=="3":
    print("See you next time!")
    time.sleep(0.5)
    quit()
  
  else:
    print("Choose an option!")
    close = 0