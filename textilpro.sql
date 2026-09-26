-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.16.0.7229
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla textilpro.alertas_stock: ~0 rows (aproximadamente)

-- Volcando datos para la tabla textilpro.clientes: ~12 rows (aproximadamente)
INSERT INTO `clientes` (`codigo`, `razon_social`, `ruc`, `direccion_fiscal`, `telefono`, `correo`, `persona_contacto`, `limite_credito`, `condiciones_pago`, `categoria`) VALUES
	(1, 'ModaTex', '123', 'Dir1', '111', 'a@mail.com', 'Juan', 5000.00, '30 dias', 'Alta'),
	(2, 'RopaPlus', '456', 'Dir2', '222', 'b@mail.com', 'Ana', 6000.00, '30 dias', 'Media'),
	(3, 'FashionPro', '789', 'Dir3', '333', 'c@mail.com', 'Luis', 7000.00, 'Contado', 'Alta'),
	(4, 'TextilMax', '321', 'Dir4', '444', 'd@mail.com', 'Carlos', 8000.00, 'Credito', 'Alta'),
	(5, 'UrbanWear', '654', 'Dir5', '555', 'e@mail.com', 'Maria', 4000.00, 'Contado', 'Media'),
	(6, 'JeansCo', '987', 'Dir6', '666', 'f@mail.com', 'Pedro', 9000.00, 'Credito', 'Alta'),
	(7, 'ClothWorld', '741', 'Dir7', '777', 'g@mail.com', 'Laura', 3000.00, 'Contado', 'Baja'),
	(8, 'EliteWear', '852', 'Dir8', '888', 'h@mail.com', 'Jose', 9500.00, 'Credito', 'Alta'),
	(9, 'GlobalTex', '963', 'Dir9', '999', 'i@mail.com', 'Sofia', 2000.00, 'Contado', 'Baja'),
	(10, 'MegaModa', '159', 'Dir10', '000', 'j@mail.com', 'Diego', 10000.00, 'Credito', 'Alta'),
	(11, 'prueba textil', '111111', 'envigado', '13211354', 'pasif@cvs_}.com', 'pepito', 5000.00, 'contado', 'alta'),
	(122, '654', '3554', 'zdfbz', '4531', 'kjkj@j.com', 'pepito', 500.00, 'credito', 'alyta');

-- Volcando datos para la tabla textilpro.control_calidad: ~10 rows (aproximadamente)
INSERT INTO `control_calidad` (`codigo`, `id_lote`, `fecha`, `id_inspector`, `puntos_verificados`, `resultados`, `defectos`, `porcentaje_rechazo`, `decision`) VALUES
	(1, 1, '2024-03-11', 1, 'ok', 'ok', 'ninguno', 0.00, 'aprobado'),
	(2, 2, '2024-03-12', 2, 'ok', 'ok', 'leve', 2.00, 'aprobado'),
	(3, 3, '2024-03-13', 3, 'ok', 'fallo', 'grave', 10.00, 'rechazo'),
	(4, 4, '2024-03-14', 4, 'ok', 'ok', 'ninguno', 0.00, 'aprobado'),
	(5, 5, '2024-03-15', 5, 'ok', 'fallo', 'leve', 5.00, 'reproceso'),
	(6, 6, '2024-03-16', 6, 'ok', 'ok', 'ninguno', 0.00, 'aprobado'),
	(7, 7, '2024-03-17', 7, 'ok', 'ok', 'leve', 3.00, 'aprobado'),
	(8, 8, '2024-03-18', 8, 'ok', 'fallo', 'grave', 12.00, 'rechazo'),
	(9, 9, '2024-03-19', 9, 'ok', 'ok', 'ninguno', 0.00, 'aprobado'),
	(10, 10, '2024-03-20', 10, 'ok', 'ok', 'leve', 1.00, 'aprobado');

