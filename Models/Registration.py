class Registration:

    def __init__(self, name, mail, ssn, phone):
        self.__name = name
        self.__mail = mail
        self.__ssn = ssn
        self.__phone = phone
    
    def __str__(self):
        return "{},{},{},{}".format(self.__name, self.__mail, self.__ssn, self.__phone)

    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.__name
    
    def get_mail(self):
        return self.__mail
    
    def get_ssn(self):
        return self.__ssn

    def get_phone(self):
        return self.__phone