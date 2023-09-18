def userInput():
    numOne = int(input("Please Enter The First Value : "))
    numTwo = int(input("Please Enter The Second Value : "))
    return numOne,numTwo
def add(numOne,numTwo):
    sum=numOne+numTwo
    print("Diff Is",sum)
    return numOne,numTwo
def sub(numOne,numTwo):
    sum=numOne-numTwo
    print("Diff Is",sum)
    return numOne,numTwo
def mul(numOne,numTwo):
    sum=numOne*numTwo
    print("Diff Is",sum)
    return numOne,numTwo
def div(numOne,numTwo):
    sum=numOne/numTwo
    print("Diff Is",sum)
    return numOne,numTwo
def modu(numOne,numTwo):
    sum=numOne%numTwo
    print("Diff Is",sum)
    return numOne,numTwo
def options():
 print("Press 1 To Add \nPress 2 To Substract \nPress 3 To Multiply \nPress 4 To Divine \nPress 5 To Modulus \nPress 6 To Exit")

print('Welcome to "Atharv s" Calculator')

while True:
    options()
    inputUser = int(input("Enter The Numer : "))
    if(inputUser==1):
            numOne, numTwo = userInput()
            numOne, numTwo = add(numOne, numTwo)
    elif(inputUser==2):
            numOne, numTwo = userInput()
            numOne, numTwo = sub(numOne, numTwo)
    elif(inputUser==3):
            numOne, numTwo = userInput()
            numOne, numTwo = mul(numOne, numTwo)
    elif(inputUser==4):
            numOne, numTwo = userInput()
            numOne, numTwo = div(numOne, numTwo)
    elif(inputUser==4):
            numOne, numTwo = userInput()
            numOne, numTwo = div(numOne, numTwo)
    elif(inputUser==5):
            numOne, numTwo = userInput()
            numOne, numTwo = modu(numOne, numTwo)
    else:
            exit()
    option = input("Would you like to continue? (Yes/No): ").strip().lower()
    if (option != 'yes'):
        print("Good Bye")
        break
