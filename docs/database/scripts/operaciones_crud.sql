-- Operaciones CRUD para el Sistema de Gestión de Usuarios
-- Este script contiene todas las operaciones comunes de la base de datos

-- =============================================
-- Operaciones CREATE (Crear)
-- =============================================

-- Crear nuevo usuario
INSERT INTO usuarios (nombre_usuario, contrasena_hash, rol)
VALUES (?, ?, ?);

-- Crear perfil de usuario
INSERT INTO perfiles (id_usuario, nombre, apellido, email, direccion, telefono)
VALUES (?, ?, ?, ?, ?, ?);

-- =============================================
-- Operaciones READ (Leer)
-- =============================================

-- Obtener información completa de un usuario
SELECT u.*, p.*
FROM usuarios u
JOIN perfiles p ON u.id_usuario = p.id_usuario
WHERE u.nombre_usuario = ?;

-- Verificar rol de usuario
SELECT rol
FROM usuarios
WHERE nombre_usuario = ?;

-- Obtener lista de usuarios con perfiles incompletos
SELECT u.nombre_usuario, p.*
FROM usuarios u
JOIN perfiles p ON u.id_usuario = p.id_usuario
WHERE p.email IS NULL OR p.telefono IS NULL OR p.direccion IS NULL;

-- Obtener lista de todos los usuarios
SELECT u.nombre_usuario, u.rol, p.nombre, p.apellido, p.email
FROM usuarios u
LEFT JOIN perfiles p ON u.id_usuario = p.id_usuario;

-- =============================================
-- Operaciones UPDATE (Actualizar)
-- =============================================

-- Actualizar contraseña de usuario
UPDATE usuarios
SET contrasena_hash = ?
WHERE id_usuario = ?;

-- Actualizar perfil de usuario
UPDATE perfiles
SET nombre = ?, 
    apellido = ?, 
    email = ?, 
    -- fecha_nacimiento = ?, -- faltó incorporar
    direccion = ?, 
    telefono = ?
WHERE id_usuario = ?;

-- Cambiar rol de usuario
UPDATE usuarios
SET rol = ?
WHERE id_usuario = ?;

-- =============================================
-- Operaciones DELETE (Eliminar)
-- =============================================

-- Eliminar usuario (el perfil se eliminará automáticamente debido a ON DELETE CASCADE)
DELETE FROM usuarios
WHERE id_usuario = ?; 