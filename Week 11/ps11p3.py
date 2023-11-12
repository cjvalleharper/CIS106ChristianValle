# input

lastname = input("Enter your last name: ")
sales = float(input("Enter your sales: "))


# process

if sales > 100000:
    comm = sales*1.1
else: comm = sales*1.05

target = comm*1.05

# output

print("Stats for: ",lastname)
print("Target is: $",target)
print("Commission $",comm)