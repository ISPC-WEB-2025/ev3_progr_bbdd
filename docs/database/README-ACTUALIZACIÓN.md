# Documentación de la Base de Datos

## Descripción General

El sistema utiliza una base de datos relacional para almacenar la información de usuarios, sus perfiles, sesiones activas y registro de actividades. La estructura está diseñada para mantener la integridad de los datos, facilitar las consultas más comunes y proporcionar un sistema completo de auditoría.

## Creación de la Base de Datos

Para crear la base de datos y sus tablas, ejecute el script [scripts/crear_base_datos.sql](scripts/crear_base_datos.sql). Este script:
- Crea la base de datos `sistema_usuarios`
- Crea las tablas `usuarios`, `perfiles`, `sesiones` y `logs_actividad` con sus respectivas restricciones
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
| rol | ENUM('administrador', 'estandar') | NOT NULL, DEFAULT 'estandar' | Rol del usuario |
| fecha_creacion | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Fecha de creación del usuario |
| ultimo_acceso | TIMESTAMP | NULL | Fecha del último acceso |
| activo | BOOLEAN | DEFAULT TRUE | Estado del usuario |


### Tabla: `perfiles`

Almacena la información personal de los usuarios.

| Columna | Tipo | Restricciones | Descripción |
|---------|------|---------------|-------------|
| id_perfil | INT | PRIMARY KEY, AUTO_INCREMENT | Identificador único del perfil |
| id_usuario | INT | FOREIGN KEY, UNIQUE, NOT NULL | Referencia al usuario |
| nombre | VARCHAR(255) | NULL | Nombre del usuario |
| apellido | VARCHAR(255) | NULL | Apellido del usuario |
| email | VARCHAR(255) | UNIQUE, NULL | Correo electrónico |
| telefono | VARCHAR(50) | NULL | Número de teléfono |
| direccion | TEXT | NULL | Dirección física |
| fecha_nacimiento | DATE | NULL | Fecha de nacimiento |
| ha_editado_datos_obligatorios | BOOLEAN | DEFAULT FALSE | Indica si ha editado datos obligatorios |
| fecha_actualizacion | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP | Última fecha de actualización |

### Tabla: `sesiones`

Gestiona las sesiones activas de los usuarios del sistema.

| Columna | Tipo | Restricciones | Descripción |
|---------|------|---------------|-------------|
| session_id | VARCHAR(255) | PRIMARY KEY | Identificador único de sesión |
| id_usuario | INT | FOREIGN KEY, NOT NULL | Referencia al usuario |
| fecha_inicio | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Fecha de inicio de sesión |
| fecha_expiracion | TIMESTAMP | NOT NULL | Fecha de expiración de la sesión |
| ip_address | VARCHAR(45) | NULL | Dirección IP del usuario |
| user_agent | VARCHAR(255) | NULL | Información del navegador |
| activa | BOOLEAN | DEFAULT TRUE | Estado de la sesión |
| ultima_actividad | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Última actividad registrada |

### Tabla: `logs_actividad`

Registra todas las actividades importantes del sistema para auditoría.

| Columna | Tipo | Restricciones | Descripción |
|---------|------|---------------|-------------|
| id_log | INT | PRIMARY KEY, AUTO_INCREMENT | Identificador único del log |
| id_usuario | INT | FOREIGN KEY, NULL | Referencia al usuario (puede ser NULL para actividades del sistema) |
| session_id | VARCHAR(255) | FOREIGN KEY, NULL | Referencia a la sesión |
| accion | VARCHAR(100) | NOT NULL | Tipo de acción realizada |
| descripcion | TEXT | NULL | Descripción detallada de la acción |
| ip_address | VARCHAR(45) | NULL | Dirección IP desde donde se realizó la acción |
| fecha_hora | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Fecha y hora del evento |

## Relaciones

### Usuario - Perfil
- Relación 1:1 (uno a uno)
- Un usuario tiene exactamente un perfil
- Un perfil pertenece a exactamente un usuario
- La relación se mantiene mediante la clave foránea `id_usuario` en la tabla `perfiles`
- Se implementa ON DELETE CASCADE (si se elimina un usuario, su perfil también se elimina)

### Usuario - Sesiones
- Relación 1:N (uno a muchos)
- Un usuario puede tener múltiples sesiones activas
- Una sesión pertenece a un único usuario
- La relación se mantiene mediante la clave foránea `id_usuario` en la tabla `sesiones`
- Se implementa ON DELETE CASCADE (si se elimina un usuario, sus sesiones también se eliminan)

### Usuario - Logs de Actividad
- Relación 1:N (uno a muchos)
- Un usuario puede generar múltiples logs de actividad
- Un log pertenece a un usuario específico (puede ser NULL para logs del sistema)
- La relación se mantiene mediante la clave foránea `id_usuario` en la tabla `logs_actividad`
- Se implementa ON DELETE SET NULL (si se elimina un usuario, los logs se mantienen pero sin referencia)

