# input

name = input("Enter Last Name: ")
code = input("Enter District Code: ")
hours = float(input("Enter Credit Hours: "))

# process
if code == "I":
  cost = hours*250
else: cost = hours*550

print("Tution cost for ",name, "is: $",cost)