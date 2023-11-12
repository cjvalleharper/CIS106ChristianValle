# input

qty = float(input("Input Quantity: "))
price = float(input("Input Price: "))

# process

extprice = qty * price
tax = (extprice * 1.07) - extprice
total = extprice + tax

# output

print("Tax is: $", tax)
print("Total cost is: $", total)
