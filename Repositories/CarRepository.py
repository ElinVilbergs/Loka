from Models.Car import Car

import csv

class CarRepository:
    
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        # first add to file then to private list
        with open("./Data/availablecars.csv", "a+", encoding="utf-8", newline="") as cars_file:
            plate = car.get_plate()
            make = car.get_make()
            cars_file.write("{},{}\n".format(plate, make))
            
    def get_cars(self):
        with open("./Data/availablecars.csv", "r") as findcustomer:
            findcustomerreader = csv.DictReader(findcustomer)
            for line in findcustomerreader:
                print(line)

    def rented(self):
        with open("./Data/rentedcars.csv", "r") as findcustomer:
            findcustomerreader = csv.DictReader(findcustomer)
            for line in findcustomerreader:
                print(line)