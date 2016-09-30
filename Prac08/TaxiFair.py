from Prac08.taxiCode import Taxi, SilverServiceTaxi


def main():
     menu = "Q)quit, C)Choose taxi, D)drive"
     user_input = ""
     total_bill = 0
     taxis = [Taxi("Prius", 100),
              SilverServiceTaxi("Limo", 100, 2),
              SilverServiceTaxi("Hummer", 200, 4)]

     cab_decision = choose(taxis)

     while user_input != "q":
         user_input = menu(menu)
         if user_input == "c":
             cab_decision = choose(taxis)
         elif user_input == "d":
             total_bill = drive(taxis, cab_decision, total_bill)
         elif user_input != "q":
             print("Invalid option")
         print("Bill to date: ${}".format(total_bill))
         print()

     print("Total trip cost: {}".format(total_bill))
     print("Taxis are now:")
     for taxi in range(len(taxis)):
         print("{} - {}".format(taxi, taxis[taxi]))


def menu(menu_choices):
     print(menu_choices)
     menu_input = input().lower()
     return menu_input


def choose(taxis):
     taxi_choice = int(input("Choose taxi by it's number: "))
     if taxi_choice < 0 or taxi_choice > len(taxis):
         print("Invalid taxi number")
     print()
     return taxi_choice


def drive(taxies, taxi_choice, total_bill):
     distance = 0
     trip_cost = 0
     if distance < 0:
             distance = int(input("Drive how far? "))
             trip_cost = taxies[taxi_choice].drive(distance)
             if distance <= 0:
                 print("Invalid input, distance must be greater then 0")
     print("Your {} trip cost you ${}".format(taxies[taxi_choice].name, trip_cost))
     total_bill += trip_cost

     return total_bill

main()