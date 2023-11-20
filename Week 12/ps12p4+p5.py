names = []
scores = []

with open('list.txt', 'r') as f:
  for index, line in enumerate(f):
    stripped_line = line.strip('\n\r')
    if index % 2 == 0:
        names.append(stripped_line)
    else:
        scores.append(float(stripped_line))



response = 'y'
while response.lower() == 'y':
    response = input("Do you want to search for a last name? (y/n) ")

    if response.lower() == 'n':
        break

    search = input("Enter a last name: ")

    if not search in names:
        print(search, "is not a real person :(")
        continue

    name_index = names.index(search)
    print(f"{search} has a score of {scores[name_index]}")

