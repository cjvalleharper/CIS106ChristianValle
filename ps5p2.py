# input
item = input("Enter Item ")
qty = float(input("Enter Quantity "))



# process
if item == "A":
  up = 10
else:
  up = 20

extprice = qty*up

# output
print("Total Price is: $",extprice)
