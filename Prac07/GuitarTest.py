from Prac07.GuitaerClass import GuitarDetails

def main():
    guitars = []
    menu(guitars)

#    guitar_stock = [GuitarDetails("Wong", 1950, 155.09),
#                      GuitarDetails("Wing", 2000, 890.00),
#                      GuitarDetails("Wang", 1000, 100000)]

    for product in guitars:
        print(product)

def menu(guitars):
    quickBool = False
    while quickBool == False:
        guitar_name = input("Guitar Name: ")
        if guitar_name == "".strip():
            break
        guitar_year = input("Year Made: ")
        guitaer_price = input("Price: ")
        guitars.append(GuitarDetails(guitar_name, guitar_year, guitaer_price))
    return guitars

main()