### Sesiones - Logs de Actividad
- Relación 1:N (uno a muchos)
- Una sesión puede generar múltiples logs de actividad
- Un log puede estar asociado a una sesión específica
- La relación se mantiene mediante la clave foránea `session_id` en la tabla `logs_actividad`
- Se implementa ON DELETE SET NULL (si se elimina una sesión, los logs se mantienen)

## Índices

Los índices se crean para optimizar el rendimiento de las consultas más frecuentes en la base de datos:

### Tabla `usuarios`
- PRIMARY KEY (`id_usuario`): Índice primario para identificar de forma única cada usuario
- UNIQUE INDEX (`nombre_usuario`): Optimiza las búsquedas por nombre de usuario, especialmente útiles para:
  - Iniciar sesión (login)
  - Verificar disponibilidad de nombres de usuario
  - Búsquedas rápidas de usuarios específicos
- INDEX (`activo`): Optimiza filtros por usuarios activos/inactivos
- INDEX (`ultimo_acceso`): Optimiza consultas de usuarios por actividad reciente

### Tabla `perfiles`
- PRIMARY KEY (`id_perfil`): Índice primario para identificar de forma única cada perfil
- UNIQUE INDEX (`id_usuario`): Garantiza la relación uno a uno con la tabla usuarios
- UNIQUE INDEX (`email`): Optimiza las búsquedas por email, útiles para:
  - Verificar si un email ya está registrado
  - Búsquedas de usuarios por su email
  - Validación de unicidad de emails

### Tabla `sesiones`
- PRIMARY KEY (`session_id`): Índice primario para identificar de forma única cada sesión
- INDEX (`id_usuario`): Optimiza búsquedas de sesiones por usuario
- INDEX (`activa`): Optimiza filtros por sesiones activas
- INDEX (`fecha_expiracion`): Optimiza limpieza de sesiones expiradas
- INDEX (`ultima_actividad`): Optimiza consultas por actividad reciente

### Tabla `logs_actividad`
- PRIMARY KEY (`id_log`): Índice primario para identificar de forma única cada log
- INDEX (`id_usuario`): Optimiza búsquedas de logs por usuario
- INDEX (`session_id`): Optimiza búsquedas de logs por sesión
- INDEX (`accion`): Optimiza filtros por tipo de acción
- INDEX (`fecha_hora`): Optimiza consultas cronológicas y reportes
- INDEX (`ip_address`): Optimiza búsquedas por dirección IP

## Consideraciones de Diseño

### Normalización
- Las tablas están en 3FN (Tercera Forma Normal)
- La información personal está separada de la información de autenticación
- Las sesiones y logs están en tablas separadas para optimizar consultas
- Se evita la redundancia de datos

### Seguridad
- Las contraseñas se almacenan encriptadas
- Se registran direcciones IP para auditoría de seguridad
- Se implementan restricciones de unicidad donde es necesario
- Se utiliza ENUM para validar los roles permitidos
- Sistema completo de logs para trazabilidad

### Rendimiento
- Se utilizan índices para optimizar las búsquedas más comunes
- Las claves foráneas están indexadas
- Se utilizan tipos de datos optimizados para cada columna
- Separación de datos transaccionales (sesiones, logs) de datos maestros (usuarios, perfiles)

### Gestión de Sesiones
- Sesiones con expiración automática
- Seguimiento de actividad para detectar sesiones inactivas
- Registro de información del navegador para seguridad adicional

### Auditoría y Logs
- Registro completo de actividades del sistema
- Capacidad de rastrear acciones por usuario y sesión
- Información de contexto (IP, fecha/hora) para análisis de seguridad

## Operaciones CRUD

Las operaciones CRUD (Create, Read, Update, Delete) se encuentran en el archivo [scripts/operaciones_crud.sql](scripts/operaciones_crud.sql). Este archivo contiene todas las consultas SQL necesarias para:
- Crear nuevos usuarios y perfiles
- Leer información de usuarios
- Actualizar datos de usuarios y perfiles
- Eliminar usuarios del sistema
- Gestionar sesiones de usuario
- Consultar logs de actividad

## Procedimientos de Mantenimiento

### Limpieza Automática
Se recomienda implementar procedimientos automáticos para:
- Eliminar sesiones expiradas diariamente
- Archivar logs de actividad antiguos (más de 6 meses)
- Marcar usuarios inactivos después de 90 días sin acceso

### Backups
- Se recomienda realizar backups diarios de la base de datos
- Mantener un historial de backups por al menos 30 días
- Realizar backups incrementales de las tablas de logs debido a su crecimiento

### Limpieza
- Los usuarios inactivos pueden ser archivados después de 6 meses
- Mantener logs de actividad por al menos 1 año para auditoría
- Limpiar sesiones expiradas automáticamente

### Monitoreo
- Monitorear el tamaño de las tablas, especialmente `logs_actividad`
- Verificar la integridad de los índices periódicamente
- Revisar el rendimiento de las consultas más frecuentes
- Monitorear sesiones activas para detectar patrones anómalos
- Alertas automáticas para intentos de acceso sospechosos