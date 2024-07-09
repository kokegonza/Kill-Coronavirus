import mysql.connector
from conexion import Conexion
from anamnesis import Anamnesis
class AnamnesisDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def insertar_anamnesis(self, anamnesis):
        try:
            consulta = """
                INSERT INTO anamnesis (paciente_id, medico_id, fecha, descripcion)
                VALUES (%s, %s, %s, %s)
            """
            valores = (anamnesis.paciente_id(), anamnesis.medico_id(), anamnesis.fecha(), anamnesis.descripcion())
            self.mysql.cursor.execute(consulta, valores)
            self.mysql.connection.commit()
            return "Anamnesis agregada exitosamente."
        except mysql.connector.Error as err:
            print(f"Error al insertar la anamnesis: {err}")
            return None
