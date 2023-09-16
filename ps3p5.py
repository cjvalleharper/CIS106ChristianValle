# input
fixedcosts = float(input("Input Fixed Costs "))
ppu = float(input("Input Price per unit "))
cpu = float(input("Input Cost per unit "))

# processing
breakeven = (ppu-cpu)/fixedcosts

# output
print("Break even point is $",breakeven)