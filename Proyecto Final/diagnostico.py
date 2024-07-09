class Diagnostico:
    def __init__(self, id_diagnostico, paciente_id, fecha, descripcion):
        self.__id_diagnostico = id_diagnostico
        self.__paciente_id = paciente_id
        self.__fecha = fecha
        self.__descripcion = descripcion

    def get_id_diagnostico(self):
        return self.__id_diagnostico

    def get_paciente_id(self):
        return self.__paciente_id

    def get_fecha(self):
        return self.__fecha

    def get_descripcion(self):
        return self.__descripcion