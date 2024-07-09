class FichaMedica:
    def __init__(self, id_fichamedica, paciente_id, fecha, diagnostico, anamnesis):
        self.__id_fichamedica = id_fichamedica
        self.__paciente_id = paciente_id
        self.__fecha = fecha
        self.__diagnostico = diagnostico
        self.__anamnesis = anamnesis

    def get_id_fichamedica(self):
        return self.__id_fichamedica
    
    def get_paciente_id(self):
        return self.__paciente_id

    def get_fecha(self):
        return self.__fecha
    
    def get_diagnostico(self):
        return self.__diagnostico
    
    def get_anamnesis(self):
        return self.__anamnesis

    def generar_ficha(self):
        print("FICHA MEDICA:")
        print(f"ID de Ficha: {self.__id_fichamedica}")
        print(f"Paciente ID: {self.__paciente_id}")
        print(f"Fecha: {self.__fecha}")
        print(f"Diagnóstico: {self.__diagnostico}")
        if self.__anamnesis:
            print(f"Anamnesis: {self.__anamnesis}")

    def __str__(self):
        return f"FichaMedica(ID: {self.__id_fichamedica}, Paciente ID: {self.__paciente_id}, Fecha: {self.__fecha}, Diagnóstico: {self.__diagnostico}, Anamnesis: {self.__anamnesis})"