-- Volcando datos para la tabla textilpro.disenos: ~10 rows (aproximadamente)
INSERT INTO `disenos` (`codigo`, `nombre`, `descripcion`, `disenador`, `fecha_creacion`, `categoria_producto`, `archivo_digital`, `version`, `id_estado`, `productos`) VALUES
	(1, 'Floral', 'estampado floral', 'Ana', '2024-01-01', 'ropa', 'file1', 'v1', 2, '1'),
	(2, 'Rayas', 'lineas', 'Luis', '2024-01-02', 'ropa', 'file2', 'v1', 2, '2'),
	(3, 'Cuadros', 'cuadros', 'Maria', '2024-01-03', 'ropa', 'file3', 'v1', 1, '3'),
	(4, 'Abstracto', 'formas', 'Carlos', '2024-01-04', 'ropa', 'file4', 'v1', 2, '4'),
	(5, 'Minimalista', 'simple', 'Laura', '2024-01-05', 'ropa', 'file5', 'v1', 2, '5'),
	(6, 'Vintage', 'retro', 'Pedro', '2024-01-06', 'ropa', 'file6', 'v1', 3, '6'),
	(7, 'Moderno', 'nuevo', 'Sofia', '2024-01-07', 'ropa', 'file7', 'v1', 2, '7'),
	(8, 'Deportivo', 'sport', 'Diego', '2024-01-08', 'ropa', 'file8', 'v1', 2, '8'),
	(9, 'Elegante', 'floral', 'Elena', '2024-01-09', 'ropa', 'file9', 'v1', 4, '9'),
	(10, 'Casual', 'estampado', 'Juan', '2024-01-10', 'ropa', 'file10', 'v1', 2, '10');

-- Volcando datos para la tabla textilpro.empleados: ~10 rows (aproximadamente)
INSERT INTO `empleados` (`numero`, `nombres`, `apellidos`, `documento_identidad`, `id_especialidad`, `nivel_habilidad`, `area_asignada`, `turno_trabajo`, `fecha_contratacion`, `productividad_promedio`) VALUES
	(1, 'Juan', 'Perez', '111', 1, 'alto', 'produccion', 'mañana', '2020-01-01', 90.00),
	(2, 'Ana', 'Gomez', '222', 2, 'medio', 'produccion', 'tarde', '2021-02-01', 80.00),
	(3, 'Luis', 'Diaz', '333', 3, 'alto', 'produccion', 'mañana', '2019-03-01', 85.00),
	(4, 'Maria', 'Lopez', '444', 4, 'medio', 'produccion', 'noche', '2022-04-01', 75.00),
	(5, 'Carlos', 'Ruiz', '555', 1, 'alto', 'produccion', 'mañana', '2020-05-01', 88.00),
	(6, 'Laura', 'Torres', '666', 2, 'medio', 'produccion', 'tarde', '2021-06-01', 82.00),
	(7, 'Pedro', 'Sanchez', '777', 3, 'alto', 'produccion', 'mañana', '2018-07-01', 87.00),
	(8, 'Sofia', 'Ramirez', '888', 4, 'medio', 'produccion', 'noche', '2022-08-01', 76.00),
	(9, 'Diego', 'Morales', '999', 1, 'alto', 'produccion', 'mañana', '2017-09-01', 91.00),
	(10, 'Elena', 'Castro', '000', 2, 'medio', 'produccion', 'tarde', '2023-01-01', 79.00);

-- Volcando datos para la tabla textilpro.especialidad_empleado: ~10 rows (aproximadamente)
INSERT INTO `especialidad_empleado` (`id_especialidad`, `nombre`) VALUES
	(1, 'tejedor'),
	(2, 'costurero'),
	(3, 'cortador'),
	(4, 'estampador'),
	(5, 'tejedor'),
	(6, 'costurero'),
	(7, 'cortador'),
	(8, 'estampador'),
	(9, 'tejedor'),
	(10, 'costurero');

-- Volcando datos para la tabla textilpro.estado_diseno: ~10 rows (aproximadamente)
INSERT INTO `estado_diseno` (`id_estado`, `nombre`) VALUES
	(1, 'borrador'),
	(2, 'aprobado'),
	(3, 'en produccion'),
	(4, 'descontinuado'),
	(5, 'aprobado'),
	(6, 'borrador'),
	(7, 'en produccion'),
	(8, 'aprobado'),
	(9, 'descontinuado'),
	(10, 'aprobado');

