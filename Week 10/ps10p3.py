# input
print("Welecome to CJ's Car..Calculator? This code should help you figure out")
print("the Out the door price of a selected car.")
choice = input("Run the Program? (Y/N): ")


# process
while choice == "Y":
 make = input("Input Make of desired car: ")
 model = input("Input Model of desired car: ")
 code = input("Is this an electric car? (Y/N): ")
 msrp = float(input("Input MSRP of desired car: "))

 if code == "Y":
    price = (msrp-msrp*.3)*1.07
 elif make == "Honda" and model == "Accord":
    print("This is the car! ;D")
    price = (msrp-msrp*.1)*1.07
 elif make == "Toyota" and model == "Rav4":
    price = (msrp-msrp*.15)*1.07
 else:
    price = (msrp-msrp*.05)*1.07

 # output
 print("Out the door price of desired car is: $",price)
 choice = input("Run the Program again? (Y/N): ")
