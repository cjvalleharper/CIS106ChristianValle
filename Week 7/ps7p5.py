# input
choice = input("Start the program? ")


# process
while choice == "Yes":
  qty = float(input("Input Quantity: "))
  price = float(input("Input Price: "))
  extprice =  price*qty
  if extprice > 10000:
    discount = .25
  else: discount=.10
  discountamount = extprice*discount
  total = extprice-discountamount
  print("Order details")
  print("Discount Amount: $",discountamount)
  print("Total Sale: $",total)
  choice = input("Run again? ")

# output
print("Goodbye...")