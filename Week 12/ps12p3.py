
def displayarrays(lname, score):
  hivar = float()
  lovar = float(999999)
  for i in range(0, 10, 1):
    print(lname[i], "has a score of",score[i])


  for y in range (0,10,1):
    if float(score[y]) > float(hivar):
      hivar = max(hivar, score[y])
    
      

    if float(score[y]) < float(lovar):
      lovar = min(lovar, score[y])
      

  print("High Score: ",hivar)
  print("Low Score: ",lovar)



lname = ["Adams", "Baker", "Smith", "Davis", "Jones","Johnson","Miller","Davis","Scott","Logan"]
score = [92,22,30,17,19,51,89,80,7,25]

displayarrays(lname, score)
