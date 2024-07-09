class Usuario:
    def __init__(self, rut, password, rol):
        self.__rut = rut
        self.__password = password
        self.__rol = rol 
        
    def rut(self):
        return self.__rut

    def rol(self):
        return self.__rol

    def password(self):
        return self.__password