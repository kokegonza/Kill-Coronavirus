import mysql.connector
class Anamnesis:
    def __init__(self, id_anamnesis, paciente_id, medico_id, fecha, descripcion):
        self.__id_anamnesis = id_anamnesis
        self.__paciente_id = paciente_id
        self.__medico_id = medico_id
        self.__fecha = fecha
        self.__descripcion = descripcion

    def id_anamnesis(self):
        return self.__id_anamnesis

    def paciente_id(self):
        return self.__paciente_id

    def medico_id(self):
        return self.__medico_id

    def fecha(self):
        return self.__fecha

    def descripcion(self):
        return self.__descripcion
    
    















