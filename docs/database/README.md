# Documentación de la Base de Datos

## Descripción General

El sistema utiliza una base de datos relacional para almacenar la información de usuarios y sus perfiles. La estructura está diseñada para mantener la integridad de los datos y facilitar las consultas más comunes.

## Tablas

### Tabla: `usuarios`

Almacena la información básica de autenticación de los usuarios.

| Columna | Tipo | Restricciones | Descripción |
|---------|------|---------------|-------------|
| id_usuario | INT | PRIMARY KEY, AUTO_INCREMENT | Identificador único del usuario |
| nombre_usuario | VARCHAR(255) | UNIQUE, NOT NULL | Nombre de usuario para login |
| contrasena_hash | VARCHAR(255) | NOT NULL | Contraseña encriptada |
| rol | VARCHAR(50) | NOT NULL, CHECK(rol IN ('administrador', 'estandar')) | Rol del usuario |

### Tabla: `perfiles`

Almacena la información personal de los usuarios.

| Columna | Tipo | Restricciones | Descripción |
|---------|------|---------------|-------------|
| id_perfil | INT | PRIMARY KEY, AUTO_INCREMENT | Identificador único del perfil |
| id_usuario | INT | FOREIGN KEY, UNIQUE, NOT NULL | Referencia al usuario |
| nombre | VARCHAR(255) | NOT NULL | Nombre del usuario |
| apellido | VARCHAR(255) | NOT NULL | Apellido del usuario |
| email | VARCHAR(255) | UNIQUE, NULL | Correo electrónico |
| fecha_nacimiento | DATE | NULL | Fecha de nacimiento |
| direccion | VARCHAR(255) | NULL | Dirección física |
| telefono | VARCHAR(50) | NULL | Número de teléfono |

## Relaciones

### Usuario - Perfil
- Relación 1:1 (uno a uno)
- Un usuario tiene exactamente un perfil
- Un perfil pertenece a exactamente un usuario
- La relación se mantiene mediante la clave foránea `id_usuario` en la tabla `perfiles`
- Se implementa ON DELETE CASCADE (si se elimina un usuario, su perfil también se elimina)

## Índices

### Tabla `usuarios`
- PRIMARY KEY (`id_usuario`)
- UNIQUE INDEX (`nombre_usuario`)

### Tabla `perfiles`
- PRIMARY KEY (`id_perfil`)
- UNIQUE INDEX (`id_usuario`)
- UNIQUE INDEX (`email`)

## Consideraciones de Diseño

### Normalización
- Las tablas están en 3FN (Tercera Forma Normal)
- La información personal está separada de la información de autenticación
- Se evita la redundancia de datos

### Seguridad
- Las contraseñas se almacenan encriptadas
- Se utilizan tipos de datos apropiados para cada columna
- Se implementan restricciones de unicidad donde es necesario
- Se utiliza CHECK para validar los roles permitidos

### Rendimiento
- Se utilizan índices para optimizar las búsquedas más comunes
- Las claves foráneas están indexadas
- Se utilizan tipos de datos optimizados para cada columna

## Consultas Comunes

### 1. Create (Crear)
```sql
-- Crear nuevo usuario
INSERT INTO usuarios (nombre_usuario, contrasena_hash, rol)
VALUES (?, ?, ?);

-- Crear perfil para usuario
INSERT INTO perfiles (id_usuario, nombre, apellido, email, fecha_nacimiento, direccion, telefono)
VALUES (?, ?, ?, ?, ?, ?, ?);
```

### 2. Read (Leer)
```sql
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
```

### 3. Update (Actualizar)
```sql
-- Actualizar contraseña de usuario
UPDATE usuarios
SET contrasena_hash = ?
WHERE id_usuario = ?;

-- Actualizar perfil de usuario
UPDATE perfiles
SET nombre = ?, apellido = ?, email = ?, fecha_nacimiento = ?, direccion = ?, telefono = ?
WHERE id_usuario = ?;

-- Cambiar rol de usuario
UPDATE usuarios
SET rol = ?
WHERE id_usuario = ?;
```

### 4. Delete (Eliminar)
```sql
-- Eliminar usuario (el perfil se eliminará automáticamente por ON DELETE CASCADE)
DELETE FROM usuarios
WHERE id_usuario = ?;
```

## Mantenimiento

### Backups
- Se recomienda realizar backups diarios de la base de datos
- Mantener un historial de backups por al menos 30 días

### Limpieza
- Los usuarios inactivos pueden ser archivados después de 6 meses
- Mantener un registro de auditoría de cambios importantes

### Monitoreo
- Monitorear el tamaño de las tablas
- Verificar la integridad de los índices periódicamente
- Revisar el rendimiento de las consultas más frecuentes