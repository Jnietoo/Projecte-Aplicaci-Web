-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-02-2026 a las 19:10:12
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
-- Base de datos: `practica5`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torneos`
--

CREATE TABLE `torneos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `juego` varchar(50) NOT NULL,
  `premio` int(11) NOT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `torneos`
--

INSERT INTO `torneos` (`id`, `nombre`, `juego`, `premio`, `fecha`) VALUES
(1, 'Kings League Online', 'EAFC 24', 5000, '2024-06-15'),
(2, 'Mundialito FIFA', 'FIFA 23', 1000, '2024-07-01'),
(3, 'geri torneo', 'eFootball', 1000000, '2026-03-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario` varchar(30) NOT NULL,
  `mails` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `mails`) VALUES
('Antonio', 'antonioprueba@gmail.com'),
('Armanjot', 'Armanjots136@gmail.com'),
('BasedatosNieto', 'nietobasedatos@gmail.com'),
('Cristian', 'cristianxxl4@gmail.com'),
('Diego', 'dmiguelgaliana@gmail.com'),
('Frederick', 'vargasfred04@gmail.com'),
('Gerard', 'gerard.gonzalez0312@gmail.com'),
('Hans', 'jemi2710.39@gmail.com'),
('Jaume', 'jaumemd161718@gmail.com'),
('JoelN', 'jnietoneira@gmail.com'),
('JoelS', 'joelsansi4@gmail.com'),
('José', 'jtejeroantich@gmail.com'),
('JuanCarlos', 'j.1808carlossa@gmail.com'),
('JuanMiguel', 'juanmiguel301205@gmail.com'),
('jueeek', 'fdffdf@gmail.com'),
('Lluc', 'llukflores10@gmail.com'),
('Myrna', 'myrnapt96@gmail.com'),
('Óscar', 'oducuara12@gmail.com'),
('Raúl', 'ralugo00@gmail.com'),
('Roc', 'rocsilo44@gmail.com'),
('Sergio', 'srms1866@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_futbol`
--

CREATE TABLE `usuarios_futbol` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuarios_futbol`
--

INSERT INTO `usuarios_futbol` (`id`, `usuario`, `password`, `email`) VALUES
(1, 'joel futbol', '1234', 'jnietoneira@gmail.com'),
(2, 'geri', '1234', 'geri@gmail.com'),
(3, 'diego', '12345', 'diego@gmail.com'),
(4, 'oscar', 'qwe', 'oscar@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `torneos`
--
ALTER TABLE `torneos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario`);

--
-- Indices de la tabla `usuarios_futbol`
--
ALTER TABLE `usuarios_futbol`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `torneos`
--
ALTER TABLE `torneos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios_futbol`
--
ALTER TABLE `usuarios_futbol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
