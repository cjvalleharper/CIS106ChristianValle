# inputs
name = input("Input product name ")
cost = float(input("Input product cost "))


# processing
if cost > 1000:
  war = cost*.1
else: war = cost*.05

total = cost+war

# output
print("Costs for: ",name)
print("Warrantee cost: $",war)
print("Total cost: $",total)