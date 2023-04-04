#part3
salary=float(input("Please enter your salary in Germany: "))
country=input("Enter the country you want to migrate: ")
def convertSalary(country, salary):
  if country.lower()=="canada":
    final=salary*1.55
    if final >64000:
      print("You will be rich in Canada with a salary of " ,final, "CAD")
    else:
      print("You will be poor in Canada with a salary of " ,final, "CAD")
  elif country.lower()=="usa":
    final=salary*1.18
    if final >56516:
       print("You will be rich in USA with a salary of " ,final, " US Dollars")
    else:
      print("You will be poor in USA with a salary of " ,final, " US Dollars")
  elif country.lower()=="cambodia":
    final=salary*4847.38
    if final > 5649856:
       print("You will be rich in Cambodia with a salary of " ,final, " Cambodian Riel")
    else:
      print("You will be poor in Cambodia with a salary of " ,final, " Cambodian Riel")
  elif country.lower()=="united kingdom":
    final=salary*1.2
    if final>35423:
      print("You will be rich in United Kingdom with a salary of " ,final, " Pound Sterling") 
    else:
      print("You will be poor in United Kingdom with a salary of " ,final, " Pound Sterling")
  else:
    print("Error") 

convertSalary(country, salary)

    

    
    
    
    
  