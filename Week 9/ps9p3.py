# input

city = (input("Enter destination: "))
miles = float(input("Enter Miles travelled: "))
gal = float(input("Enter Gallons used: "))

# process
data = 0
mpg = miles/gal
data = data+1

print("Destination: ", city, "Miles: ", miles, "MPG: ",mpg)
print("Trips tracked: ",data)

choice = input("Do you wish to run this program? (y/n): ")

while choice == "y":
  city = (input("Enter destination: "))
  miles = float(input("Enter Miles travelled: "))
  gal = float(input("Enter Gallons used: "))
  mpg = miles/gal
  data = data+1

  print("Destination: ", city, "Miles: ", miles, "MPG: ",mpg)
  print("Trips tracked: ",data)

  choice = input("Do you wish to run this program? (y/n): ")
