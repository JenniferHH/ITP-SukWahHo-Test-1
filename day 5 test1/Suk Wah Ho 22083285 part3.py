#part3
salary=int(input("Please enter your salary in Germany: "))
country=input("Enter the country you want to migrate: ")
def convertSalary():
  if country=="Canada":
    finalsalary=int(salary*56)
  elif country=="USA":
    finalsalary=int(salary*1.18)
  elif country=="Cambodia":
    finalsalary=int(salary*4,847.38)
  else:
    finalsalary=int(salary*	
0.91)
  convertSalary()
  if finalsalary>=64000:
     print("You will be rich in Canada with a salary of " + finalsalary + "CAD")
    

    
    
    
    
  