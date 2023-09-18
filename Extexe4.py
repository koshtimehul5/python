quantaty=int(input("Please Enter your quantaty:"))

costPerUnit=100

cost = quantaty * costPerUnit

if(cost > 1000):
    discount = cost * 0.10
    totalCost = cost - discount
    print(discount)
    print("Total Cost for",quantaty,"item is:",totalCost)
else:
    print("Total Cost for", quantaty, "item is:", cost)