# Input

lastname = input("Input your last name: ")
game1 = float(input("Input your game 1 score: "))
game2 = float(input("Input your game 2 score: "))
game3 = float(input("Input your game 3 score: "))
handi = float(input("Input your handicap: "))


# processing

total = game1+game2+game3
avg = total/3
havg = (total+handi)/3
handicap = avg-havg

# output

print("Scores for ",lastname)
print("Total points earned: ",total)
print("Average points earned: ",avg)
print("Average points earned with handicap: ",havg)