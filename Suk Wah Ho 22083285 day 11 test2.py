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
     
   elif option==2:
    productname=input("Enter name to search: ")
    h=True
    for i in phoneDirectory.keys():
       if (i==name):
        print(i+":"+phoneDirectory[i])
        h=False
       if h:
        print("Not Found")
        h=h<1
   elif option==3:
       name=input("Enter name: ")
       phonenumber=input("Enter new 10-digit phone number: ")   
   phoneDirectory.update({name:phonenumber})
   print("Record updated")