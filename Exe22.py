first_celsius = int(input("Enter the first amount in Celsius: "))
last_celsius = int(input("Enter the last amount in Celsius: "))

print("\nCELSIUS \tFAHRENHEIT")

for celsius in range(first_celsius, last_celsius + 1):
     fahrenheit = celsius * 9/5 + 32
     print(celsius," \t\t",fahrenheit)

for i in range(0,5):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()

for i in range(5,0,-1):
     for j in range (1,i+1):
         print("*",end="")
     print()