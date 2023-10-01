# input
qty = float(input("Input Quantity: "))



# processing
if qty >= 25:
  price = 50
elif qty >= 10:
  price = 60
elif qty >= 5:
  price = 70
else: price = 75

total = price*qty

# output
print("Price per Ticket: $",price)
print("Total Price is: $",total)