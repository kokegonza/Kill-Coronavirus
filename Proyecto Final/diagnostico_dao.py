import mysql.connector
from conexion import Conexion
from diagnostico import Diagnostico

class DiagnosticoDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def insertar_diagnostico(self, diagnostico):
        try:
            consulta = """
                INSERT INTO diagnostico (id_diagnostico, paciente_id, fecha, descripcion)
                VALUES (%s, %s, %s, %s)
            """
            valores = (diagnostico.get_id_diagnostico(), diagnostico.get_paciente_id(), diagnostico.get_fecha(), diagnostico.get_descripcion())
            self.mysql.cursor.execute(consulta, valores)
            self.mysql.connection.commit()
            return "Diagnóstico insertado correctamente."
        except mysql.connector.Error as err:
            print(f"Error al insertar el diagnóstico: {err}")
            return None