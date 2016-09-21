#
HEXIDECIMAL_COLOURS = {"BLACK": "000000", "BLUE": "0000ff", "BROWN": "a52a2a", "CADETBLUE": "5f9ea0",
                       "CHARTREUSE": "7fff00", "CORAL": "ff7526"
    , "CHOCOLATE": "d2691e", "DARKGREEN": "006400", "DARKORANGE": "ff8c00", "DARKKHAKI": "bdb76b"}

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in HEXIDECIMAL_COLOURS:
        print(colour, "is", HEXIDECIMAL_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()