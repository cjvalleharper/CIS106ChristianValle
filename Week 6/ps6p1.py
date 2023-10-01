# input
qty = float(input("Input Quantity: "))

# process
if qty > 10000:
  price = 10
elif qty >= 5000:
  price = 20
else: price = 30

extprice = price*qty
tax = extprice*.07
total = tax+extprice

# output
print("Extended Price is: $",extprice)
print("Tax is: $",tax)
print("Total Price is: $",total)