import random
thelist = []
amountOfPicks = input("Please enter the amount of picks you would like")
for i in range (int(amountOfPicks)):
    for number in range(6):
        number = random.randint(1,45)
        thelist.append(number)
    print(thelist)
    thelist = []