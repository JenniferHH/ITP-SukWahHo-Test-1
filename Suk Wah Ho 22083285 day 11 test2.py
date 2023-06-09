phoneDirectory = {}
option = 0
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
print("1. Add a record")
print("2. Search a record")
print("3. Update a record")
print("4. Delete a record")
print("5. Quit")
while option != 5:
  option = int(input("Enter your choice: "))
  if option == 1:
    name = input("Enter name: ")
    if all(i.isalpha() or i.isspace() for i in name):
      phonenumber = int(input("Enter your 10-digit phone number: "))
      if len(str(phonenumber)) != 10:
        print("Enter again")
      else:
        phoneDirectory.update({name: phonenumber})
        print("Record added")
        print("Menu")
        print("1. Add a record")
        print("2. Search a record")
        print("3. Change a record")
        print("4. Delete a record")
        print("5. Quit")
    else:
      print("Enter again")
    
  elif option == 2:
    name = input("Enter name to search: ")
    if all(z.isalpha() or z.isspace() for z in name):
      h = True
      for i in phoneDirectory.keys():
        if (i == name):
          print(i, ":" , phoneDirectory[i])
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
    else:
      print("Enter again")

  elif option == 3:
    name = str(input("Enter name: "))
    if all(i.isalpha() or i.isspace() for i in name):
      phonenumber = int(input("Enter new 10-digit phone number: "))
      if len(str(phonenumber)) != 10:
        print("Enter again")
      else:
        h = True
        for i in phoneDirectory.keys():
          if (i == name):
            phoneDirectory.update({name: phonenumber})
            print("Record updated")
            h = False
          elif h:
            print("Not Found")
            h = h < 1
        print("Menu")
        print("1. Add a record")
        print("2. Search a record")
        print("3. Change a record")
        print("4. Delete a record")
        print("5. Quit")
    else:
      print("Enter again")

  elif option == 4:
    name = str(input("Enter name: "))
    if all(i.isalpha() or i.isspace() for i in name):
      if name in phoneDirectory:
        phoneDirectory.pop(name)
        print("Record deleted")
      else:
       print("Not found")
       print("Menu")
       print("1. Add a record")
       print("2. Search a record")
       print("3. Change a record")
       print("4. Delete a record")
       print("5. Quit")
    else:
      print("Enter again")

  elif option == 5:
    print("Quit")
  else:
    print("Wrong Option Entered")
