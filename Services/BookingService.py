from Repositories.BookingRepository import BookingRepository
from Models.NewBooking import NewBooking
import datetime
present = datetime.datetime.now()

class BookingService:
    def __init__(self):
        self.__booking_repo = BookingRepository()

    def add_booking(self, booking):
        if self.is_valid_booking(booking):
            self.__booking_repo.add_booking(booking)
    
    def is_valid_booking(self, booking):
        return True
    
    def get_booking(self):
        return self.__booking_repo.get_booking()

    #########################################################
    
    #Allows you to create a new booking
    def booking_menu_1(self):

        print("Customer needs to be registerd")
        ssn = input("Enter customer social security number: ")
        
        #Velja bílaflokk:
        car_category = input("Enter car category: 1,2 or 3: ")
        fullprice = NewBooking.select_category(self, car_category)

        #Taka frá bíl:
        plate_num = input("Enter car plate numer: ")
        BookingRepository.add_to_booking(self, plate_num)

        #Fá leigutíma:
        starte_date = input("Enter start date (D/M/YYYY): ")
        dte = datetime.datetime.strptime(starte_date, "%d/%m/%Y")
        if dte < present:
            print("Error date has passed")
            start_date = input("Enter start date (D/M/YYYY): ")
        start_date = starte_date  #starte_date = start_date
        dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
                            
        rent_length = int(input("Enter length of rental in days: "))
        tdelta = datetime.timedelta(days = rent_length)
        end_date = dt + tdelta
        pop = end_date.strftime("%d/%m/%Y")
        end_end_date = pop
        
        #Reikna út fullt verð:
        extra_ins = input("Extra insurance (1000/day)?    yes(y), no(n): ").lower()
        NewBooking.calc_fullprice(self, rent_length, fullprice, extra_ins)

        #Velja greiðsluleið:
        credit_card = input("Please enter the credit card number to confirm the booking: ")
        payment = input("Choose a payment method: 1. for credit card, 2. for debit card, 3. for cash: ")
        
        payment_method = ""
        if payment == "1":
            NewBooking.payment_credit_card(self, payment_method)
        elif payment == "2":
            NewBooking.payment_debit_card(self, payment_method)
        elif payment == "3":
            payment_method = "Cash"
            print("Payment successful\n")
        new_booking = NewBooking(ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method)
    
        BookingRepository.add_booking(self, new_booking)

    #Allows  you to edit previous booking
    def booking_menu_2(self):
        #Ná í bókunina/bílinn
        plate_num = input("Enter the plate number: ")
        BookingRepository.change_booking(self, plate_num)
        
        #Breyta upplýsingunum
        print("You can now change the booking information")
        
        print("Customer needs to be registerd")
        ssn = input("Enter customer social security number: ")
        
        #Velja nýjan bílaflokk
        car_category = input("Enter car category: 1,2 or 3: ")
        fullprice = NewBooking.select_category(self, car_category)
        
        #Taka frá nýjan bíl
        plate_num = input("Enter car plate number: ")
        BookingRepository.add_to_booking(self, plate_num)

        #Breyta leigutímanum
        start_date = input("Enter start date (D/M/YYYY): ")
        rent_length = int(input("Enter length of rental in days: "))
        dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        tdelta = datetime.timedelta(days = rent_length)
        end_date = dt + tdelta
        pop = end_date.strftime("%d/%m/%Y")
        end_end_date = pop

        #Reikna út nýtt verð:
        extra_ins = input("Extra insurance (1000/day)?    yes(y), no(n): ").lower()
        NewBooking.calc_fullprice(self, rent_length, fullprice, extra_ins)
        
        #Kreditkortaupplýsingar fyrir tryggingu:
        credit_card = input("Please enter the credit card number to confirm the booking: ")
        while len(credit_card) != 16:
            print("Error, try again")
            credit_card = input("Please enter the credit card number to confirm the booking: ")
        payment = input("Choose a payment method: 1. for credit card, 2. for debit card, 3. for cash: ")
        
        #Velja nýja greiðsluleið:
        payment = input("Choose a payment method: 1. for credit card, 2. for debit card, 3. for cash: ")
        
        payment_method = ""
        if payment == "1":
            NewBooking.payment_credit_card(self, payment_method)
        elif payment == "2":
            NewBooking.payment_debit_card(self, payment_method)
        elif payment == "3":
            payment_method = "Cash"
            print("Payment successful\n")
        new_booking = NewBooking(ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method)
    
        BookingRepository.add_booking(self, new_booking)

    #Allows you to look up a booking by typeing in the car plate number
    def booking_menu_3(self):
        BookingRepository.get_booking(self)
        
    #Allows you to remove a booking/unregister a booking
    def booking_menu_4(self):
        plate_num = input("Enter car plate number: ")
        BookingRepository.remove_booking(self, plate_num)
    
        print("Car has been returned\n")

