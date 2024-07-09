from beautifultable import BeautifulTable
import mysql.connector
from conexion import Conexion
from paciente_dao import PacienteDao
from ficha_medica_dao import FichaMedicaDao
from anamnesis_dao import AnamnesisDao
from paciente import Paciente
from ficha_medica import FichaMedica
from medico import Medico
from medico_dao import MedicoDao
from anamnesis import Anamnesis
from datetime import datetime
from diagnostico_dao import DiagnosticoDao
from medicamento_dao import MedicamentoDao
from medicamento import Medicamento
from especialidad_dao import EspecialidadDao
from especialidad import Especialidad
from medicoPacienteDao import MedicoPacienteDao
import time
import os
from diagnostico import Diagnostico

def mostrar_menu_principal():
    menu = BeautifulTable()
    menu.columns.header = ['============================ INICIO DE SESIÓN ============================']
    menu.rows.append(['1. Iniciar sesión como médico'])
    menu.rows.append(['2. Iniciar sesión como administrador'])
    menu.rows.append(['X. Salir'])
    menu.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu)

def mostrar_menu_medico():
    menu = BeautifulTable()
    menu.columns.header = ['============================ MENÚ MÉDICO ============================']
    menu.rows.append(['1. Ver fichas médicas'])
    menu.rows.append(['2. Generar anamnesis y diagnóstico'])
    menu.rows.append(['3. Recetar medicamentos o exámenes'])
    menu.rows.append(['4. Buscar un paciente por RUT'])
    menu.rows.append(['5. Ver pacientes atendidos'])
    menu.rows.append(['6. Insertar paciente'])
    menu.rows.append(['7. Salir'])
    menu.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu)

def mostrar_menu_admin():
    menu = BeautifulTable()
    menu.columns.header = ['============================ MENÚ ADMINISTRADOR ============================']
    menu.rows.append(['1. Mantenimiento de medicamentos'])
    menu.rows.append(['2. Mantenimiento de médicos'])
    menu.rows.append(['3. Mantenimiento de especialidades'])
    menu.rows.append(['4. Salir'])
    menu.columns.alignment = BeautifulTable.ALIGN_LEFT
    print(menu)

def obtener_ficha(conexion, medico_id):
    cursor = conexion.cursor()
    consulta = """
        SELECT m.nombre AS 'Nombre Médico', m.especialidad, fm.anamnesis, fm.diagnostico
        FROM fichamedica fm
        INNER JOIN medicoPaciente mp ON fm.paciente_id = mp.paciente_id
        INNER JOIN medico m ON mp.medico_id = m.id_medico
        WHERE m.id_medico = %s
    """
    valores = (medico_id,)
    cursor.execute(consulta, valores)
    resultados = cursor.fetchall()

    if resultados:
        table = BeautifulTable()
        table.columns.header = ['Nombre Médico', 'Especialidad', 'Anamnesis', 'Diagnóstico']
        for resultado in resultados:
            table.rows.append(resultado)
        return table
    else:
        return None

def generar_anamnesis_diagnostico(conexion, paciente_id, anamnesis_desc, diagnostico):
    try:
        cursor = conexion.cursor()
        consulta_verificacion = "SELECT id_paciente FROM paciente WHERE id_paciente = %s"
        cursor.execute(consulta_verificacion, (paciente_id,))
        if cursor.fetchone() is None:
            print(f"Error: El paciente con ID {paciente_id} no existe.")
            return
        
        consulta = """
            INSERT INTO fichamedica (paciente_id, fecha, anamnesis, diagnostico)
            VALUES (%s, %s, %s, %s)
        """
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        valores = (paciente_id, fecha_actual, anamnesis_desc, diagnostico)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Anamnesis y diagnóstico generados correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al generar la anamnesis y el diagnóstico: {err}")

