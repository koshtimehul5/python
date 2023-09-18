print("3\n4    5\n6       7\n   4")

for i in range(1,11):
    print(i)
i=1
while i<11:
    print(i)
    i=i+1



userone=int(input("Enter the Number1 : "))
for i in range(1,11):
    print(userone,"*", i,"=",userone*i)

#reverse Number
num = int(input("Enter an integer number: "))
reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)

#Get the key of a minimum value from the following dictionary
sample = {'Physics': 82, 'Math': 65, 'history': 75}
temp = min(sample.values())
res = [key for key in sample if sample[key] == temp]
print("Keys with minimum values are : " + str(res))