# input
print("Welecome to CJ's Paint Gallon Calculator. This code should help you figure out")
print("how much paint you would need to buy to paint a room.")
choice = input("Run the Program? (Y/N): ")


# process
while choice == "Y":
  L = float(input("Input Length: "))
  W = float(input("Input Width: "))
  H = float(input("Input Height: "))

  SquareFoot = 2*(L * W * H)+2*(L * W * H)+2*(L * W * H)
  Gallons = SquareFoot/50

  # output
  print("Square footage of room is: ",SquareFoot)
  print("Prediction for paint gallons needed is: ",Gallons)
  choice = input("Run the Program again? (Y/N): ")



