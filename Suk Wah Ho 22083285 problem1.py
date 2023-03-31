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
