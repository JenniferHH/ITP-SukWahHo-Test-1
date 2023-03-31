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

    





 

  


