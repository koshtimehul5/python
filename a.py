# # for i in range(65,70):
# #     print(chr(i)*4)
# # for i in range(64,70):
# #          print(i * chr(i+1),end="  ")
# #          print()
#
#
# #
# # employees = ["Mehul = 15000", "Vatsal = 10000", "Maulik = 4000"]
# # print(employees)
# # employees.append("Hardik = 20000")
# # print(employees)
# # del employees[3]
# # print(employees)
# # employees.sort()
# # print(employees)
#
# for i in range(0, 6):
#       for j in range(5-i):
#            print(" ", end="")
#       for k in range(i+1):
#            print(chr(65+i), end=" ")
#       print()
# i = 1
# while (i<7):
#     j=6
#     while (j>i):
#         print(chr(70-i), end=" ")
#         j=j-1
with open("radishsurvey.txt", "r") as file:
    lines = file.readlines()

# Iterate through the lines and count the votes
for line in lines:
    name, radish_type = line.strip().split(" - ")
    name = name.replace(" ", "").upper()
    radish_type = radish_type.replace(" ", "").upper()

    radish_votes[radish_type] += 1
    name_votes[name]+=1
most_popular_radish = radish_votes.most_common(1)
print("The most popular radish type is", most_popular_radish)

least_popular_radish = radish_votes.most_common()[-1]
print("The least popular radish type is", least_popular_radish)
#     print()
#     i=i+1

# Create a dictionary
my_dict = {'apple': 2, 'banana': 1, 'cherry': 2, 'date': 3, 'fig': 3}

# Step 1: Count the occurrences of each value in the dictionary
value_counts = {}
for value in my_dict.values():
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Step 2: Count the occurrences of the same values
same_value_counts = {}
for count in value_counts.values():
    if count in same_value_counts:
        same_value_counts[count] += 1
    else:
        same_value_counts[count] = 1

# Print the occurrences of values in the dictionary
print("Occurrences of values in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Print the occurrences of the same values
print("\nOccurrences of the same values:")
for key, value in same_value_counts.items():
    print(f"Value {key}: Count {value}")





value_counts = {}
for value in my_Dict.values():
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Step 2: Count the occurrences of the same values
same_value_counts = {}
for count in value_counts.values():
    if count in same_value_counts:
        same_value_counts[count] += 1
    else:
        same_value_counts[count] = 1

# Print the occurrences of values in the dictionary
# print("Occurrences of values in the dictionary:")
# for key, value in my_Dict.items():
#     print(f"{key}: {value}")

# Print the occurrences of the same values
print("\nOccurrences of the same values:")
for key, value in same_value_counts.items():
    print(f"Value {key}: Count {value}")

    repeated_names = name_votes.most_common(2)
    print("The most repeate names are", repeated_names)

#Akshsy's Code
from collections import Counter

# Create Counter objects to store the counts
radish_votes = Counter()
name_votes = Counter()

# Read the data from the file

