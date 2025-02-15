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
    def __init__(self, brand, model, year, doors, wheels):
        super().__init__(brand, model, year)
        self.doors = doors
        self.wheels = wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels


############
### MAIN ###
############

if __name__ == '__main__':

    # # Uncomment to test
    # vehicle_01 = Vehicle('Brand_A', 'Model_A', 1910)
    # vehicle_01.start()
    # vehicle_01.stop()

    # Uncomment to test
    car_01 = Car('Brand_B', 'Model_B', 2020, 3, 4)
    print(car_01.__dict__)
    car_01.start()
    car_01.stop()

    # Uncomment to test
    bike_01 = Bike('Brand_C', 'Model_C', 2010, 2)
    print(bike_01.__dict__)
    bike_01.start()
    bike_01.stop()

