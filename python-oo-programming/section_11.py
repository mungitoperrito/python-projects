# Polymorphism

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def start(self):
        print(f'{self.__class__.__name__}: is starting' )


    def stop(self):
        print(f'{self.__class__.__name__}: is stopping' )

class Car(Vehicle):
    def __init__(self, brand, model, year, wheels, doors):
        super().__init__(brand, model, year)
        self.wheels = wheels
        self.doors = doors

    def stop(self):
        print(f'{self.__class__.__name__}: Method overide' )


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels

    def start(self):
        print(f'{self.__class__.__name__}: Method overide' )


############
### MAIN ###
############

if __name__ == '__main__':

    # # Uncomment to test
    # car_01 = Car('Brand_C', 'Model_C', 2020, 3, 4)
    # print(car_01.__dict__)
    # car_01.start()

    # # Uncomment to test
    # bike_01 = Motorcycle('Brand_M', 'Model_M', 2010, 2)
    # print(bike_01.__dict__)
    # bike_01.start()

    # Uncomment to test
    vehicles = [
        Car('BrandCC', 'ModelCC', 2018, 4, 4),
        Motorcycle('BrandMM', 'ModelMM', 2021, 2)
    ]
    for v in vehicles:
        print(v.__dict__)
        v.start()
        v.stop()
