#Q1
#identified year and total
years=int(input("Enter the number of years: "))
total=0
for i in range(1,years+1):
#print the input from user
  print("For year",i,":")
  for months in range(1,13):
#get the monthly rainfall amount input from user
    i=float(input("Enter the rainfall amount for the month-"+ str(months) +":"))
    total=float(total+i)
#print the amount of month
print("For "+str(months*years)+" months") 
#print the total rainfal
print("Total rainfal: "+str(total)+" inches")
#print the average monthly rainfall
print("Average monthly rainfall: "+ str(total/(months*years)) + " inches")
