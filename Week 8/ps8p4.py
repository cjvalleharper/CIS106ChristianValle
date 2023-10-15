f = open("ps8p4text.txt", "r")

# initialize counters and sums to 0
c = 0.0
total_ex = 0.0

# get first data line
item = str(f.readline().rstrip('\n'))

while item !="":
  qty = float(f.readline())
  price = float(f.readline())
  ep = qty*price
  total_ex = total_ex+ep
  c = c+1
  
  # display a line
  print("Item:", item, "Qty:", qty, "Price:", price, "Extended Price:", ep)

  # get next data line
  item = str(f.readline().rstrip('\n'))

# after loop
# final calc
# display them and any sums and counts
print("Total Extended Price:", total_ex)
print("Count:", c)
print("Average Extended Price:", total_ex/c)