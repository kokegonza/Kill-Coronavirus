class Paciente:
    def __init__(self, id_paciente, nombre, rut, fecha_nacimiento, sexo, direccion, telefono):
        self.__id_paciente = id_paciente
        self.__nombre = nombre
        self.__rut = rut
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self.__direccion = direccion
        self.__telefono = telefono

    def id_paciente(self):
        return self.__id_paciente

    def nombre(self):
        return self.__nombre

    def rut(self):
        return self.__rut

    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def sexo(self):
        return self.__sexo

    def direccion(self):
        return self.__direccion

    def telefono(self):
        return self.__telefono

    def mostrar_paciente(self):
        print("Paciente: " + str(self.__id_paciente) + " " + self.__nombre)
        print("Fecha de nacimiento: " + str(self.__fecha_nacimiento))
        print("Sexo: " + self.__sexo)
        print("Dirección: " + self.__direccion)
        print("Teléfono: " + self.__telefono)


