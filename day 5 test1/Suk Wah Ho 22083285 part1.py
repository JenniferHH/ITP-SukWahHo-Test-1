#part1
month=int(input("Enter the month in the numeric form : "))
day=int(input("Enter the day of the month:  "))
year=int(input("Enter the year in two digit format: "))
if (month <=0) and (month >=31):
  print("Error: Invalid Month Input")
elif (day <=0) and (day >=13):
  print("Error: Invalid Day Input")
elif (year<=9) and  (year>= 100):
  print("Error: Invalid Year Input")
else:
  print("The date is " + str(month),str(day),str(year),sep="/") 
  print("Success: Congratulations! you entered the correct date.")