-- Volcando datos para la tabla textilpro.estado_inventario: ~10 rows (aproximadamente)
INSERT INTO `estado_inventario` (`id_estado`, `nombre`) VALUES
	(1, 'disponible'),
	(2, 'reservado'),
	(3, 'defectuoso'),
	(4, 'disponible'),
	(5, 'reservado'),
	(6, 'defectuoso'),
	(7, 'disponible'),
	(8, 'reservado'),
	(9, 'defectuoso'),
	(10, 'disponible');

-- Volcando datos para la tabla textilpro.inspectores: ~10 rows (aproximadamente)
INSERT INTO `inspectores` (`id_inspector`, `nombre`) VALUES
	(1, 'Juan'),
	(2, 'Ana'),
	(3, 'Luis'),
	(4, 'Maria'),
	(5, 'Carlos'),
	(6, 'Laura'),
	(7, 'Pedro'),
	(8, 'Sofia'),
	(9, 'Diego'),
	(10, 'Elena');

-- Volcando datos para la tabla textilpro.inventario: ~10 rows (aproximadamente)
INSERT INTO `inventario` (`codigo_producto`, `color`, `talla`, `cantidad`, `ubicacion`, `id_lote`, `fecha_fabricacion`, `id_estado`) VALUES
	(1, 'rojo', 'M', 50, 'A', 1, '2024-03-01', 1),
	(2, 'azul', 'L', 40, 'B', 2, '2024-03-02', 2),
	(3, 'rojo', 'S', 30, 'C', 3, '2024-03-03', 3),
	(4, 'blanco', '2x2', 20, 'D', 4, '2024-03-04', 1),
	(5, 'gris', '2x3', 10, 'E', 5, '2024-03-05', 2),
	(6, 'negro', 'L', 15, 'F', 6, '2024-03-06', 3),
	(7, 'negro', 'M', 25, 'G', 7, '2024-03-07', 1),
	(8, 'blanco', 'S', 35, 'H', 8, '2024-03-08', 2),
	(9, 'azul', 'M', 45, 'I', 9, '2024-03-09', 1),
	(10, 'verde', 'L', 60, 'J', 10, '2024-03-10', 1);

-- Volcando datos para la tabla textilpro.lotes: ~10 rows (aproximadamente)
INSERT INTO `lotes` (`id_lote`, `codigo_producto`) VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10);

-- Volcando datos para la tabla textilpro.mantenimiento: ~0 rows (aproximadamente)

-- Volcando datos para la tabla textilpro.maquinas: ~10 rows (aproximadamente)
INSERT INTO `maquinas` (`numero_serie`, `id_tipo_maquina`, `marca`, `modelo`, `anio_fabricacion`, `capacidad_produccion`, `consumo_electrico`, `ubicacion`, `estado_operativo`, `fecha_ultimo_mantenimiento`) VALUES
	(1, 1, 'Toyota', 'T1', 2015, 100, 50.00, 'A1', 'activo', '2024-01-01'),
	(2, 2, 'Singer', 'S1', 2018, 80, 30.00, 'A2', 'activo', '2024-02-01'),
	(3, 3, 'CutterPro', 'C1', 2020, 120, 40.00, 'A3', 'activo', '2024-03-01'),
	(4, 4, 'PrintX', 'P1', 2019, 90, 35.00, 'A4', 'activo', '2024-01-15'),
	(5, 1, 'Toyota', 'T2', 2017, 110, 55.00, 'A1', 'activo', '2024-02-10'),
	(6, 2, 'Singer', 'S2', 2021, 85, 28.00, 'A2', 'activo', '2024-03-05'),
	(7, 3, 'CutterPro', 'C2', 2022, 130, 45.00, 'A3', 'activo', '2024-01-20'),
	(8, 4, 'PrintX', 'P2', 2016, 95, 33.00, 'A4', 'activo', '2024-02-25'),
	(9, 1, 'Toyota', 'T3', 2014, 105, 52.00, 'A1', 'activo', '2024-03-10'),
	(10, 2, 'Singer', 'S3', 2023, 88, 29.00, 'A2', 'activo', '2024-01-30');

