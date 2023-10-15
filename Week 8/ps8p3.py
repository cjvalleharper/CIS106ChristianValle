# input
name = input("Input Name: ")
salary = float(input("Input Salary: $"))

# Process
if salary >= 100000:
    b = salary*.2
elif salary == 50000:
    b = salary*.15
else:
    b = salary*.1

# output
print("Bonus is: $",b)