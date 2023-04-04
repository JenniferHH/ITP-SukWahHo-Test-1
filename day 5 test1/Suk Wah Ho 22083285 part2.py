#part2
color1=str(input("Enter the first primary color in lower letters: "))
color2=str(input("Enter the second primary color in lower case letters: "))
if (color1!="red") and (color1!="blue") and (color1!="yellow"):
  print("Error: Invalid Color1")
elif (color2!="red") and (color2!="blue") and (color2!="yellow"):
  print("Error: Invalid Color2")
elif color1==color2:
  print("Error: The two colors you entered are same")
else:
  if (color1=="red") and (color2=="blue"):
    print("purple")
  elif (color1=="red") and (color2=="yellow"):
    print("orange")
  if (color1=="blue") and (color2=="red"):
    print("purple")
  elif (color1=="blue") and (color2=="yellow"):
    print("green")
  if (color1=="yellow") and (color2=="red"):
    print("orange")
  elif (color1=="yellow") and (color2=="blue"):
    print("green")
    
    
  