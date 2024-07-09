import mysql.connector
from conexion import Conexion
from especialidad import Especialidad

class EspecialidadDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql
    
    def insertar_especialidad(self, especialidad):
        try:
            sql = "INSERT INTO especialidad (id_especialidad, nombre) VALUES (%s, %s)"
            values = (especialidad.id_especialidad(), especialidad.nombre())

            cursor = self.__mysql.cursor
            cursor.execute(sql, values)
            self.__mysql.connection.commit()

            print("Especialidad insertada correctamente.")
        except Exception as e:
            print(f"Error al insertar especialidad: {e}")

        finally:
            if cursor:
                cursor.close()

    def editar_especialidad(self, id_especialidad):
        try:
            cursor = self.__mysql.cursor

            
            sql_select = "SELECT nombre FROM especialidad WHERE id_especialidad = %s"
            cursor.execute(sql_select, (id_especialidad,))
            especialidad_data = cursor.fetchone()

            if not especialidad_data:
                print(f"No se encontró ninguna especialidad con id_especialidad {id_especialidad}.")
                return

            
            print("Datos actuales de la especialidad:")
            print(f"Nombre: {especialidad_data[0]}")

            
            nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener el actual): ").strip() or especialidad_data[0]

            
            especialidad = Especialidad(id_especialidad, nuevo_nombre)

            
            sql_update = "UPDATE especialidad SET nombre = %s WHERE id_especialidad = %s"
            values = (especialidad.nombre(), id_especialidad)

            cursor.execute(sql_update, values)
            self.__mysql.connection.commit()

            print(f"Especialidad con ID {id_especialidad} actualizada correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar especialidad en la base de datos: {err}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_especialidad(self, id_especialidad):
        try:
            sql = "DELETE FROM especialidad WHERE id_especialidad = %s"
            self.mysql.cursor.execute(sql, (id_especialidad,))
            self.mysql.connection.commit()
            print(f"Especialidad con ID {id_especialidad} eliminada correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar la especialidad con ID {id_especialidad}: {err}")