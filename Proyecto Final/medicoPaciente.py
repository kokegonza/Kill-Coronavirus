class MedicoPaciente():
    def __init__(self, id_medicoPaciente, paciente_id, medico_id):
        self.__id_medicoPaciente = id_medicoPaciente
        self.__paciente_id = paciente_id
        self.__medico_id = medico_id
    

    def id_medicoPaciente(self):
        return self.__id_medicoPaciente
    def paciente_id(self):
        return self.__paciente_id
    def medico_id(self):
        return self.__medico_id