from conexion import Conexion
from paciente import Paciente
from beautifultable import BeautifulTable
import mysql.connector

class PacienteDao:
    def __init__(self):
        self.__mysql = Conexion()
    
    @property
    def mysql(self):
        return self.__mysql

    def mostrar_pacientes_disponibles(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id_paciente FROM paciente")
            pacientes = cursor.fetchall()
            return pacientes
        except mysql.connector.Error as error:
            print(f"Error al obtener pacientes disponibles: {error}")
            return None

    def id_paciente_disponible(self, id_paciente):
        try:
            cursor = self.conexion.cursor()
            consulta = "SELECT id_paciente FROM paciente WHERE id_paciente = %s"
            cursor.execute(consulta, (id_paciente,))
            paciente = cursor.fetchone()
            return paciente is None
        except mysql.connector.Error as error:
            print(f"Error al verificar disponibilidad del ID de paciente: {error}")
            return False

    def eliminar_paciente(self, rut):
        try:
            if self.buscar_paciente(rut) is not None:
                consulta = "DELETE FROM paciente WHERE rut = %s"
                self.conexion.cursor().execute(consulta, (rut,))
                self.conexion.connection.commit()
                return 'Paciente eliminado correctamente!'
            else:
                return 'Paciente con RUT no existe!'
        except Exception as e:
            print(f"Error al eliminar el paciente: {e}")
            return None

    def actualizar_paciente(self, rut, nuevo_nombre, nueva_fecha_nacimiento, nuevo_sexo, nueva_direccion, nuevo_telefono):
        try:
            if self.buscar_paciente(rut) is not None:
                consulta = "UPDATE paciente SET nombre = %s, fecha_nacimiento = %s, sexo = %s, direccion = %s, telefono = %s WHERE rut = %s"
                valores = (nuevo_nombre, nueva_fecha_nacimiento, nuevo_sexo, nueva_direccion, nuevo_telefono, rut)
                self.conexion.cursor().execute(consulta, valores)
                self.conexion.connection.commit()
                return 'Paciente actualizado correctamente!'
            else:
                return 'Paciente con RUT no existe!'
        except Exception as e:
            print(f"Error al actualizar el paciente: {e}")
            return None

    def buscar_paciente(self, rut):
        try:
            consulta = "SELECT * FROM paciente WHERE rut = %s"
            self.conexion.cursor().execute(consulta, (rut,))
            resultado = self.conexion.cursor().fetchone()
            if resultado:
                return Paciente(*resultado)
            else:
                return None
        except Exception as e:
            print(f"Error al buscar el paciente: {e}")
            return None
        
    def buscar_por_rut(self, rut):
        try:
            query = "SELECT * FROM Paciente WHERE rut = %s"
            self.mysql.cursor.execute(query, (rut,))
            paciente_data = self.mysql.cursor.fetchone()

            if paciente_data:
                
                paciente_data = list(paciente_data)  
                fecha_nacimiento = paciente_data[3]  
                paciente_data[3] = fecha_nacimiento.strftime("%Y-%m-%d")  

                table = BeautifulTable()
                table.column_headers = ["ID Paciente", "Nombre", "RUT", "Fecha Nacimiento", "Sexo", "Dirección", "Teléfono"]
                table.append_row(paciente_data)
                print(table)
            else:
                print(f"No se encontró ningún paciente con RUT {rut}")

        except mysql.connector.Error as error:
            print(f"Error al buscar paciente por RUT: {error}")

        finally:
            self.mysql.connection.close()
    
