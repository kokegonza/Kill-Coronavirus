class Medico():
    def __init__(self, id_medico, nombre, telefono, especialidad,email):
        self.__id_medico = id_medico
        self.__especialidad = especialidad
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
    
    def id_medico(self):
        return self.__id_medico
    
    def especialidad(self):
        return self.__especialidad

    def nombre(self):
        return self.__nombre

    def telefono(self):
        return self.__telefono
    
    def email(self):
        return self.__email