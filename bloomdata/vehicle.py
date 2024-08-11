# This file holds two classes: Vehicle and Convertible
# They are a parent and a child class

# Imagine I want to list these vehicles on Craigslist
# the "Parent" class is the more generic class of the two

class Vehicle:
    """Parent class representing a Vehicle"""

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        """Function returning honk"""
        return "Hooooonk"

    def drive(self, miles_driven):
        """Function returning mileage after miles_driven"""
        self.mileage = self.mileage - miles_driven
        return self.mileage

    def __repr__(self):
        return f"A {self.color} {self.year} {self.model} with {self.mileage} miles."

if __name__ == '__main__':
    my_vehicle = Vehicle('Toyota', 'Camry', 'grey', 2015, 60000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print(my_vehicle)


# Imagine I want to list these vehicles on Craigslist
# the "Child" class is more specific
# The Convertible class inherits from the Vehicle (Parent)class

class Convertible(Vehicle):
    """Child class representing convertible vehicles from 
    Parent class vehicles"""


    def __init__(self, make, model, color, year, mileage, top_down=True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down


    def change_top_status(self):
        """Function to returning if the convertible top is down"""
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True
            return "Top is now down!"


    def __repr__(self):
        return f"A {self.color} {self.year} {self.model} with {self.mileage} miles."

if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'grey', 2015, 60000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    # print(my_vehicle.honk())
    # print(my_vehicle.drive(1234))
    # print(my_vehicle.mileage)

    print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())
    print(my_vehicle.top_down)
    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    # End of file (EOF)
    