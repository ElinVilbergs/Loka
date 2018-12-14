class Car:
    def __init__(self, plate, make):
        self.__plate = plate
        self.__make = make

    def __str__(self):
        return "{}, {}".format(self.__plate, self.__make)

    def __repr__(self):
        return self.__str__()

    def get_plate(self):
        return self.__plate
    
    def get_make(self):
        return self.__make