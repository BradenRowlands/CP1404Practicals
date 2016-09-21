userInputer = input("Please enter a string")
finalString = userInputer.split()
userString = dict()
for value in finalString:
    if value in userString:
        userString[value] += 1
    else:
        userString [value] = int(1)

for i in userString:
    print("{:<5}  :  {:<5}".format(i, userString[i]))
