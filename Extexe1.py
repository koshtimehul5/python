salary = float(input("Enter your salary: "))
yearsOfService = int(input("Enter your years of service: "))

if yearsOfService > 5:
    bonus_percentage = 5
    bonus_amount = (bonus_percentage / 100) * salary
    print(f"Congratulations! You qualify for a {bonus_percentage}% bonus.")
    print(f"Your bonus amount is: £{bonus_amount:.2f}")
else:
    print("Sorry, you do not qualify for a bonus.")