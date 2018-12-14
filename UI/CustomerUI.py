from Services.CustomerService import CustomerService


class CustomerUI:

    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):
        
        action = ""
        while(action != "q"):
        
            print("")
            print("You can do the following: ")
            print("1. Add a customer")
            print("2. Look up customer")
            print("3. Edit customer")
            print("4. Unregister customer")
            print("press q to quit")
            print("")

            action = input("Choose an option: ").lower()

            

            if action == "1":
                CustomerService.ui_menu_1(action)   #útfært

            elif action == "2":
                CustomerService.ui_menu_2(action)   #í vinnslu
                

            elif action == "3":
                CustomerService.ui_menu_3(action)

            elif action == "4":
                CustomerService.ui_menu_4(action)