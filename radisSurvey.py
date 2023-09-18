radisList=[]
radisFile=open("C:\\Users\\Admin\\Desktop\\radishsurvey.txt",'r')
for i in radisFile.readlines():
    radisList.append(i)
# print(radisList)

newRadisList=[]
for j in radisList:
    nRemoval=j.replace("\n",'')
    newRadisList.append(nRemoval.upper())
    newRadisList.sort()

# print(newRadisList)

my_Dict={}
for item in newRadisList:
    myDist=item.split(" - ")
    key, value = myDist
    my_Dict[key] = value

# newFile=open("C:\\Users\\Admin\\Desktop\\NewRadisFIle2.txt",'w')
# for key, value in my_Dict.items():
#      newFile.write(f'{key}: {value}\n')

value_counts={}
for value in my_Dict.values():
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

item_counts={}

for item, count in value_counts.items():
    item_name = item.strip()

    if item_name in item_counts:
        item_counts[item_name] += count
    else:
        item_counts[item_name] = count
mostCommon=max(item_counts,key=item_counts.get)
mostValue=item_counts[mostCommon]
print(mostCommon,":",mostValue)
mostPopular=min(item_counts,key=item_counts.get)
mostPopValue=item_counts[mostPopular]
print(mostPopular,":",mostPopValue)

# Print the counts
# for item, count in item_counts.items():
#     print(f"{item} = {count}")


#
