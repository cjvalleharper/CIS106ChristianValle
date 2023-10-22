# input

name = (input("Enter Last Name: "))
hits = float(input("Enter number of Hits: "))
bat = float(input("Enter times at Bat: "))

# process
data = 0
avg = bat/hits
data = data+1

print("Batting Average for ",name," is: ",avg)
print("Players accounted for: ",data)

choice = input("Do you wish to run this program? (y/n): ")

while choice == "y":
  name = (input("Enter Last Name: "))
  hits = float(input("Enter number of Hits: "))
  bat = float(input("Enter times at Bat: "))
  avg = bat/hits
  data = data+1
  print("Batting Average for ",name," is: ",avg)
  print("Players accounted for: ",data)

  choice = input("Do you wish to run this program? (y/n): ")