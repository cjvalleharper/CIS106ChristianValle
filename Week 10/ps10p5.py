# input

choice = input("Run the Program? (Y/N): ")


# process
while choice == "Y":
  print("Valid counties are Cook, DuPage, McHenry, Kane and All others")
  county = input("Enter county to calculate: ")
  value = float(input("Enter value: "))

  if county == "Cook":
    total = value*1.9
  elif county == "DuPage":
    total = value*1.8
  elif county == "McHenry":
    total = value*1.75
  elif county == "Kane":
    total = value*1.6
  else:
    total = value*1.7

  # output
  print("Total value for home is: $",total)
  choice = input("Run the Program again? (Y/N): ")



