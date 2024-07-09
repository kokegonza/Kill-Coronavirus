from conexion import Conexion
from ficha_medica import FichaMedica
from beautifultable import BeautifulTable
from conexion import Conexion
from medico import Medico
from paciente import Paciente
from ficha_medica import FichaMedica

class FichaMedicaDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql

    def ver_fichas_medicas(self):
        try:
            self.mysql.cursor.execute("SELECT * FROM fichamedica")
            fichas = []
            for (id_fichamedica, paciente_id, fecha, anamnesis, diagnostico) in self.mysql.cursor:
                ficha = FichaMedica(id_fichamedica, paciente_id, fecha, diagnostico, anamnesis)
                fichas.append(ficha)
            return fichas
        except Exception as e:
            print(f"Error al obtener las fichas médicas: {e}")
            return None

    def insertar_ficha_medica(self, ficha_medica):
        try:
            consulta = "INSERT INTO fichamedica (paciente_id, fecha, anamnesis, diagnostico) VALUES (%s, %s, %s, %s)"
            valores = (ficha_medica.paciente_id(), ficha_medica.fecha(), ficha_medica.anamnesis(), ficha_medica.diagnostico())
            self.mysql.cursor.execute(consulta, valores)
            self.mysql.connection.commit()
            return "Ficha médica agregada exitosamente."
        except Exception as e:
            print(f"Error al insertar la ficha médica: {e}")
            return None

    def ver_pacientes_atendidos(self, medico_id):
        try:
            consulta = """
                SELECT p.nombre, fm.fecha, fm.diagnostico
                FROM fichamedica fm
                INNER JOIN paciente p ON fm.paciente_id = p.id_paciente
                INNER JOIN medicoPaciente mp ON fm.paciente_id = mp.paciente_id
                WHERE mp.medico_id = %s
            """
            self.mysql.cursor.execute(consulta, (medico_id,))
            resultados = self.mysql.cursor.fetchall()
            pacientes = [{"nombre": r[0], "fecha_atencion": r[1], "diagnostico": r[2]} for r in resultados]
            return pacientes
        except Exception as e:
            print(f"Error al obtener los pacientes atendidos: {e}")
            return None
        
    def listar_fichas_medicas(self):
        try:
            query = (
                "SELECT medico.nombre AS nombre_medico, medico.especialidad, "
                "paciente.nombre AS nombre_paciente, fichamedica.id_fichamedica, "
                "fichamedica.fecha, fichamedica.diagnostico, fichamedica.anamnesis "
                "FROM fichamedica "
                "INNER JOIN medico ON fichamedica.paciente_id = medico.id_medico "
                "INNER JOIN paciente ON fichamedica.paciente_id = paciente.id_paciente"
            )

            cursor = self.mysql.cursor
            cursor.execute(query)
            records = cursor.fetchall()

            if records:
                table = BeautifulTable()
                table.column_headers = ["ID Ficha Médica", "Fecha", "Médico", "Especialidad", "Paciente", "Diagnóstico", "Anamnesis"]

                for record in records:
                    table.append_row([
                        record[3],  
                        record[4],  
                        record[0],  
                        record[1],  
                        record[2],  
                        record[5],  
                        record[6]   
                    ])

                print(table)
            else:
                print("No se encontraron fichas médicas.")

        except Exception as e:
            print(f"Error al listar fichas médicas: {e}")

        finally:
            cursor.close()
            self.mysql.connection.close()

