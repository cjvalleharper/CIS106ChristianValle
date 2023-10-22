# input

qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))

# process
total = 0
extprice = qty*price

print("Extended Price is: $",extprice)

if extprice > 10000:
  discount = extprice * .1
else:
  discount = 0

total = extprice - discount

choice = input("Do you wish to run this program? (y/n): ")

while choice == "y":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
  extprice = qty*price
  print("Extended Price is: $",extprice)
  if extprice > 10000:
    discount = extprice * .1
  else:
    discount = 0
  total = extprice - discount
  print("Total price is: $",total)
  choice = input("Do you wish to run this program? (y/n): ")