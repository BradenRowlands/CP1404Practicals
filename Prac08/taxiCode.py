import random


class Car:
     """ represent a car object """

     def __init__(self, name="", fuel=0):
         """ initialise a Car instance """
         self.name = name
         self.fuel = fuel
         self.odometer = 0

     def __str__(self):
         return "{:10}, fuel={:3}, odo={:5}".format(self.name, self.fuel, self.odometer)

     def add_fuel(self, amount):
         """ add amount to the car's fuel"""
         self.fuel += amount

     def drive(self, distance):
         """ drive the car a given distance if it has enough fuel or drive until fuel runs out
         return the distance actually driven """
         if distance > self.fuel:
             distance_driven = self.fuel
             self.fuel = 0
         else:
             self.fuel -= distance
             distance_driven = distance
         self.odometer += distance_driven
         return distance_driven


class Taxi(Car):
     """ specialised version of a Car that includes fare costs """

     price_per_km = 1.20

     def __init__(self, name="", fuel=0):
         """ initialise a Taxi instance, based on parent class Car """
         super().__init__(name, fuel)
         self.current_fare_distance = 0
         self.style = 1

     def __str__(self):
         """ return a string representation like a car but with current fare distance"""
         return "{}, {:4}km on current fare, ${:5.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                                 self.price_per_km * self.style)

     def get_fare(self):
         """ get the price for the taxi trip """
         return self.price_per_km * self.current_fare_distance

     def start_fare(self):
         """ begin a new fare """
         self.current_fare_distance = 0

     def drive(self, distance):
         """ drive like parent Car but calculate fare distance as well"""
         distance_driven = super().drive(distance)
         self.current_fare_distance += distance_driven
         return distance_driven * self.price_per_km

     def name(self):
         """ return the name """
         return self.name


class SilverServiceTaxi(Taxi):
     cab_decision = 4.50

     def __init__(self, name="", fuel=0, style=3, ):
         super().__init__(name, fuel)
         self.name = name
         self.fuel = fuel
         self.style = style
         self.odometer = 0

     def __str__(self):
         return "{} plus flagfall of {}".format(super().__str__(), self.cab_decision)

     def get_fare(self):
         return super().get_fare() * self.style + self.cab_decision

     def drive(self, distance):
         return (super().drive(distance) * self.style) + self.cab_decision


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=50):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def __str__(self):
        return "{}, reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if random.uniform(1, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
