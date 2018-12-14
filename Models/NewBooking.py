import datetime
present = datetime.datetime.now()

class NewBooking:
    def __init__(self, ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method):
        self.__ssn = ssn
        self.__car_category = car_category
        self.__plate_num = plate_num
        self.__start_date = start_date
        self.__credit_card = credit_card
        self.__end_end_date = end_end_date
        self.__extra_ins = extra_ins
        self.__payment_method = payment_method

# ssn = kennitala, card_info = kortaupplýsingar, car_category = flokkur bíls,
# extend_rent = lengd leigu, extra_ins = auka trygging

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__ssn, self.__car_category, self.__plate_num, self.__start_date, self.__credit_card, self.__end_end_date, self.__extra_ins, self.__payment_method)

    def get_ssn(self):
        return self.__ssn

    def get_car_category(self):
        return self.__car_category

    def get_plate_num(self):
        return self.__plate_num

    def get_start_date(self):
        return self.__start_date

    def get_credit_card(self):
        return self.__credit_card

    def get_end_end_date(self):
        return self.__end_end_date

    def get_extra_ins(self):
        return self.__extra_ins

    def get_payment_method(self):
        return self.__payment_method

    def select_category(self, car_category):
        fullprice = 0
        balance = 0

        if car_category == "1":
            fullprice = balance + 12000
        elif car_category == "2":
            fullprice = balance + 23000
        elif car_category == "3":
            fullprice = balance + 50000
        else:
            print("Invalid input, please try again")
            #Setja svo loopu þannig ef það er valið vitlaust að hann reyni aftur
         
        return fullprice
        


    def calc_fullprice(self, rent_length, fullprice, extra_ins):
        fullprice = fullprice * rent_length
        
        if extra_ins == "y":
            fullfullprice = fullprice + (1000 * rent_length)
            print("The price of the rental is {} with insurance included".format(fullfullprice))
            print("Price without the insurance is: {}".format(fullprice))
            
        else:
            print("The price for the rental is: {}".format(fullprice))
            
        

        #Hafa extra_ins fyrir utan fallið og importa það í fallið

    def payment_credit_card(self, payment_method):
        cvv = 0
        payment_method = "Credit card"
        credit = input("Enter credit card number: ")
        while len(credit) != 16:
            print("Error, try again")
            credit = input("Enter credit card number: ")
        print(input("Enter cardholder name: "))
        print(input("Enter expiration date (M/Y): "))
        print(input("Enter CVV number: "))
        while len(cvv) != 3:
            print("Error, try again")
            cvv = input("Enter CVV number: ")
        print("Payment successful\n")

        return payment_method

    def payment_debit_card(self, payment_method):
        cvv = 0
        payment_method = "Debit card"
        debit = input("Enter debit card number: ")
        while len(debit) != 16:
            print("Error, try again")
            debit = input("Enter debit card number: ")
        print(input("Enter cardholder name: "))
        print(input("Enter expiration date (M/Y): "))
        print(input("Enter CVV number: "))
        while len(cvv) != 3:
            print("Error, try again")
            cvv = input("Enter CVV number: ")
        print("Payment successful\n")

        return payment_method