-- Volcando datos para la tabla textilpro.materia_prima: ~10 rows (aproximadamente)
INSERT INTO `materia_prima` (`codigo`, `descripcion`, `id_tipo_material`, `unidad_medida`, `caracteristicas`, `id_proveedor`, `precio_unitario`, `stock_minimo`) VALUES
	(1, 'Algodon', 1, 'kg', 'suave', 1, 60.00, 100),
	(2, 'Poliester', 2, 'kg', 'resistente', 2, 40.00, 200),
	(3, 'Hilo blanco', 3, 'rollo', 'fino', 3, 30.00, 50),
	(4, 'Tinte rojo', 4, 'litro', 'intenso', 4, 55.00, 30),
	(5, 'Lana', 1, 'kg', 'caliente', 5, 70.00, 80),
	(6, 'Seda', 1, 'kg', 'delicada', 6, 90.00, 20),
	(7, 'Hilo negro', 3, 'rollo', 'grueso', 3, 35.00, 60),
	(8, 'Tinte azul', 4, 'litro', 'suave', 4, 45.00, 40),
	(9, 'Nylon', 2, 'kg', 'flexible', 2, 65.00, 90),
	(10, 'Algodon premium', 1, 'kg', 'extra suave', 1, 80.00, 70);

-- Volcando datos para la tabla textilpro.ordenes_produccion: ~10 rows (aproximadamente)
INSERT INTO `ordenes_produccion` (`numero`, `fecha_emision`, `codigo_cliente`, `codigo_producto`, `cantidad`, `especificaciones`, `fecha_entrega`, `prioridad`, `estado`) VALUES
	(1, '2024-03-01', 1, 1, 100, 'ninguna', '2024-04-05', 'alta', 'pendiente'),
	(2, '2024-03-02', 2, 2, 200, 'urgente', '2024-04-10', 'alta', 'proceso'),
	(3, '2024-03-03', 3, 3, 150, 'ninguna', '2024-04-15', 'media', 'pendiente'),
	(4, '2024-03-04', 4, 4, 120, 'especial', '2024-04-20', 'alta', 'proceso'),
	(5, '2024-03-05', 5, 5, 90, 'ninguna', '2024-04-25', 'baja', 'pendiente'),
	(6, '2024-03-06', 6, 6, 80, 'urgente', '2024-05-01', 'alta', 'proceso'),
	(7, '2024-03-07', 7, 7, 70, 'ninguna', '2024-05-05', 'media', 'pendiente'),
	(8, '2024-03-08', 8, 8, 60, 'especial', '2024-05-10', 'alta', 'proceso'),
	(9, '2024-03-09', 9, 9, 50, 'ninguna', '2024-05-15', 'baja', 'pendiente'),
	(10, '2024-03-10', 10, 10, 40, 'urgente', '2024-05-20', 'alta', 'proceso');

-- Volcando datos para la tabla textilpro.procesos: ~10 rows (aproximadamente)
INSERT INTO `procesos` (`codigo`, `nombre`, `descripcion`, `secuencia`, `materias_primas`, `maquinas`, `personal`, `parametros_configuracion`, `tiempo_estandar`) VALUES
	(1, 'Tejido', 'tejido', 1, 'algodon', 'telar', 'tejedor', 'config1', 5),
	(2, 'Corte', 'corte', 2, 'poliester', 'cortadora', 'cortador', 'config2', 4),
	(3, 'Costura', 'costura', 3, 'hilo', 'maquina', 'costurero', 'config3', 6),
	(4, 'Estampado', 'estampado', 4, 'tinte', 'estampadora', 'estampador', 'config4', 3),
	(5, 'Lavado', 'lavado', 5, 'agua', 'lavadora', 'operario', 'config5', 2),
	(6, 'Secado', 'secado', 6, 'aire', 'secadora', 'operario', 'config6', 2),
	(7, 'Planchado', 'planchado', 7, 'energia', 'plancha', 'operario', 'config7', 3),
	(8, 'Empaque', 'empaque', 8, 'bolsa', 'manual', 'operario', 'config8', 2),
	(9, 'Control', 'control', 9, 'ninguno', 'manual', 'inspector', 'config9', 1),
	(10, 'Distribucion', 'distribucion', 10, 'ninguno', 'vehiculo', 'operario', 'config10', 4);

