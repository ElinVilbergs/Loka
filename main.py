from UI.CarUI import CarUI
from UI.CustomerUI import CustomerUI
from UI.BookingUI import BookingUI


def main():
    print("Welcome to group 27 assignment please do one of the following actions:\n")
    while(True):
        print("Pick 1 for Cars")
        print("Pick 2 for Customers")
        print("Pick 3 for Booking")
        print("Pick q to quit")
        
        choice = input("Enter option: ")
        if choice == "1":
            ui = CarUI()
            ui.main_menu()
            print("Main Menu")
        elif choice == "2":
            ui = CustomerUI()
            ui.main_menu()
            print("Main Menu")
        elif choice == "3":
            ui = BookingUI()
            ui.main_menu()
            print("Main Menu")
        elif choice == "q":
            print("\nThank you for using out system, goodbye!")
            break
        else:
            print("\nInvalid input, try again!\n")
main()
