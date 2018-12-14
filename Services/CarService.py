from Repositories.CarRepository import CarRepository
from Models.Car import Car

import csv

class CarService:
    def __init__(self):
        self.__Car_repo = CarRepository()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__Car_repo.add_car(car)
    
    def is_valid_car(self, car):
        return True

    def get_cars(self):
        return self.__Car_repo.get_cars()

    def get_car_by_make(self, make):
        pass

    ########### VIÐBÆTUR ###########

    def add_car_ui(self):
        plate = input("Input plate number: ")
        while len(plate) != 6:
            print("Plate number is incorrect!")
            plate = input("Input plate number: ")
        make = input("Input make of car: ")
        new_car = Car(plate, make)
        CarRepository.add_car(self, new_car)

    def available_ui(self):
        CarRepository.get_cars(self)

    def rented_ui(self):
        CarRepository.rented(self)