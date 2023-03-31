#Q1
#show clinic's name 
print("Melanie Dental Clinic")
print("* ----------------------------*")
#take the patient's name from user
patient_name = input("Receipt for patient name: ??? \n")
print("----------------------------------------------")
#take cleaning performed, cavity-filling performed and X-Ray performed from user
a = input("Was cleaning performed?(y/n)")
b = input("Was cavity-filling performed?(y/n)")
c = input("Was X-Ray performed?(y/n)")
#calculate function
def calculate(a, b, c):
  if a == "y":
    a= 60
  else:
    a = 0
  if b == "y":
    b= 200
  else:
    b= 0
  if c == "y":
    c= 100
  else:
    c= 0
  d = int(a) + int(b) + int(c)
  return d
subtotal = calculate(a, b, c)
#decision-making statement
#If it is more than $300, give a 10% discount.
if(subtotal>300):
  subtotal= (((int(calculate(a, b, c))) *(int(10)))/(int(100)))
#If the bill of a patient is more than $200, give the user 5% discount
elif (subtotal>200) and (subtotal<300):
  subtotal= (((int(calculate(a, b, c))) *(int(5)))/(int(100)))
else:
#Otherwise keep the same total.
  subtotal=(((int(calculate(a, b, c))) *(int(15)))/(int(100)))
print("Subtotal: $" + str(subtotal))
print("Tax: 15%")
print("------------------------------------------------")
#show the result
print("Total: $" + str(subtotal))

#Q2
#function takeInput()
def takeInput():
#take numbers and operator from user
    a = int(input("Please enter a number: \n"))
    b = int(input("Please enter another number: \n"))
    c = input("Please enter an operator: \n")
    return a, b, c
#function displayResult()
def displayResult():
#return three values to a, b, c from takeInput()
    a, b, c = takeInput()
    if c == "+":
        d = a + b
#show formula
        print(f"{a} + {b} = {d}")
    elif c == "-":
        d = a - b
#show formula
        print(f"{a} - {b} = {d}")
    elif c == "*":
        d = a * b
#show formula
        print(f"{a} * {b} = {d}")
    else:
        d = a / b
#show formula
        print(f"{a} / {b} = {d}")
displayResult()

#Q3
#take number of pennies, nickels, dimes and quarters from user 
a=int(input("Enter the number of pennies: "))
b=int(input("Enter number of nickels: "))
c=int(input("Enter number of dimes: "))
d=int(input("Enter number of quarters: "))
#calculate totalCent
totalCent=(a*1+b*5+c*10+d*25)
#calculate totalDollars
totalDollars=(totalCent/100)
# If the totalDollars value is greater than 1.0
if (totalDollars>1.0):
  print("Sorry, the amount you entered was more than one dollar.")
#If the totalDollars value is less than 1.0
elif (totalDollars<1.0):
  print("Sorry, the amount you entered was less than one dollar.")
# If the totalDollars value is 1.0
else:
  print ("Congratulations!")
  print ("The amount you entered was exactly one dollar!")
  print ("You win the game!!")

    
  
  


 

  


