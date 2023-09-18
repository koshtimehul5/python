# # def add(num1,num2):
# #     sum=num1+num2
# #     print(sum)
# # def sub(num1,num2):
# #     sub=num1-num2
# #     print(sub)
# # def mul(num1,num2):
# #     mul= num1*num2
# #     print(mul)
# # def div(num1,num2):
# #     div=num1/num2
# #     print(div)
# # def mod(num1,num2):
# #     mod=num1%num2
# #     print(mod)
# #
# # while True:
# #     print('Welcome to "Prince`s" calculator\nPress 1 to add\nPress 2 to subtract\nPress 3 to muliply\nPress 4 to divide\nPress 5 to modulus\nPress 6 to exit')
# #     choice=int(input("Enter the number :"))
# #     # num1 = int(input("Enter the number 1:"))
# #     # num2 = int(input("Enter the number 2:"))
# #     #
# #     if choice == 1:
# #         num1 = int(input("Enter the number 1:"))
# #         num2 = int(input("Enter the number 2:"))
# #         print('You chose "Addition"')
# #         add(num1, num2)
# #     elif choice == 2:
# #         num1 = int(input("Enter the number 1:"))
# #         num2 = int(input("Enter the number 2:"))
# #         print('You chose "Subtraction"')
# #         sub(num1, num2)
# #     elif choice == 3:
# #         num1 = int(input("Enter the number 1:"))
# #         num2 = int(input("Enter the number 2:"))
# #         print('You chose "Multiply"')
# #         mul(num1, num2)
# #     elif choice == 4:
# #         num1 = int(input("Enter the number 1:"))
# #         num2 = int(input("Enter the number 2:"))
# #         print('You chose "divide')
# #         div(num1, num2)
# #     elif choice == 5:
# #         num1 = int(input("Enter the number 1:"))
# #         num2 = int(input("Enter the number 2:"))
# #         print('You chose "modulus"')
# #         mod(num1, num2)
# #     else:
# #         exit()
# #     question = input("Would you like to continue (Y/N) ?:  ")
# #     if question.upper() != "Y":
# #         print("thank you for your time")
# #         break
#
# def firstUser(choice):
#     if(choice == 1):
#         print(choice)
#
# choice=int(input("Please Enter the Value : "))
# choice=firstUser(choice)





# question -1:
print("3\n\n4\n\t\t5\n\n6\t\t\t\t7\n\t\t\t4")
# question: 2:
i=1

while(i<11):
    naturalnumbers = int(input("enter first 10 natural numbers"))
    print(1,2,3,4,5,6,7,8,9,10)
    i=i+1
    # print()


# question:3

num = 8
for i in range(1,11):
    print(num, "X", i, "=", num*i)

# question 4:

num = 76542
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: " + str(reversed_num))

# question 5:

sample_dict = {"Physics": 82,"Math": 65,"history": 75}
min_value = min(sample_dict.values())
print(min_value)