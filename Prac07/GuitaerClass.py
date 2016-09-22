class GuitarDetails:
    def __init__(self, guitar_name=" ", year_made=0, price=0):
        self.guitar_name = guitar_name
        self.year_made = year_made
        self.price = price

    def __str__(self):
        return print("Guitar {}: {} {}".format(self.guitar_name, self.year_made, self.price))

    def get_age(self):
        self.get_age = 2016 - self.year_made
        return self.get_age

    def is_vintage(self):
        if self.get_age >= 50:
            return True
        else:
            False