-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql:3306
-- Tiempo de generación: 06-03-2025 a las 13:34:59
-- Versión del servidor: 8.0.32
-- Versión de PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `4thewords_prueba_michael_hernandez`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('a0f80308994f');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `legends`
--

CREATE TABLE `legends` (
  `name` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `legend_date` date NOT NULL,
  `province` varchar(50) NOT NULL,
  `canton` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `id` int NOT NULL,
  `created_at` datetime DEFAULT (now()),
  `updated_at` datetime DEFAULT (now())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `legends`
--

INSERT INTO `legends` (`name`, `category`, `description`, `image_url`, `legend_date`, `province`, `canton`, `district`, `id`, `created_at`, `updated_at`) VALUES
('La Tulevieja', 'Mito', 'Leyenda sobre una mujer encantada que deambula por las noches.', '/public/1.jpeg', '2020-05-10', 'San José', 'Desamparados', 'San Miguel', 1, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('El Cadejos', 'Mito', 'Fábula sobre un perro demoníaco...', '/public/2.jpeg', '2021-07-15', 'Alajuela', 'San Ramón', 'Sarchí', 2, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('La Llorona', 'Mito', 'Trágica historia de una mujer...', '/public/3.jpeg', '2019-03-22', 'Cartago', 'Paraíso', 'La Unión', 3, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('El Chupacabras', 'Mito', 'Relato de una criatura que ataca animales de granja.', '/public/4.jpg', '2022-01-05', 'Heredia', 'Barva', 'San Pablo', 4, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('La Siguanaba', 'Mito', 'Fantasma femenino que aparece en la noche...', '/public/5.jpg', '2021-11-11', 'San José', 'Desamparados', 'San Juan', 5, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('El Duende', 'Mito', 'Pequeño ser travieso...', '/public/6.jpg', '2020-09-30', 'Guanacaste', 'Liberia', 'Nicoya', 6, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('La Ciguapa', 'Leyenda', 'Mujer misteriosa con pies al revés...', '/public/7.jpg', '2018-06-18', 'Puntarenas', 'Quepos', 'Parrita', 7, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('El Fantasma de la Carreta', 'Leyenda', 'Historia de un antiguo conductor...', '/public/8.jpg', '2017-12-12', 'San José', 'Alajuelita', 'San Isidro', 8, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('La Dama de Blanco', 'Leyenda', 'Figura espectral vestida de blanco...', '/public/9.jpg', '2020-02-29', 'Limón', 'Pococí', 'Guácimo', 9, '2025-03-06 00:00:00', '2025-03-06 13:24:46'),
('El Gigante del Valle', 'Leyenda', 'Relato sobre un ser enorme...', '/public/10.jpg', '2019-08-08', 'San José', 'Escazú', 'San Rafael', 10, '2025-03-06 00:00:00', '2025-03-06 13:24:46');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indices de la tabla `legends`
--
ALTER TABLE `legends`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_legends_name` (`name`),
  ADD KEY `ix_legends_category` (`category`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `legends`
--
ALTER TABLE `legends`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
