import mysql.connector

class Medicamento:
    def __init__(self, id_medicamento, nombre, descripcion):
        self.__id_medicamento = id_medicamento
        self.__nombre = nombre
        self.__descripcion = descripcion

    def id_medicamento(self):
        return self.__id_medicamento
    def nombre(self):
        return self.__nombre
    def descripcion(self):
        return self.__descripcion

    def guardar(self, conexion):
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO medicamento (nombre, descripcion)
        VALUES (%s, %s)
        """
        valores = (self.nombre, self.descripcion)
        try:
            cursor.execute(consulta, valores)
            self.id_medicamento = cursor.lastrowid  
            conexion.commit()
            print("Medicamento guardado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conexion.rollback()
        finally:
            cursor.close()

    @staticmethod
    def obtener_medicamento_por_id(conexion, id_medicamento):
        cursor = conexion.cursor()
        consulta = "SELECT id_medicamento, nombre, descripcion FROM medicamento WHERE id_medicamento = %s"
        cursor.execute(consulta, (id_medicamento,))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return Medicamento(*resultado)
        else:
            return None

    def actualizar(self, conexion):
        cursor = conexion.cursor()
        consulta = """
        UPDATE medicamento
        SET nombre = %s, descripcion = %s
        WHERE id_medicamento = %s
        """
        valores = (self.nombre, self.descripcion, self.id_medicamento)
        try:
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Medicamento actualizado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conexion.rollback()
        finally:
            cursor.close()

    def eliminar(self, conexion):
        cursor = conexion.cursor()
        consulta = "DELETE FROM medicamento WHERE id_medicamento = %s"
        try:
            cursor.execute(consulta, (self.id_medicamento,))
            conexion.commit()
            print("Medicamento eliminado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            conexion.rollback()
        finally:
            cursor.close()
