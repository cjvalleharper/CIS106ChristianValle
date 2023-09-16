# input
mealprice = float(input("Input Meal Price "))

# process
# For some reason, tip15value came back at 14.9 repeating, so I added a round.
tip15 = round(mealprice * 1.15)
tip15value = tip15 - mealprice
tip18 = mealprice * 1.18
tip18value = tip18 - mealprice
tip20 = mealprice * 1.2
tip20value = tip20 - mealprice

# output
# I put the "with X Tip" I hope that is okay.
print("15% Tip")
print("Total: $", mealprice)
print("Tip: $", tip15value)
print("Total with Tip: $", tip15)
print("")
print("18% Tip")
print("Total: $", mealprice)
print("Tip: $", tip18value)
print("Total with Tip: $", tip18)
print("")
print("20% Tip")
print("Total: $", mealprice)
print("Tip: $", tip20value)
print("Total with Tip: $", tip20)
