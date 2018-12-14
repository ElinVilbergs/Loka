from Services.CarService import CarService

class CarUI:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):
        
        action = ""

        while(action != "q"):

            print(" ")
            print("You can do the following:")
            print("1. Add a car")
            print("2. List all available cars")
            print("3. List all rented cars")
            print("Press 'q' to quit \n")

            action = input("Choose an option: ").lower()

            if action == "1":
                CarService.add_car_ui(action)

            elif action == "2":
                CarService.available_ui(action)

            elif action == "3":
                CarService.rented_ui(action)
