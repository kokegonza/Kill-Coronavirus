import mysql.connector

from conexion import Conexion
from medicamento import Medicamento

class MedicamentoDao:
    def __init__(self):
        self.__mysql = Conexion()

    @property
    def mysql(self):
        return self.__mysql
    
    def insertar_medicamento(self, medicamento):
        try:
            sql = "INSERT INTO medicamento (id_medicamento, nombre, descripcion) VALUES (%s, %s, %s)"
            values = (medicamento.id_medicamento(), medicamento.nombre(), medicamento.descripcion())

            cursor = self.__mysql.cursor  
            cursor.execute(sql, values)
            self.__mysql.connection.commit()

            print("Medicamento insertado correctamente.")
        except Exception as e:
            print(f"Error al insertar medicamento: {e}")

        finally:
            if cursor:
                cursor.close()

    def editar_medicamento(self, id_medicamento):
        try:
            cursor = self.__mysql.cursor

            # Seleccionar datos actuales del medicamento
            sql_select = "SELECT nombre, descripcion FROM medicamento WHERE id_medicamento = %s"
            cursor.execute(sql_select, (id_medicamento,))
            medicamento_data = cursor.fetchone()

            if not medicamento_data:
                print(f"No se encontró ningún medicamento con id_medicamento {id_medicamento}.")
                return

            # Mostrar datos actuales y solicitar nuevos datos
            print("Datos actuales del medicamento:")
            print(f"Nombre: {medicamento_data[0]}")
            print(f"Descripción: {medicamento_data[1]}")

            nombre = input("Nuevo nombre (dejar en blanco para mantener el actual): ").strip() or medicamento_data[0]
            descripcion = input("Nueva descripción (dejar en blanco para mantener la actual): ").strip() or medicamento_data[1]

            # Crear objeto Medicamento con los nuevos datos
            medicamento = Medicamento(id_medicamento, nombre, descripcion)

            # Actualizar los datos en la base de datos
            sql_update = "UPDATE medicamento SET nombre = %s, descripcion = %s WHERE id_medicamento = %s"
            values = (medicamento.nombre(), medicamento.descripcion(), id_medicamento)

            cursor.execute(sql_update, values)
            self.__mysql.connection.commit()

            print(f"Medicamento con ID {id_medicamento} actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar medicamento en la base de datos: {err}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_medicamento(self, id_medicamento):
        try:
            cursor = self.__mysql.cursor

            
            sql_select = "SELECT * FROM medicamento WHERE id_medicamento = %s"
            cursor.execute(sql_select, (id_medicamento,))
            medicamento_data = cursor.fetchone()

            if not medicamento_data:
                print(f"No se encontró ningún medicamento con id_medicamento {id_medicamento}.")
                return

            
            sql_delete_prescripciones = "DELETE FROM prescripcion WHERE medicamento_id = %s"
            cursor.execute(sql_delete_prescripciones, (id_medicamento,))
            self.__mysql.connection.commit()

           
            sql_delete_medicamento = "DELETE FROM medicamento WHERE id_medicamento = %s"
            cursor.execute(sql_delete_medicamento, (id_medicamento,))
            self.__mysql.connection.commit()

            print(f"Medicamento con ID {id_medicamento} eliminado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar medicamento en la base de datos: {err}")
        finally:
            if cursor:
                cursor.close()