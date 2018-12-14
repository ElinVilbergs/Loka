from Repositories.CustomerRepository import CustomerRepository
from Models.Registration import Registration

import csv
import os

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)
    
    def is_valid_customer(self, customer):
        return True

    def get_customer(self):
        return self.__customer_repo.get_customer()

##################### VIÐBÆTUR ######################################

    def ui_menu_1(self):

        name = input("Name: ")
        mail = input("Email: ")
        ssn = input("Social security number: ")
        while len(ssn) != 10:
            print("Invalid SSN")
            ssn = input("Social security number: ")
        phone = input("Phone number: ")
        new_customer = Registration(name, mail, ssn, phone)
        CustomerRepository.add_customer(self, new_customer)
        print("Customer has been added")


    def ui_menu_2(self):

        CustomerRepository.find_customer(self)
        print("")
        return

    def ui_menu_3(self):

        CustomerRepository.edit_customer(self)              #Opnar skránna í repoinu og replace-ar upplýsingarnar
        print("You can now change the customers information")
        name = input("Name: ")
        mail = input("Email: ")
        ssn = input("Social security number: ")
        if len(ssn) != 10:
            print("Invalid SSN")
            ssn = input("Social security number: ")
        phone = input("Phone number: ")
        new_customer = Registration(name, mail, ssn, phone)
        CustomerRepository.add_customer(self, new_customer)
        print("Customer has been edited")

    def ui_menu_4(self):
        #Unregister a customer
        ssn = input("Enter the Social security number: ")

        CustomerRepository.unregister_customer(self, ssn)
