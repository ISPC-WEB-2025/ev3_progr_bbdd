-- Script de creación de la base de datos
-- Este script crea la base de datos y todas las tablas necesarias

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS sistema_usuarios;
USE sistema_usuarios;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('administrador', 'estandar')),
);

-- Crear tabla de perfiles
CREATE TABLE IF NOT EXISTS perfiles (
    id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    -- fecha_nacimiento DATE, -- faltó incorporar
    direccion VARCHAR(255),
    telefono VARCHAR(50),
);

-- Crear tabla de sesiones
CREATE TABLE IF NOT EXISTS sesiones (
    session_id VARCHAR(255) PRIMARY KEY, -- Usamos VARCHAR para IDs de sesión generados (ej. UUIDs)
    id_usuario INT NOT NULL,
    fecha_inicio DATETIME NOT NULL,
    fecha_expiracion DATETIME NOT NULL,
    ultima_actividad DATETIME NOT NULL,
    activa BOOLEAN DEFAULT TRUE,
    ip_address VARCHAR(45), -- Soporte para IPv4 e IPv6
    dispositivo_info TEXT, -- Información del navegador, OS, etc.
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Crear tabla de logs de actividad
CREATE TABLE IF NOT EXISTS logs_actividad (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT, -- Puede ser NULL si la acción no está asociada a un usuario específico (ej. intento de login fallido)
    session_id VARCHAR(255),
    accion VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE SET NULL, -- Si el usuario se elimina, el id_usuario en logs se pone a NULL
    FOREIGN KEY (session_id) REFERENCES sesiones(session_id) ON DELETE SET NULL -- Si la sesión se elimina, el session_id en logs se pone a NULL
);

-- Crear índices
CREATE INDEX idx_nombre_usuario ON usuarios(nombre_usuario);
CREATE INDEX idx_email ON perfiles(email);

-- Insertar usuario administrador por defecto
INSERT INTO usuarios (nombre_usuario, contrasena_hash, rol)
VALUES ('admin', SHA2('admin123', 256), 'administrador');

-- Crear perfil para el administrador por defecto
INSERT INTO perfiles (id_usuario, nombre, apellido, email)
VALUES (LAST_INSERT_ID(), 'Administrador', 'Sistema', 'admin@sistema.com'); 

-- Los índices son fundamentales para el rendimiento y la escalabilidad de tu base de datos, 
-- permitiendo que las operaciones de lectura sean rápidas y eficientes, lo cual es especialmente importante 
-- en tablas que almacenan muchos datos o son consultadas frecuentemente.