first=int(input("Please Enter First Age : "))
second=int(input("Please Enter second Age : "))
third=int(input("Please Enter third Age : "))

if(first >= second and first >=third):
    print("First Is Oldest")
elif(second >= first and second >=third):
    print("Second Is Oldest")
elif(third >= first and third >=second):
    print("Second Is Oldest")
else:
    print("All Are Same")