-- Volcando datos para la tabla textilpro.productos: ~10 rows (aproximadamente)
INSERT INTO `productos` (`codigo`, `nombre`, `categoria`, `subcategoria`, `composicion`, `dimensiones`, `peso`, `colores`, `procesos_fabricacion`, `tiempo_estandar`, `costo_objetivo`) VALUES
	(1, 'Camiseta', 'ropa', 'Camisetas', 'algodon', 'M', 0.20, 'rojo', 'tejido, costura', 5, 10.00),
	(2, 'Jean', 'ropa', 'Pantalones', 'denim', 'L', 0.80, 'azul', 'corte, costura', 8, 20.00),
	(3, 'Vestido', 'ropa', 'Vestidos', 'algodon', 'S', 0.30, 'rojo', 'tejido, estampado', 6, 15.00),
	(4, 'Sabana', 'hogar', 'Sabanas', 'algodon', '2x2', 1.20, 'blanco', 'tejido', 7, 25.00),
	(5, 'Cortina', 'hogar', 'Cortinas', 'poliester', '2x3', 1.50, 'gris', 'corte', 9, 30.00),
	(6, 'Chaqueta', 'ropa', 'Chaquetas', 'cuero', 'L', 1.80, 'negro', 'costura', 12, 50.00),
	(7, 'Pantalon deportivo', 'ropa', 'Pantalones', 'nylon', 'M', 0.50, 'negro', 'costura', 6, 18.00),
	(8, 'Blusa', 'ropa', 'Camisetas', 'seda', 'S', 0.20, 'blanco', 'tejido', 5, 22.00),
	(9, 'Falda', 'ropa', 'Vestidos', 'algodon', 'M', 0.30, 'azul', 'costura', 6, 16.00),
	(10, 'Camiseta premium', 'ropa', 'Camisetas', 'algodon', 'L', 0.25, 'verde', 'tejido', 5, 14.00);

-- Volcando datos para la tabla textilpro.proveedor: ~10 rows (aproximadamente)
INSERT INTO `proveedor` (`id_proveedor`, `nombre`, `pais_origen`) VALUES
	(1, 'Proveedor A', 'Colombia'),
	(2, 'Proveedor B', 'China'),
	(3, 'Proveedor C', 'Peru'),
	(4, 'Proveedor D', 'Brasil'),
	(5, 'Proveedor E', 'Argentina'),
	(6, 'Proveedor F', 'India'),
	(7, 'Proveedor G', 'Mexico'),
	(8, 'Proveedor H', 'Chile'),
	(9, 'Proveedor I', 'Ecuador'),
	(10, 'Proveedor J', 'España');

-- Volcando datos para la tabla textilpro.reporte_produccion: ~0 rows (aproximadamente)

-- Volcando datos para la tabla textilpro.tipo_maquina: ~10 rows (aproximadamente)
INSERT INTO `tipo_maquina` (`id_tipo_maquina`, `nombre`) VALUES
	(1, 'telar'),
	(2, 'maquina de coser'),
	(3, 'cortadora'),
	(4, 'estampadora'),
	(5, 'telar'),
	(6, 'maquina de coser'),
	(7, 'cortadora'),
	(8, 'estampadora'),
	(9, 'telar'),
	(10, 'maquina de coser');

-- Volcando datos para la tabla textilpro.tipo_material: ~10 rows (aproximadamente)
INSERT INTO `tipo_material` (`id_tipo_material`, `nombre`) VALUES
	(1, 'fibra natural'),
	(2, 'sintetica'),
	(3, 'hilo'),
	(4, 'tinte'),
	(5, 'fibra natural'),
	(6, 'sintetica'),
	(7, 'hilo'),
	(8, 'tinte'),
	(9, 'fibra natural'),
	(10, 'sintetica');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
