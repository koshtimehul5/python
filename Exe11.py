firstName=input("Please Enter Your First Name : ")
lastName=input("Please Enter Your Last Name : ")
fName=firstName.upper()
lName=lastName.upper()
print(firstName)
print(lastName)
print("Your Full Name is",fName,"",lName)
print("Your initials are ",fName[0] + " " + lName[0])
print("First Name Length",len(fName))
print("First Name Length",len(lName))
fullName= fName + lName
print("Full Name Length",len(fullName))
print("First name indexes are 0 - ",len(fName)-1)
print("Last name indexes are 0 - ",len(lName)-1)
print("First name trims 1 ",fName[0:3])
print("First name trims 2 ",fName[1:5])
print("Last name trims 1 ",lName[0:3])
print("Last name trims 2 ",lName[3:9])
