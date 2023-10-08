# input
choice = input("Start the program? ")
data = 0

# process
while choice == "Yes":
  name = input("Input Last Name: ")
  exam1 = float(input("Input Score of Exam 1: "))
  exam2 = float(input("Input Score of Exam 2: "))
  data = +1
  average = (exam1 + exam2) / 2
  print("Data enteries: ", data)
  print("Average for Exam 1 and Exam 2 is: ", average)
  choice = input(print("Try again? "))

print("Goodbye")
# output
