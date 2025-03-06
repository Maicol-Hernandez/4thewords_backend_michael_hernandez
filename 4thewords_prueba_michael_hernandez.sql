-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql:3306
-- Tiempo de generación: 06-03-2025 a las 13:03:17
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
('La Llorona', 'Mito', 'Trágica historia de una mujer...', 'https://example.com/images/llorona.jpg', '2019-03-22', 'Cartago', 'Paraíso', 'La Unión', 3, '2025-03-05 00:00:00', '2025-03-05 13:31:30'),
('El Chupacabras', 'Mito', 'Relato de una criatura que ataca animales de granja.', '/static/a6a0555e-39fd-4e77-873d-88c5d9d9af4d.png', '2025-03-06', 'Heredia', 'Barva', 'San Pablo', 4, '2025-03-05 00:00:00', '2025-03-06 12:15:42'),
('La Siguanaba', 'Mito', 'Fantasma femenino que aparece en la noche...', 'https://example.com/images/siguanaba.jpg', '2021-11-11', 'San José', 'Desamparados', 'San Juan', 5, '2025-03-05 00:00:00', '2025-03-05 13:31:30'),
('El Duende', 'Mito', 'Pequeño ser travieso...', 'https://example.com/images/duende.jpg', '2020-09-30', 'Guanacaste', 'Liberia', 'Nicoya', 6, '2025-03-05 00:00:00', '2025-03-05 13:31:30'),
('La Llorona', 'Leyenda', '...', '/static/91cfd8e0-0ddc-444d-bf71-fe85cd8aa314.jpg', '2025-03-05', 'San José', 'Escazú', 'San Rafael', 11, '2025-03-06 07:55:57', '2025-03-06 07:55:57'),
('La Llorona', 'Leyenda', '...blablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablablabla', '/static/e36cb73b-dc0b-405f-beee-4aebbe0cc190.jpg', '2025-03-06', 'San José', 'Escazú', 'San Rafael', 12, '2025-03-06 09:13:40', '2025-03-06 11:47:20'),
('La Llorona', 'Leyenda', '...', '/static/652aa6fd-e67b-4cc6-9eb8-83ee2e7a2794.jpg', '2025-03-05', 'San José', 'Escazú', 'San Rafael', 13, '2025-03-06 09:13:43', '2025-03-06 09:13:43'),
('La Llorona', 'Leyenda', '...ploploploploploploploploploploploploploploploploploploploploploploploplo', '/static/cff5eefc-75b1-4c1c-9594-8c94463ddc94.jpg', '2025-03-06', 'San José', 'Escazú', 'San Rafael', 14, '2025-03-06 09:14:37', '2025-03-06 12:10:30'),
('Maicol Hernandez Peralta', 'ssssssssss', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', '/static/09233e58-6190-4ed2-85a7-166906667fe5.jpg', '2025-03-06', 'Armenia Quindío', 'dsdsds', 'xxxxx', 15, '2025-03-06 09:55:19', '2025-03-06 09:55:19');

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
  ADD KEY `ix_legends_category` (`category`),
  ADD KEY `ix_legends_name` (`name`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `legends`
--
ALTER TABLE `legends`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
