# input
choice = input("Start the program? ")
data = 0


# process
while choice == "Yes":
  name = input("Input last name: ")
  hours = float(input("Input hours worked: "))
  rate = float(input("Input rate of pay: "))
  data = data+1
  if hours > 40:
    print("Overtime hours checked")
    OT = (hours-40)*rate*1.5
    gross = rate*40+OT
  else: gross = rate*hours
  print("Output for: ",name)
  print("Gross Pay is: ",gross)
  print("Data enteries: ",data)
  choice = input("Run again? ")

# output
print("Goodbye...")