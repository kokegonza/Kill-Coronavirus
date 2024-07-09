import mysql.connector

class Prescripcion:
    def __init__(self, ficha_medica_id, medicamento_id, dosis, frecuencia, duracion):
        self.__ficha_medica_id = ficha_medica_id
        self.__medicamento_id = medicamento_id
        self.__dosis = dosis
        self.__frecuencia = frecuencia
        self.__duracion = duracion

    def guardar_prescripcion(self, cursor):
        try:
            
            cursor.execute("SELECT id_fichamedica FROM fichamedica WHERE id_fichamedica = %s", (self.__ficha_medica_id,))
            ficha_medica = cursor.fetchone()

            if ficha_medica:
                
                consulta = """
                    INSERT INTO prescripcion (ficha_medica_id, medicamento_id, dosis, frecuencia, duracion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                valores = (self.__ficha_medica_id, self.__medicamento_id, self.__dosis, self.__frecuencia, self.__duracion)
                cursor.execute(consulta, valores)
                print("Prescripción guardada exitosamente.")
            else:
                print(f"No se encontró la ficha médica con id {self.__ficha_medica_id}.")
        except mysql.connector.Error as error:
            print(f"Error al guardar la prescripción: {error}")

# Ejemplo de uso
conexion = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="bdd_kill"
)

# Crear un objeto de prescripción y guardarla
prescripcion = Prescripcion(ficha_medica_id=1, medicamento_id=1, dosis="10 mg", frecuencia="Cada 8 horas", duracion="7 días")
cursor = conexion.cursor()
prescripcion.guardar_prescripcion(cursor)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

