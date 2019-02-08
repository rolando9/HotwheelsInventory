class Car:
    """A simple attempt to represent a car in my 1/64th scale car inventory"""
    def __init__(self, year, make, model, layout, v_class, color):
        """Initialize attributes to describe a car in the inventory"""
        self.year = year
        self.make = make
        self.model = model
        self.layout = layout
        self.v_class = v_class
        self.color = color

    def get_info(self):
        print('What is the year of the vehicle?')

    def car_description(self):
        """Return a short description of the car for the user."""
        print("Car specifications:"
              "\n"
              "\nYear:   " + self.year +
              "\nMake:   " + self.make.title() +
              "\nModel:  " + self.model.title() +
              "\nLayout: " + self.layout.upper() +
              "\nClass:  " + self.v_class.title() +
              "\nColor:  " + self.color.title())

get_info
ferrari = Car(str(1995), 'ferrari', 'f512m', 'rme, rwd', 'S', 'silver')
print(ferrari.car_description())
