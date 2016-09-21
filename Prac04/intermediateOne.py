#
cycles = 5
numbers = []
for i in range (cycles):
    number = input("Please enter a positive whole number")
    numbers.append(number)

firstNumber = numbers[0]
print("first number is {}".format(firstNumber))

lastNumber = numbers [4]
print("last number is {}".format(lastNumber))
test = 1000
for i in numbers:
    smallest = int(i)
    if smallest < test:
        test = smallest
print(test)

testOne = 1
for i in numbers:
    highest = int(i)
    if highest > testOne:
        testOne = highest
print(testOne)

total = 0
for i in numbers:
    total += int(i)
average = total / 5
print(average)
