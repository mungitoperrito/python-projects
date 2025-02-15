# Polymorphism

class Car:
    def __init__(self, brand, model, year, doors, wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.doors = doors
        self.wheels = wheels


    def start(self):
        print(f'{self.__class__.__name__}: is starting' )


    def stop(self):
        print(f'{self.__class__.__name__}: is stopping' )


class Motorcycle:
    def __init__(self, brand, model, year, wheels):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f'{self.__class__.__name__}: is starting' )


    def stop(self):
        print(f'{self.__class__.__name__}: is stopping' )


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
