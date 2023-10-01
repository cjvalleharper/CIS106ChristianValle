# input
partnumber = float(input("Input Part Number: "))
qty = float(input("Input Quantity: "))


# process
if partnumber == 99:
  price = 2
elif partnumber == 10 or partnumber == 55:
  price = 1
elif partnumber == 80 or partnumber == 70:
  price = 3
else: price = 5

total = qty * price

# output
print("Total is: $",total)