file=open("test.txt",'r')

for each in file:
    print(each)

file = open('test.txt','w')
file.write('This is the write Command')
file.write('It allows us to write in a Particuler file')
file.close()

f = open("test.txt", "r")
print(f.read())

