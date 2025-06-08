# Sistema de Gestión de Usuarios

Sistema de gestión de usuarios desarrollado en Python que permite la administración de perfiles de usuario con diferentes niveles de acceso (administrador y usuario estándar).

## 🚀 Características

- Autenticación de usuarios con diferentes roles
- Gestión de perfiles de usuario
- Interfaz de consola intuitiva
- Validación de datos y seguridad
- Sistema de encriptación de contraseñas

## 📋 Requisitos

- Python 3.8 o superior
- Sistema operativo: Windows/Linux/MacOS

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
```

2. Navegar al directorio del proyecto:
```bash
cd [NOMBRE_DEL_DIRECTORIO]
```

3. Ejecutar el programa:
```bash
python main.py
```

## 🎮 Uso

1. Iniciar sesión con las credenciales predeterminadas:
   - Usuario administrador: `admin`
   - Contraseña: `admin123`

## 📁 Estructura del Proyecto

```
📦 proyecto
 ┣ 📂 src
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📂 models
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 usuario.py
 ┃ ┃ ┣ 📜 usuario_estandar.py
 ┃ ┃ ┣ 📜 admin.py
 ┃ ┃ ┗ 📜 perfil.py
 ┃ ┣ 📂 menus
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 menu.py
 ┃ ┃ ┣ 📜 menu_admin.py
 ┃ ┃ ┣ 📜 menu_usuario.py
 ┃ ┃ ┗ 📜 menu_usuario_est.py
 ┃ ┗ 📂 utils
 ┃   ┣ 📜 __init__.py
 ┃   ┣ 📜 func_aux.py
 ┃   ┗ 📜 perfil_utils.py
 ┣ 📂 docs
 ┃ ┗ 📂 diagrams
 ┃   ┣ 📜 class_diagrams.md
 ┃   ┗ 📜 class_diagrams_current.md
 ┣ 📜 main.py
 ┣ 📜 sistema_aut.py
 ┗ 📜 README.md
```

## 📊 Documentación

### Diagramas de Clases

El proyecto incluye dos diagramas de clases:

1. [Diagrama de Clases Inicial](docs/diagrams/class_diagrams.md): Muestra la estructura base del sistema.
2. [Diagrama de Clases Actual](docs/diagrams/class_diagrams_current.md): Refleja la implementación actual con todas las clases y sus relaciones.

### Base de Datos

La documentación detallada de la base de datos se encuentra en [docs/database/README.md](docs/database/README.md), incluyendo:
- Estructura de tablas
- Relaciones
- Índices
- Consultas comunes
- Consideraciones de diseño y mantenimiento

### Clases Principales

- `SistemaAut`: Gestiona la autenticación y usuarios
- `Usuario`: Clase base para todos los tipos de usuarios
- `UsuarioEstandar`: Usuario con permisos básicos
- `Admin`: Usuario con permisos administrativos
- `Perfil`: Maneja la información personal del usuario
- `MenuBase`: Clase base para los menús del sistema
- `MenuAdmin` y `MenuUsuario`: Menús específicos para cada tipo de usuario

## 🔐 Seguridad

- Contraseñas encriptadas
- Validación de datos de entrada
- Control de acceso basado en roles
- Protección contra inyección de datos

## 👥 Equipo de Desarrollo

- Aylén Bartolino Luna
- Miguel Ángel Flores
- Brenda Pogliano

## 📝 Licencia

Este proyecto fue desarrollado como parte del curso de Programación y Base de Datos.

## ✨ Créditos

Desarrollado como parte del curso de Programación y Base de Datos.

---

## 📞 Soporte

Para reportar problemas o sugerencias, contactar a los desarrolladores del equipo.


