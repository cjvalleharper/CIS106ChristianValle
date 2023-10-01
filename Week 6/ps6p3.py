# input
principle = float(input("Input Principle: "))



# process
if principle > 100000:
  years = float(input("Input Years until maturity: "))
  if years == 5:
    interest = .06
  else: interest = .02
elif principle >= 50000:
  years = float(input("Input Years until maturity: "))
  if years == 10: 
    interest = .05
  elif years == 5:
    interest = .04
  else: interest = .02
else: interest = .02

total = principle*interest

# output
print("Interest is: ",interest)
print("Total after one year is: $",total)