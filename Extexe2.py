# lenth=float(input("Enter The Lenth"))
# breath=float(input("Enter The Breath"))
#
# if(lenth == breath):
#     print("It is a Sqare")
# else:
#     print("It is not a Sqare")
#
# for i in range(3,8):
#     for j in range(4):
#         for k in range(1,3):
#             print("Mehul")
# i=0
# while(i<5):
#     print("Hi")
#     i=i+1

# i=0
# j=1
# while(i<2):
#     while(j<3):
#         print(i)
#         i=i+1
#         j=j+1
# for i in range(1,5):
#     for j in range(2,6):
#         if(j==3):
#             break
#         else:
#             print(j)
for i in range(1,10,5):
    for j in range(10,0,-3):
        if(j==4):
            break
        else:
            print(j)

for i in range(0,6,7):
    for j in range(10,0,-6):
        if(j==4):
            continue
        else:
            print(j)