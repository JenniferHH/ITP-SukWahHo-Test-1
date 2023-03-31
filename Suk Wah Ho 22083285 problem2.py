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
        print(a,"+",b,"=",d)
    elif c == "-":
        d = a - b
        print(a,"-",b,"=",d)
    elif c == "*":
        d = a * b
        print(a,"*",b,"=",d)
    else:
        d = a / b
        print(a,"/",b,"=",d)
displayResult()
