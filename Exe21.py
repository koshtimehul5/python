name=input("Please Enter The Name : ")
encryptedName = name[0] + '*' * (len(name) - 2) + name[-1]
print(encryptedName)

for i in range(1,5):
    print(chr(65+i)+" "*(i+1))

# for i in range(1,4):
#     for j in range(i):
#         print(" ", end='')
#     for k in range(2 + i):
#         print(" ", end='')
#         print(chr(65+ i), end='')
#     print()