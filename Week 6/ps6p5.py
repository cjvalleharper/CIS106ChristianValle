# input
name = input("Input Last Name: ")
salary = float(input("Input Salary: "))
joblevel = float(input("Input Job Level: "))

# processing
if joblevel >= 10:
  bonus = .25
elif joblevel >= 5:
  bonus = .20
else: bonus = .10
  
total = salary+(salary*bonus)

# output
print("Info for: ",name)
print("Total with Bonus is: $",total)