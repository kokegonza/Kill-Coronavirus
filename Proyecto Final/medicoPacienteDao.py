from conexion import Conexion
from beautifultable import BeautifulTable
class MedicoPacienteDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql
    def listar_medicopacientes_id(self, id_medico):
        try:
            query = (
                "SELECT mp.id_medicoPaciente, p.nombre AS nombre_paciente, "
                "m.nombre AS nombre_medico "
                "FROM medicopaciente mp "
                "INNER JOIN paciente p ON mp.paciente_id = p.id_paciente "
                "INNER JOIN medico m ON mp.medico_id = m.id_medico "
                "WHERE mp.medico_id = %s"
            )

            cursor = self.mysql.cursor
            cursor.execute(query, (id_medico,))
            records = cursor.fetchall()

            if records:
                table = BeautifulTable()
                table.column_headers = ["ID de registro", "Nombre Paciente", "Nombre Medico que lo atendio"]

                for record in records:
                    table.append_row([
                        record[0],  
                        record[1],  
                        record[2]   
                    ])

                print(table)
            else:
                print(f"No se encontraron registros en la tabla medicopaciente para el médico con ID {id_medico}.")

        except Exception as e:
            print(f"Error al listar medicopacientes: {e}")

        finally:
            cursor.close()
            self.mysql.connection.close()

    def listar_medicopacientes(self):
        try:
            query = (
                "SELECT mp.id_medicoPaciente, p.nombre AS nombre_paciente, "
                "m.nombre AS nombre_medico "
                "FROM medicopaciente mp "
                "INNER JOIN paciente p ON mp.paciente_id = p.id_paciente "
                "INNER JOIN medico m ON mp.medico_id = m.id_medico"
            )

            cursor = self.mysql.cursor
            cursor.execute(query)
            records = cursor.fetchall()

            if records:
                table = BeautifulTable()
                table.column_headers = ["ID MedicoPaciente", "Nombre Paciente", "Nombre Medico"]

                for record in records:
                    table.append_row([
                        record[0],  
                        record[1],  
                        record[2]   
                    ])

                print(table)
            else:
                print("No se encontraron registros en la tabla medicopaciente.")

        except Exception as e:
            print(f"Error al listar medicopacientes: {e}")

        finally:
            cursor.close()
            self.mysql.connection.close()