def recetar_medicamentos(conexion, ficha_medica_id, medicamento_id, dosis, frecuencia, duracion):
    cursor = conexion.cursor()
    
    
    cursor.execute("SELECT COUNT(*) FROM medicamento WHERE id_medicamento = %s", (medicamento_id,))
    resultado = cursor.fetchone()

    if resultado[0] == 0:
        print(f"Error: No existe un medicamento con el ID {medicamento_id}")
        return

    cursor.execute("SELECT COUNT(*) FROM fichamedica WHERE id_fichamedica = %s", (ficha_medica_id,))
    resultado = cursor.fetchone()

    if resultado[0] == 0:
        print(f"Error: No existe una ficha médica con el ID {ficha_medica_id}")
        return

    
    consulta = """
    INSERT INTO prescripcion (ficha_medica_id, medicamento_id, dosis, frecuencia, duracion)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (ficha_medica_id, medicamento_id, dosis, frecuencia, duracion)

    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Medicamento recetado con éxito.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conexion.rollback()

    cursor.close()

def pacientes_atendidos(conexion, medico_id):
    cursor = conexion.cursor()
    consulta = """
        SELECT p.nombre AS 'Nombre Paciente', fm.fecha AS 'Fecha Atención'
        FROM fichamedica fm
        INNER JOIN paciente p ON fm.paciente_id = p.id_paciente
        INNER JOIN medicoPaciente mp ON fm.paciente_id = mp.paciente_id
        WHERE mp.medico_id = %s
    """
    valores = (medico_id,)
    cursor.execute(consulta, valores)
    resultados = cursor.fetchall()

    if resultados:
        table = BeautifulTable()
        table.columns.header = ['Nombre Paciente', 'Fecha Atención']
        for resultado in resultados:
            table.rows.append(resultado)
        return table
    else:
        return None

def insertar_paciente(paciente_dao):
    id_paciente = input("Ingrese el ID del paciente: ").strip()
    nombre = input("Ingrese el nombre del paciente: ").strip()
    rut = input("Ingrese el RUT del paciente: ").strip()
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ").strip()
    sexo = input("Ingrese el sexo del paciente: ").strip()
    direccion = input("Ingrese la dirección del paciente: ").strip()
    telefono = input("Ingrese el teléfono del paciente: ").strip()

    nuevo_paciente = Paciente(id_paciente, nombre, rut, fecha_nacimiento, sexo, direccion, telefono)
    resultado = paciente_dao.insertar_paciente(nuevo_paciente)
    print(resultado)

def mantenimiento(conexion, tabla):
    cursor = conexion.cursor
    while True:
        print(f"Mantenimiento de {tabla}")
        print("1. Agregar")
        print("2. Editar")
        print("3. Eliminar")
        print("4. Volver al menú principal")
        opcion = input("Ingrese su opción: ").strip()

        if opcion == '1':
            if tabla == "medico":
                medico_dao = MedicoDao()
                medico_dao.insertar_medico()
                print("MEDICO INSERTADO")
                
            elif tabla == "medicamento":
                nombre = input("Ingrese el nombre del medicamento: ")
                descripcion = input("Ingresa su descripcion")
                medicamento = Medicamento(None, nombre, descripcion)
                medicamento_dao = MedicamentoDao()
                medicamento_dao.insertar_medicamento(medicamento)
                print("MEDICAMENTO INSERTADO")

            elif tabla == "especialidad":
                nombre = input("Ingresa el Nombre de la Especialidad: ")
                especialidad = Especialidad(None, nombre)
                especialidad_dao = EspecialidadDao()
                especialidad_dao.insertar_especialidad(especialidad)
                print("ESPECIALIDAD INGRESADA")
            else:
                print("Tabla no reconocida")
            
        elif opcion == '2':
            if tabla == "medico":
                id_medico = input("Ingrese el ID del médico que desea editar: ").strip()
                medico_dao = MedicoDao()
                medico_dao.editar_medico(id_medico)
                print("MEDICO ELIMINADO")
                
            elif tabla == "medicamento":
                id_medicamento = input("Ingrese el ID del medicamento que desea editar: ").strip()
                medicamento_dao = MedicamentoDao()
                medicamento_dao.editar_medicamento(id_medicamento)
                print("MEDICAMENTO EDITADO")

            elif tabla == "especialidad":
                id_especialidad = input("Ingrese el ID de la especialidad que desea editar: ").strip()
                especialidad_dao = EspecialidadDao()
                especialidad_dao.editar_especialidad(id_especialidad)
                print("ESPECIALIDAD EDITADA")
            else:
                print("Tabla no reconocida")
        elif opcion == '3':
            if tabla == "medico":
                id_medico = input("Ingrese el ID del médico que desea eliminar: ").strip()
                medico_dao = MedicoDao()
                medico_dao.eliminar_medico(id_medico)
                print("MEDICO EDITADO")
                
            elif tabla == "medicamento":
                id_medicamento = input("Ingrese el ID del medicamento que desea eliminar: ").strip()
                medicamento_dao = MedicamentoDao()
                medicamento_dao.eliminar_medicamento(id_medicamento)
                print("MEDICAMENTO EDITADO")

            elif tabla == "especialidad":
                id_especialidad = input("Ingrese el ID del especialidad que desea eliminar: ").strip()
                especialidad_dao = EspecialidadDao()
                especialidad_dao.eliminar_especialidad(id_especialidad)
                print("ESPECIALIDAD ELIMINADA")
            
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    conexion = Conexion().connection  
    paciente_dao = PacienteDao()
    ficha_medica_dao = FichaMedicaDao()
    anamnesis_dao = AnamnesisDao()  
    diagnostico_dao = DiagnosticoDao()  

    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese su opción (X para salir): ").strip().lower()

        if opcion == 'x':
            print("Saliendo...Muchas Gracias!!")
            break

        rut = input("Ingrese su RUT: ").strip().lower()
        contraseña = input("Ingrese su contraseña: ").strip()

        if rut == "medico" and contraseña == "contraseña":
            medico_id = 1  

            while True:
                mostrar_menu_medico()
                opcion_medico = input("Ingrese su opción: ").strip()

                if opcion_medico == '1':
                    opcion_medico = '1'
                    if opcion_medico == '1':
                        dao_ficha_medica = FichaMedicaDao()

                        
                        dao_ficha_medica.listar_fichas_medicas()
                    else:
                        print("Opción no válida.")

                elif opcion_medico == '2':
                    print("Insertar anamnesis")
                    paciente_id = input("Ingrese el ID del paciente: ").strip()
                    anamnesis_desc = input("Ingrese la anamnesis: ").strip()
                    diagnostico_desc = input("Detalle en la ficha medica: ").strip()
                    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    nueva_anamnesis = Anamnesis(None, paciente_id, medico_id, fecha_actual, anamnesis_desc)
                    resultado_anamnesis = anamnesis_dao.insertar_anamnesis(nueva_anamnesis)
                    print(resultado_anamnesis)

                    print("Insertar Diagnóstico")
                    fecha_diagnostico = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
                    descripcion_diagnostico = input("Ingrese una descripción: ").strip()
                    nuevo_diagnostico = Diagnostico(None, paciente_id, fecha_diagnostico, descripcion_diagnostico)
                    resultado_diagnostico = diagnostico_dao.insertar_diagnostico(nuevo_diagnostico)
                    print(resultado_diagnostico)

                    generar_anamnesis_diagnostico(conexion, paciente_id, anamnesis_desc, diagnostico_desc)
                    print("Ingresado con éxito")
                    time.sleep(3)
                    limpiar_pantalla()
                
                elif opcion_medico == '3':
                    ficha_medica_id = input("Ingrese el ID de la ficha médica: ").strip()
                    medicamento_id = input("Ingrese el ID del medicamento: ").strip()
                    dosis = input("Ingrese la dosis: ").strip()
                    frecuencia = input("Ingrese la frecuencia: ").strip()
                    duracion = input("Ingrese la duración: ").strip()
                    recetar_medicamentos(conexion, ficha_medica_id, medicamento_id, dosis, frecuencia, duracion)

                elif opcion_medico == '4':
                    rut = input("Ingrese el RUT del paciente que desea buscar: ")
                    dao = PacienteDao()
                    dao.buscar_por_rut(rut)

                elif opcion_medico == '5':
                    id = input("Ingrese el ID del Medico para buscar los pacientes atendidos: ").strip()
                    dao = MedicoPacienteDao()
                    dao.listar_medicopacientes_id(id)
                    

                elif opcion_medico == '6':
                    insertar_paciente(paciente_dao)

                elif opcion_medico == '7':
                    print("Volviendo al menú principal...")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

        elif rut == "admin" and contraseña == "contraseña":
            while True:
                mostrar_menu_admin()
                opcion_admin = input("Ingrese su opción: ").strip()

                if opcion_admin == '1':
                    mantenimiento(conexion, "medicamento")
                elif opcion_admin == '2':
                    mantenimiento(conexion, "medico")
                elif opcion_admin == '3':
                    mantenimiento(conexion, "especialidad")
                elif opcion_admin == '4':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        else:
            print("RUT o contraseña incorrectos. Intente de nuevo.")

    

if __name__ == "__main__":
    main()