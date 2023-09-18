weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)

if (bmi < 18.5):
    status = "Underweight"
elif (18.5 <= bmi < 25):
    status = "Normal"
elif (25 <= bmi < 30):
    status = "Overweight"
else:
    status = "Obese"

print(f'\nYour BMI is: {bmi:.2f}\nYou are in the "{status}" range.')