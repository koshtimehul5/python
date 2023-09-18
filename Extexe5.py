marks=int(input("Please Enter The Marks : "))

if(marks<25):
    print("Gread : F")
elif(25 > marks < 45 ):
    print("Gread : E")
elif(45 > marks < 50 ):
    print("Gread : D")
elif(50 > marks < 60 ):
    print("Gread : C")
elif(60 > marks < 80 ):
    print("Gread : B")
else:
    print("Gread : A")