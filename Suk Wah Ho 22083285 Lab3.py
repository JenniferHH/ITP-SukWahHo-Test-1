phoneDirectory = {}
option = 0
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
print("1. Add a record")
print("2. Search a record")
print("3. U1pdate a record")
print("4. Delete a record")
print("5. Quit")
while option != 5:
  option = int(input("Enter your choice: "))
  if option == 1:
    name = str(input("Enter name: "))
    phonenumber = input("Enter your 10-digit phone number: ")
    if len(phonenumber) != 10:
      print ("Enter again")
    else:
      phoneDirectory.update({name: phonenumber})
      print("Record added")
      print("Menu")
      print("1. Add a record")
      print("2. Search a record")
      print("3. Change a record")
      print("4. Delete a record")
      print("5. Quit")

  elif option == 2:
    name = str(input("Enter name to search: "))
    h = True
    for i in phoneDirectory.keys():
      if (i == name):
        print(i + ":" + phoneDirectory[i])
        h = False
      if h:
        print("Not Found")
        h = h < 1
    print("Menu")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

  elif option == 3:
    name = str(input("Enter name: "))
    phonenumber = input("Enter new 10-digit phone number: ")
    if len(phonenumber) != 10:
      print ("Enter again")
    else:
      phoneDirectory.update({name: phonenumber})
      print("Record updated")
      print("Menu")
      print("1. Add a record")
      print("2. Search a record")
      print("3. Change a record")
      print("4. Delete a record")
      print("5. Quit")

  elif option == 4:
    name=str(input("Enter name: "))
    if name in phoneDirectory:
       phoneDirectory.pop(name)
       print("Record deleted")
    else:
       print("Not found")
    print(phoneDirectory)
    print("Menu")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

  elif option == 5:
    print("Quit")
  else:
    print("Wrong Option Entered.")
