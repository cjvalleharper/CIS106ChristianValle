# input   
p = float(input("Input Principle: "))
r = float(input("Input Rate: "))


# process
year = 0
total = 0
while year < 5:
  i = (p*r)
  end = p+i
  p = end
  total = total+i
  year = year+1
  print("Years:",year)
  print("Total Interest:",total)
  print("Ending Balance:",end)
  
# output