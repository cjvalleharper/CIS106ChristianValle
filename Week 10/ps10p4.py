# input
print("Welecome to CJ's Terrific Ticket Calculator! This code should help you figure out")
print("how much a ticket would cost to get you downtown Chicago!")
choice = input("Run the Program? (Y/N): ")


# process
while choice == "Y":
 name = input("Input last name: ")
 miles = float(input("Input distance (miles): "))

 if miles > 29:
   price = 12
 elif miles > 19:
   price = 10
 elif miles > 9:
   price = 8
 else:
   price = 5

 # output
 print("Ticket price is: $",price)
 choice = input("Run the Program again? (Y/N): ")



