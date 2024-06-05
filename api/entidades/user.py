class User:
    def __init__(self, name, email, password, is_admin, cod_depart, ):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin
        #self.__cod_depart = cod_depart

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin

    #@property
    #def cod_depart(self):
        #return self.cod_depart

    #@cod_depart.setter
    #def cod_depart(self, cod_depart):
        #self.__cod_depart = cod_depart