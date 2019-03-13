import time
def text():
  print("Welcome to the Library database!")
  print("What do you want to do?")
  print("1. Show book list.")
  print("2. Add new book.")
  print("3. Close the program.")

def end():
  close = 0
  while close == 0:
    print("Do you want to exit program ? Y/N")
    exit = input()
    if exit == "Y" or exit == "y":
      quit()
    elif exit == "N" or exit == "n":
      close = 1
      time.sleep(0.5)
      print('\n')