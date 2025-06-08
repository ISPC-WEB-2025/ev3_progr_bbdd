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
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso TIMESTAMP NULL
);

-- Crear tabla de perfiles
CREATE TABLE IF NOT EXISTS perfiles (
    id_perfil INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    fecha_nacimiento DATE,
    direccion VARCHAR(255),
    telefono VARCHAR(50),
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
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