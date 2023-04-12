#Q4
#defined a function
def no():
#defined a loop
  myNumbers=[]
#get input from user
  myrange=int(input("Enter the range "))
#print the number list based on the input from user
  for i in range (1,myrange+1):
    myNumbers.append(i)
  print("List of numbers:")
  print(myNumbers)
#defined another loop
  greater=[]
#print the numbers of loop which were larger than 12
  for i in range(1, myrange+1):
    if (myNumbers[i-1]>12):
      greater.append(myNumbers[i-1])
  print("list of numbers that are larger than 12:")
  print (greater)
no()

