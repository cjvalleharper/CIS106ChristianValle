# input
qty = float(input("Input Quantity"))

# process
if qty >= 1000:
  up = 3
else:
  up = 5

ep = up * qty
tax = ep * 0.07
total = ep + tax

# output
print("Quantity Ordered is: $", qty)
print("Unit Price is: $", up)
print("Extended Price is: $", ep)
print("Tax is: $", tax)
print("Total Order is: $", total)
