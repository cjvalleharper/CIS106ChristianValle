# Howdy, quick thing I wanted to add!
# I didn't know if we were meant to do Problem 1 and 2 as one file (Since 2 builds off 1)
# I kept them together, I hope that is okay!


def displayLarrays(lname):
  for i in range(0, 10):
    print(lname[i])


def rLdisplay(lname):
  for i in range(9, -1, -1):
    print(lname[i])

  print(lname)
  lname.reverse()
  print(lname)


def displaySarrays(score):
  for i in range(0, 10):
    print(score[i])


def rSdisplay(score):
  for i in range(9, -1, -1):
    print(score[i])

  #print(score)
  #score.reverse()
  #print(score)


lname = [
    "Adams", "Baker", "Smith", "Davis", "Jones", "Johnson", "Miller", "Davis",
    "Scott", "Logan"
]
score = ["92", "22", "30", "17", "19", "51", "89", "80", "7", "25"]

displayLarrays(lname)
displaySarrays(score)
print("[Reverse Order]")
rLdisplay(lname)
rSdisplay(score)
