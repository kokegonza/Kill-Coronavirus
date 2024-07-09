class Especialidad:
    def __init__(self, id_especialidad, nombre):
        self.__id_especialidad = id_especialidad
        self.__nombre = nombre

    def id_especialidad(self):
        return self.__id_especialidad
    
    def nombre(self):
        return self.__nombre
