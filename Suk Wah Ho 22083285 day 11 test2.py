phoneDirectory={}
option=0
print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
print("1. Add a record")
print("2. Search a record")
print("3. Update a record")
print("4. Delete a record")
print("5. Quit")
while option!=5:
   option=int(input("Enter your choice: "))
   if option==1:
    name=input("Enter name: ")
    phonenumber=input("Enter your 10-digit phone number: ")
   phoneDirectory.update({name:phonenumber})
   print("Record added")