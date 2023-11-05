# input

choice = input("Run the Program? (Y/N): ")


# process
while choice == "Y":
  name = input("Enter last name: ")
  month = input("Enter Month to calculate: ")
  sales = float(input("Enter sales: "))

  if month == "January" or month == "February" or month == "March":
    prediction = sales+(sales*.1)
  elif month == "April" or month == "May" or month == "June":
    prediction = sales+(sales*.15)
  elif month == "July" or month == "August" or month == "September":
    prediction = sales+(sales*.2)
  else:
    prediction = sales+(sales*.25)

  # output
  print("Prediction for next month's sales forcast is: $",prediction)
  choice = input("Run the Program again? (Y/N): ")



