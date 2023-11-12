# Input

lastname = input("Input your last name: ")
exam1 = float(input("Input your exam 1 grade: "))
exam2 = float(input("Input your exam 2 grade: "))
exam3 = float(input("Input your exam 3 grade: "))


# processing

total = exam1+exam2+exam3
avg = total/3


# output

print("Scores for ",lastname)
print("Total points earned: ",total)
print("Average points earned: ",avg)