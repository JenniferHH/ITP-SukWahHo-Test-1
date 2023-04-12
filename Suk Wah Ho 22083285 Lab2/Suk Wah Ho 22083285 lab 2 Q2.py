#Q2
#set a function
def value():
#get inputs from user
  organisms=float(input("Starting number of organisms: "))
  average=int(input("Average daily percentage increase: "))
  finaldata=int(input("Enter the number of days to display the final data: "))
#print an error message when inputs are negative 
  if organisms and average and finaldata < 0:
    print("Error. Enter again.")
  else:
#print the Day 01 count 
    print("day Approximate                     Population")
    print("-----------------------------------------------")
    print("1                                  ",organisms)
#print other days count
    for i in range(2,finaldata+1):
      organisms=(organisms+(organisms*(average/100)))
      print(i,"                                 ",organisms)   
value()
