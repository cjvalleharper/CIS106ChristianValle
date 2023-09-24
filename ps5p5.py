# input
lname = input("Input Last Name: ")
nod = float(input("Input Number of Dependants: "))
gross = float(input("Input Gross Income: "))


# process
agi = (gross-nod)-12000

if agi > 50000:
  taxrate = .20
else: taxrate = .10

inctax = agi*taxrate

if inctax < 0:
  inctax = 100
else: inctax = inctax

# output
print("Info for ",lname)
print("Gross income: $",gross)
print("Number of Dependants: ",nod)
print("Adjusted Gross Income: $",agi)
print("Income Tax: $",inctax)