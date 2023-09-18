# 1
# 4
# 7
#
# repeating 5 time in both loops
#  for i in range (1,6):
#      for j in range (1,10,3):
#          print(j)

# j=0
# k=1
# while(j<6):
#     while(k<10):
#          print(k,k,k,k,k)
#          k += 3
#
#          j += 1

#n = 5  # Define the number of rows in the pattern

# Loop through each row
# for i in range(1, 6):
#      for j in range(6 - i):
#          print(" ", end=" ")
#      for k in range(i):
#          print("*", end=" ")
#      print()

# i=1
# while(i<10):
#     print(i,i+1,i+2)
#     i +=3
# i = 1
# while(i<10):
#     print(i,i+1,i+2,end="")
#     print(" ")
#     if(i%3==0):
#         break
#     else:
#         i +=3
for i in range(0,5):
     for k in range(1+i):
         print(chr(i+65),end=" ")
     print()

# x=""
# for i in "python":
#     x += i
#     print(x)

# for i in range (7,0,-1):
#     for j in range(1,i-1):
#       print("*",end=" ")
#     print()
#
# for i in range(7,0,-1):
#     for j in range(1,i-1):
#         print("1",end=" ")
#     print()
# #
# # for i in range (1,6):
# #     print(i*"* ")
#
# #i=1
# for i in range (5,0,-1):
#    for j in range (5,5+i):
#        print(i, end=" ")
#    print()
for i in range(1, 6):
      for j in range(i):
           print(" ", end=" ")
      for k in range(i):
           print("*", end=" ")
      print()

for i in range (1,6):
    for j in range(65,70):
        print(chr(j),end=" ")
    print()
# i=1
# j=0
# while(i<7):
#     while(j<5):
#         print(5*chr(65+j),end=" ")
#         print()
#         j+=1
#     i+=1
for i in range (0,5):
    for j in range (5-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

name="mehul"
print(len(name))