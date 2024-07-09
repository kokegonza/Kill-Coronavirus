-- Secuencias
CREATE SEQUENCE seq_medico START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_especialidadMedico START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_paciente START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_usuario START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_historialAcceso START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_diagnostico START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_tratamiento START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_fichamedica START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_medicoPaciente START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_medicamento START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_prescripcion START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE seq_prescripcionMedicamento START WITH 1 INCREMENT BY 1;

-- Tabla medico
CREATE TABLE medico (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    especialidad VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    email VARCHAR(30)
);

-- Tabla especialidad
CREATE TABLE especialidad (
    id_especialidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL
);

-- Tabla especialidadMedico
CREATE TABLE especialidadMedico (
    id_especialidadMedico INT AUTO_INCREMENT PRIMARY KEY,
    id_medico INT NOT NULL,
    id_especialidad INT NOT NULL,
    CONSTRAINT fk_em_medico FOREIGN KEY (id_medico) REFERENCES medico (id_medico),
    CONSTRAINT fk_em_especialidad FOREIGN KEY (id_especialidad) REFERENCES especialidad (id_especialidad)
);

-- Tabla paciente
CREATE TABLE paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- Tabla usuario
CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    rol VARCHAR(20) NOT NULL
);

-- Tabla historialAcceso
CREATE TABLE historialAcceso (
    id_historialAcceso INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha_hora VARCHAR(30) NOT NULL,
    accion VARCHAR(30) NOT NULL,
    CONSTRAINT fk_ha_usuario FOREIGN KEY (usuario_id) REFERENCES usuario (id_usuario)
);
-- Tabla diagnostico
CREATE TABLE diagnostico (
    id_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    fecha VARCHAR(30) NOT NULL,
    descripcion VARCHAR(30) NOT NULL,
    CONSTRAINT fk_diagnostico_paciente FOREIGN KEY (paciente_id) REFERENCES paciente (id_paciente)
);

-- Tabla tratamiento
CREATE TABLE tratamiento (
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    diagnostico_id INT NOT NULL,
    descripcion VARCHAR(30) NOT NULL,
    CONSTRAINT fk_tratamiento_diagnostico FOREIGN KEY (diagnostico_id) REFERENCES diagnostico (id_diagnostico)
);

-- Tabla fichamedica
CREATE TABLE fichamedica (
    id_fichamedica INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    fecha DATE NOT NULL,
    anamnesis VARCHAR(30),
    diagnostico VARCHAR(30) NOT NULL,
    CONSTRAINT fk_fm_paciente FOREIGN KEY (paciente_id) REFERENCES paciente (id_paciente)
);



-- Tabla medicoPaciente
CREATE TABLE medicoPaciente (
    id_medicoPaciente INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    CONSTRAINT fk_mp_paciente FOREIGN KEY (paciente_id) REFERENCES paciente (id_paciente),
    CONSTRAINT fk_mp_medico FOREIGN KEY (medico_id) REFERENCES medico (id_medico)
);

-- Tabla medicamento
CREATE TABLE medicamento (
    id_medicamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(30) NOT NULL
);


-- Tabla prescripcion
CREATE TABLE prescripcion (
    id_prescripcion INT AUTO_INCREMENT PRIMARY KEY,
    ficha_medica_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    dosis VARCHAR(50) NOT NULL,
    frecuencia VARCHAR(50) NOT NULL,
    duracion VARCHAR(50) NOT NULL,
    CONSTRAINT fk_prescripcion_fichamedica_id FOREIGN KEY (ficha_medica_id) REFERENCES fichamedica (id_fichamedica),
    CONSTRAINT fk_prescripcion_medicamento_id FOREIGN KEY (medicamento_id) REFERENCES medicamento (id_medicamento)
);

-- Tabla prescripcionMedicamento
CREATE TABLE prescripcionMedicamento (
    id_prescripcionMedicamento INT AUTO_INCREMENT PRIMARY KEY,
    prescripcion_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    CONSTRAINT fk_pm_prescripcion FOREIGN KEY (prescripcion_id) REFERENCES prescripcion (id_prescripcion),
    CONSTRAINT fk_pm_medicamento FOREIGN KEY (medicamento_id) REFERENCES medicamento (id_medicamento)
);

