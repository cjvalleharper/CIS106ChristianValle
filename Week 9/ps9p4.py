# input

name = input("Enter Last Name: ")
code = input("Enter Job Code: ")
hours = float(input("Hours worked: "))

# process
if hours > 40:
    OT = 1.5*(hours-40)
else:
  OT = 0

if code == "L":
  pay = OT+hours*25
elif code == "A":
  pay = OT+hours*30
else: pay = OT+hours*50

print("Pay for: ",name ,"is: $",pay)