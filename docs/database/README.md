# Documentación de la Base de Datos

## Descripción General

El sistema utiliza una base de datos relacional para almacenar la información de usuarios y sus perfiles. La estructura está diseñada para mantener la integridad de los datos y facilitar las consultas más comunes.

## Creación de la Base de Datos

Para crear la base de datos y sus tablas, ejecute el script [scripts/crear_base_datos.sql](scripts/crear_base_datos.sql). Este script:
- Crea la base de datos `sistema_usuarios`
- Crea las tablas `usuarios` y `perfiles` con sus respectivas restricciones
- Establece los índices necesarios
- Crea un usuario administrador por defecto

Para ejecutar el script:
```bash
mysql -u [usuario] -p < scripts/crear_base_datos.sql
```

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

Los índices se crean para optimizar el rendimiento de las consultas más frecuentes en la base de datos:

### Tabla `usuarios`
- PRIMARY KEY (`id_usuario`): Índice primario para identificar de forma única cada usuario
- UNIQUE INDEX (`nombre_usuario`): Optimiza las búsquedas por nombre de usuario, especialmente útiles para:
  - Iniciar sesión (login)
  - Verificar disponibilidad de nombres de usuario
  - Búsquedas rápidas de usuarios específicos

### Tabla `perfiles`
- PRIMARY KEY (`id_perfil`): Índice primario para identificar de forma única cada perfil
- UNIQUE INDEX (`id_usuario`): Garantiza la relación uno a uno con la tabla usuarios
- UNIQUE INDEX (`email`): Optimiza las búsquedas por email, útiles para:
  - Verificar si un email ya está registrado
  - Búsquedas de usuarios por su email
  - Validación de unicidad de emails

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

## Operaciones CRUD

Las operaciones CRUD (Create, Read, Update, Delete) se encuentran en el archivo [scripts/operaciones_crud.sql](scripts/operaciones_crud.sql). Este archivo contiene todas las consultas SQL necesarias para:
- Crear nuevos usuarios y perfiles
- Leer información de usuarios
- Actualizar datos de usuarios y perfiles
- Eliminar usuarios del sistema

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