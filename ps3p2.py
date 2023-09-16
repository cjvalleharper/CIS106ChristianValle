# input
purchaseprice = float(input("Input Price Stock was bought at "))
quantity = float(input("Input amount of stock purchased "))
currentprice = float(input("Input current Price "))

# process
value = (currentprice-purchaseprice)*quantity

# output
print("Value of stocks is $",value)