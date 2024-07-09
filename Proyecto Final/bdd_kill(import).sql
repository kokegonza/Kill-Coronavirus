-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2024 a las 13:44:14
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `k`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anamnesis`
--

CREATE TABLE `anamnesis` (
  `id_anamnesis` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `medico_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `anamnesis`
--

INSERT INTO `anamnesis` (`id_anamnesis`, `paciente_id`, `medico_id`, `fecha`, `descripcion`) VALUES
(4, 12, 1, '2024-07-08 22:28:27', 'dolor de cabeza insoportable'),
(5, 1, 1, '2024-07-08 23:21:08', 'dolor de pecho'),
(6, 3, 1, '2024-07-09 02:24:41', 'dolor de cuello');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnostico`
--

CREATE TABLE `diagnostico` (
  `id_diagnostico` int(11) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `diagnostico`
--

INSERT INTO `diagnostico` (`id_diagnostico`, `paciente_id`, `fecha`, `descripcion`) VALUES
(1, 3, '2024-09-07', 'Sindrome Febril');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad`
--

CREATE TABLE `especialidad` (
  `id_especialidad` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especialidad`
--

INSERT INTO `especialidad` (`id_especialidad`, `nombre`) VALUES
(1, 'Cardiología'),
(2, 'Dermatología'),
(3, 'Endocrinología'),
(4, 'Gastroenterología'),
(5, 'Geriatría');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidadmedico`
--

CREATE TABLE `especialidadmedico` (
  `id_especialidadMedico` int(11) NOT NULL,
  `id_medico` int(11) DEFAULT NULL,
  `id_especialidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fichamedica`
--

CREATE TABLE `fichamedica` (
  `id_fichamedica` int(11) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `anamnesis` varchar(30) DEFAULT NULL,
  `diagnostico` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fichamedica`
--

INSERT INTO `fichamedica` (`id_fichamedica`, `paciente_id`, `fecha`, `anamnesis`, `diagnostico`) VALUES
(1, 1, '2024-07-08', 'Dolor de pecho', 'Cardiopatia'),
(2, 2, '2024-07-10', 'Dolor de cabeza', 'Cancer'),
(3, 3, '2024-07-10', 'Dolor de pierna', 'Fractura severa'),
(4, 4, '2024-07-12', 'Dolor de pie', 'Fractura en el tobillo'),
(5, 5, '2024-07-15', 'Dolor de cuello', 'Fractura'),
(9, 1, '2024-07-07', 'Dolor de cabeza', 'Cancer'),
(11, 12, '2024-07-08', 'dolor de cabeza insoportable', 'cancer'),
(12, 1, '2024-07-08', 'dolor de pecho', 'pre infarto'),
(13, 3, '2024-07-09', 'dolor de cuello', 'le duele muxo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicamento`
--

CREATE TABLE `medicamento` (
  `id_medicamento` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicamento`
--

INSERT INTO `medicamento` (`id_medicamento`, `nombre`, `descripcion`) VALUES
(1, 'Aspirina', 'Analgesico'),
(2, 'Ibuprofeno', 'Antiinflamatorio no esteroideo'),
(3, 'Amoxicilina', 'Antibiotico de amplio espectro'),
(4, 'Loratadina', 'Antihistaminico'),
(5, 'Omeprazol', 'Inhibidor de la bomba de proto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medico`
--

CREATE TABLE `medico` (
  `id_medico` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `especialidad` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medico`
--

INSERT INTO `medico` (`id_medico`, `nombre`, `telefono`, `especialidad`, `email`) VALUES
(1, 'Dr. Juan Pérez', '944444444', '1', 'JuanPerez@gmail.com'),
(2, 'Dra. María González', '955555555', '2', 'MariaGonzalez@gmail.com'),
(3, 'Dr. Carlos Ruiz', '977777777', '3', 'CarlosRuiz@gmail.com'),
(4, 'Dra. Ana López', '981818181', '4', 'AnaLopez@gmail'),
(5, 'Dr. José Fernández', '917171717', '5', 'JoseFernandez@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicopaciente`
--

CREATE TABLE `medicopaciente` (
  `id_medicoPaciente` int(11) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `medico_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `medicopaciente`
--

INSERT INTO `medicopaciente` (`id_medicoPaciente`, `paciente_id`, `medico_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id_paciente` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `rut` varchar(20) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`id_paciente`, `nombre`, `rut`, `fecha_nacimiento`, `sexo`, `direccion`, `telefono`) VALUES
(1, 'Juanito Perez', '22.222.222-2', '2024-07-09', 'M', 'San Miguel', '912345678'),
(2, 'Axel Iglesias', '33.333.333-3', '2024-07-11', 'M', 'San Hector', '924681012'),
(3, 'Geovani Contreras', '44.444.444-4', '2024-07-13', 'M', 'San Jeronimo', '938943331'),
(4, 'Pedro Rodríguez', '87654321-0', '2001-07-12', 'M', 'San Javier', '998778643'),
(5, 'Ana López', '23456789-1', '2003-05-02', 'M', 'Talca', '944213321'),
(6, 'Javier Sánchez', '65432109-8', '2002-03-01', 'M', 'Linares', '122446688'),
(7, 'Sofía Ramírez', '34567890-1', '1996-05-05', 'M', 'Concepcion', '111333666'),
(8, 'Diego Pérez', '56789012-3', '1990-03-03', 'M', 'Viña del Mar', '222222222'),
(9, 'Laura Gómez', '78901234-5', '1866-01-03', 'M', 'San Clemente', '555555555'),
(10, 'Gabriel Torres', '90123456-7', '1800-04-05', 'M', 'Santiago', '474747477'),
(11, 'Brajovich Figueroa', '21.631.675-4', '2000-08-07', 'M', 'Rancagua', '993280615'),
(12, 'Emilio Sanchez', '21.632.674-3', '1999-03-07', 'M', 'San Fernando', '98704321'),
(13, 'Pancho Gonzales', '22.577.999-k', '2004-05-05', 'M', 'San Orlando', '999999999');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prescripcion`
--

CREATE TABLE `prescripcion` (
  `id_prescripcion` int(11) NOT NULL,
  `ficha_medica_id` int(11) DEFAULT NULL,
  `medicamento_id` int(11) DEFAULT NULL,
  `dosis` varchar(20) DEFAULT NULL,
  `frecuencia` varchar(30) DEFAULT NULL,
  `duracion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prescripcion`
--

INSERT INTO `prescripcion` (`id_prescripcion`, `ficha_medica_id`, `medicamento_id`, `dosis`, `frecuencia`, `duracion`) VALUES
(1, 1, 1, '10mg', 'cada 8 horas', '7 dias'),
(2, 2, 1, '20mg', 'cada  9 horas', '14 dias'),
(10, 2, 2, 'clona', '48 horas', '11 dias'),
(11, 5, 2, 'clona', '48 horas', '11 dias'),
(12, 2, 2, 'paracetamol', '48 dias', '11 dias'),
(16, 1, 1, '20mg', '48 horas', '1 semana'),
(25, 11, 5, '30mg', '48 horas', '24 dias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prescripcionmedicamento`
--

CREATE TABLE `prescripcionmedicamento` (
  `id_prescripcionMedicamento` int(11) NOT NULL,
  `prescripcion_id` int(11) DEFAULT NULL,
  `medicamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tratamiento`
--

CREATE TABLE `tratamiento` (
  `id_tratamiento` int(11) NOT NULL,
  `diagnostico_id` int(11) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `contraseña` varchar(30) DEFAULT NULL,
  `rol` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anamnesis`
--
ALTER TABLE `anamnesis`
  ADD PRIMARY KEY (`id_anamnesis`),
  ADD KEY `paciente_id` (`paciente_id`),
  ADD KEY `medico_id` (`medico_id`);

--
-- Indices de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  ADD PRIMARY KEY (`id_diagnostico`),
  ADD KEY `fk_diagnostico_paciente_id` (`paciente_id`);

--
-- Indices de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id_especialidad`);

--
-- Indices de la tabla `especialidadmedico`
--
ALTER TABLE `especialidadmedico`
  ADD PRIMARY KEY (`id_especialidadMedico`),
  ADD KEY `fk_id_medico` (`id_medico`),
  ADD KEY `fk_id_especialidad` (`id_especialidad`);

--
-- Indices de la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  ADD PRIMARY KEY (`id_fichamedica`),
  ADD KEY `fk_fichamedica_paciente_id` (`paciente_id`);

--
-- Indices de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  ADD PRIMARY KEY (`id_medicamento`);

--
-- Indices de la tabla `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`id_medico`);

--
-- Indices de la tabla `medicopaciente`
--
ALTER TABLE `medicopaciente`
  ADD PRIMARY KEY (`id_medicoPaciente`),
  ADD KEY `fk_MedicoPaciente_paciente_id` (`paciente_id`),
  ADD KEY `fk_MedicoPaciente_medico_id` (`medico_id`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id_paciente`);

--
-- Indices de la tabla `prescripcion`
--
ALTER TABLE `prescripcion`
  ADD PRIMARY KEY (`id_prescripcion`),
  ADD KEY `fk_prescripcion_fichamedica_id` (`ficha_medica_id`),
  ADD KEY `fk_medicamento_id` (`medicamento_id`);

--
-- Indices de la tabla `prescripcionmedicamento`
--
ALTER TABLE `prescripcionmedicamento`
  ADD PRIMARY KEY (`id_prescripcionMedicamento`),
  ADD KEY `fk_prescripcion_id` (`prescripcion_id`),
  ADD KEY `fk_prescripcion_medicamento_id` (`medicamento_id`);

--
-- Indices de la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD PRIMARY KEY (`id_tratamiento`),
  ADD KEY `fk_diagnostico_id` (`diagnostico_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anamnesis`
--
ALTER TABLE `anamnesis`
  MODIFY `id_anamnesis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  MODIFY `id_diagnostico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  MODIFY `id_especialidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `especialidadmedico`
--
ALTER TABLE `especialidadmedico`
  MODIFY `id_especialidadMedico` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  MODIFY `id_fichamedica` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `medicamento`
--
ALTER TABLE `medicamento`
  MODIFY `id_medicamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `medico`
--
ALTER TABLE `medico`
  MODIFY `id_medico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `medicopaciente`
--
ALTER TABLE `medicopaciente`
  MODIFY `id_medicoPaciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id_paciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `prescripcion`
--
ALTER TABLE `prescripcion`
  MODIFY `id_prescripcion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `prescripcionmedicamento`
--
ALTER TABLE `prescripcionmedicamento`
  MODIFY `id_prescripcionMedicamento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  MODIFY `id_tratamiento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `anamnesis`
--
ALTER TABLE `anamnesis`
  ADD CONSTRAINT `anamnesis_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id_paciente`),
  ADD CONSTRAINT `anamnesis_ibfk_2` FOREIGN KEY (`medico_id`) REFERENCES `medico` (`id_medico`);

--
-- Filtros para la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  ADD CONSTRAINT `fk_diagnostico_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id_paciente`);

--
-- Filtros para la tabla `especialidadmedico`
--
ALTER TABLE `especialidadmedico`
  ADD CONSTRAINT `fk_id_especialidad` FOREIGN KEY (`id_especialidad`) REFERENCES `especialidad` (`id_especialidad`),
  ADD CONSTRAINT `fk_id_medico` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id_medico`);

--
-- Filtros para la tabla `fichamedica`
--
ALTER TABLE `fichamedica`
  ADD CONSTRAINT `fk_fichamedica_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id_paciente`);

--
-- Filtros para la tabla `medicopaciente`
--
ALTER TABLE `medicopaciente`
  ADD CONSTRAINT `fk_MedicoPaciente_medico_id` FOREIGN KEY (`medico_id`) REFERENCES `medico` (`id_medico`),
  ADD CONSTRAINT `fk_MedicoPaciente_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id_paciente`);

--
-- Filtros para la tabla `prescripcion`
--
ALTER TABLE `prescripcion`
  ADD CONSTRAINT `fk_medicamento_id` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id_medicamento`),
  ADD CONSTRAINT `fk_prescripcion_fichamedica_id` FOREIGN KEY (`ficha_medica_id`) REFERENCES `fichamedica` (`id_fichamedica`);

--
-- Filtros para la tabla `prescripcionmedicamento`
--
ALTER TABLE `prescripcionmedicamento`
  ADD CONSTRAINT `fk_prescripcion_id` FOREIGN KEY (`prescripcion_id`) REFERENCES `prescripcion` (`id_prescripcion`),
  ADD CONSTRAINT `fk_prescripcion_medicamento_id` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id_medicamento`);

--
-- Filtros para la tabla `tratamiento`
--
ALTER TABLE `tratamiento`
  ADD CONSTRAINT `fk_diagnostico_id` FOREIGN KEY (`diagnostico_id`) REFERENCES `diagnostico` (`id_diagnostico`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
