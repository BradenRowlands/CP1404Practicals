items = (input("Please enter amount of items"))
while items < 1:
    print("Invalid amount")
    items = (input("Please enter amount of items"))
for i in items:
    (input("Please enter cost of items"))
    items = i + items
total = items
print("total price for" + items + "items is" + total)