shoppingCart={}
limit=5
option=0
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1.Add product to the cart.")
print("2. Search the product.")
print("3. Delete the product from the cart.")
print("4. Quit.")
while option!=4:
   option=int(input("Enter your choice: "))
   if option==1:
    n=int(input("Enter the number of items to be added in the stationary shop: "))
    v=0
    while(v<n):
      if len(shoppingCart)<limit:
        productname=input("Enter an item: ")
        brand=input("Enter the brand Name: ")
        shoppingCart.update({productname:brand})
      else:
        print("Cart is full")
      v=v+1
   elif option==2:
      productname=input("Enter the item to be searched: ")
      h=True
      for i in shoppingCart.keys():
       if (i==productname):
        print(i+":"+shoppingCart[i])
        h=False
       if h:
        print("No product exists with this name")
        h=h<1
   elif option==3:
    if productname in shoppingCart:
      shoppingCart.pop(productname)
    print("Cart is empty, no item is found.")
   elif(option==4):
    print("Exit.")
   else:
    print("Wrong Option Entered.")
    

        
    
        
    
    
