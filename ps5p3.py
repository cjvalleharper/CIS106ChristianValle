# input
qty = float(input("Input Quantity: "))
cpb = float(input("Input Cost per Book: "))



# processing
extprice = qty*cpb

if extprice < 50:
  sp = 25
else:
  sp = 50

total = extprice+sp

# output
print("Shipping is: $",sp)
print("Total is: $",total)