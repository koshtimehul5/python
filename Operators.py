#arithmetic
#addition

a=10
b=20
print(a+b)

#Substraction

print(b-a)
#Multiplication
print(a*b)
#Division
print(b/a)
#Modulus
print(b%a)

#exponents
print(5**5)
#floor Division
print(b//5)


#assignmentOpraters

x=3
print(x)

x+=10
print(x)

#comparison Operators
x=8
y=12

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#logical Operators and or not
#and
print(x<10 and y<10)
print(not y<10)

#membership Operators
#in
string="Mehul Koshti"
print('e' in string)
#not
m=[10,20,30,40]
print(50 not in m)

#identity
#is #isnot
print(x is y)
print(x is not y)
#bitiwise
#&|^
print(bin(x))
print(bin(y))
print(x&y,bin(x&y))
print(x|y,bin(x|y))
print(x^y,bin(x^y))

#datatypes
d=5
print(d,type(d))
f=5.5
print(f,type(f))
e= 2+4j
print(e,type(e))

s='"Mehul Koshti"'
print(s)
print(s,type(s))
#mutable Data Type
a=[1,2.2,'mehul']
a[2]='vatsal'
print(a,type(a))

#tuple
t=(1,2.2,'mehul',1+3j)
#Dictonary
d={
    'Name':'Mehul',
    'birth':95
}
print(d,type(d))
print(d['Name'])
#set
set={1,2,3,5,3,2}
print(set)
print(set,type(set))