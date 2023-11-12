# input

qty = float(input("Input Quantity: "))
price = float(input("Input Price: "))
rate = float(input("Input Discount Rate (Decimal Form): "))



# process

extprice = qty*price
discount = extprice*rate
total = extprice-discount


# output

print("Discount is: $",discount)
print("Total cosdt is: $",total)