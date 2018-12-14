from Services.BookingService import BookingService


class BookingUI:

    def __init__(self):
        self.__booking_service = BookingService()

    def main_menu(self):

        action = ""
        while (action != "q"):
            print("You can do the following: ")
            print("1. Add booking")
            print("2. Change booking")
            print("3. Look up booking")
            print("4. Return rental")
            print("press q to quit")

            action = input("Choose an option: ").lower()
            print("\n")
        
            if action == "1":
                BookingService.booking_menu_1(action)   
                
            elif action == "2":
                BookingService.booking_menu_2(action)
                
            elif action == "3":
                BookingService.booking_menu_3(action)
                
            elif action == "4":
                BookingService.booking_menu_4(action)
                
            
