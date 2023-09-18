setA=set(["a","b","c"])
setB=set(["c","d","e"])
# print(setA)
# setA.update(setB)
# print(setA)
setD=setA.intersection(setB)
print(setD)

setOne=set([1,2,3,4])
setTwo=set([3,4,5,6])
setThree=setOne.union(setTwo)
print(setThree)
setFour=setOne.intersection(setTwo)
print(setFour)

symbolToName={
    "H" :"hydrogen",
    "He":"helium",
    "Li" : "lithium",
    "C" : "Carbon",
    "O" : "Oxygen",
    "N" : "Nitrogen"
}
# print(symbolToName)
# print(symbolToName.keys())
# print(symbolToName.values())
symbolToName.update({"P" : "phosphoros","S" : "Sulfer"})
#print(symbolToName)

print(symbolToName.items())
del symbolToName['H']
print(symbolToName)