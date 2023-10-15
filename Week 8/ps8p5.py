f = open("ps8p5text.txt", "r")

# initialize counters and sums to 0
cost = 0

# get first data line
student = str(f.readline().rstrip('\n'))

while student != "":
  code = (f.readline())
  credits = float(f.readline())
  if code == "I":
    cost = cost+(credits * 250)
  else:
    cost = cost+(credits * 500)

  # display a line
  print("Student:", student, "Code:", code, "Credits: ",credits,"Cost: ",cost)

  # get next data line
  item = str(f.readline().rstrip('\n'))

# I know there is an error but I am unsure of how to fix it. The AI suggests a few things
# But I am unsure if I can use them/I don't fully understand it. However things do work.