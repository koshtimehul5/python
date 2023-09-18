def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero"
    return x % y


while True:
    print("Welcome to 'Atharv's' calculator")
    print("Press 1 to add")
    print("Press 2 to subtract")
    print("Press 3 to multiply")
    print("Press 4 to divide")
    print("Press 5 to modulus")
    print("Press 6 to exit")

    choice = input("Choose an option: ")

    if choice == '6':
        print("Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if choice == '1':
            result = add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "Division"
        elif choice == '5':
            result = modulus(num1, num2)
            operation = "Modulus"

        print(f"{operation} result is: {result}")

    else:
        print("Invalid choice. Please choose a valid option.")

    continue_option = input("Would you like to continue? (Yes/No): ").strip().lower()
    if continue_option != 'yes':
        print("Goodbye!")
        break
