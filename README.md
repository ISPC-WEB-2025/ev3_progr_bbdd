# ev3_progr_bbdd
# PROYECTO: Planificador de Proyectos Empresariales

## Módulo: Iniciación a la Programación y Base de Datos - 2025

### Integrantes del Equipo
- Aylén Bartolino Luna
- Miguel Ángel Flores
- Brenda Pogliano


## Situación Profesional
El presente enunciado se acomoda al proyecto con temática a elegir en la Práctica
Profesionalizante.

---
### Objetivo Principal
Desarrollar un programa de consola con un menú interactivo que facilite la
administración de usuarios según sus roles, diferenciando entre administradores y
usuarios estándar. Este sistema permitirá la gestión integral de registro de usuarios
e inicio de sesión, asegurando un control de acceso adecuado y una experiencia
intuitiva para los usuarios.

Además, se deberá diseñar una base de datos que permita la creación,
almacenamiento y manipulación eficiente de los datos de los usuarios, garantizando
su correcta gestión.

---
### Objetivos Específicos
1. Diseñar la base de datos. Definir la estructura, las relaciones entre tablas y los
atributos necesarios para almacenar la información de los usuarios y sus
roles.
2. Implementar la gestión de usuarios con SQL. Desarrollar consultas de
definición y manipulación de datos.
3. Definir el diagrama de clases que servirá como base para la implementación
del programa.
4. Implementar la gestión de usuario. Desarrollar Clases, atributos, métodos y
demás funciones para registrar, eliminar y visualizar usuarios según sus roles:
administrador y usuario estándar.
5. Integrar el sistema de autenticación. Establecer mecanismos de inicio de
sesión y control de acceso para garantizar la seguridad de la información.
6. Implementar un menú interactivo. Diseñar una interfaz basada en texto
(consola) que facilite la interacción y gestión de usuarios mediante opciones
claras.
---

### Requerimientos funcionales
- El programa de consola debe permitir el registro de usuarios con sus
respectivas validaciones. Contraseña. Mínimo 6 caracteres. Debe contener
letras y números.
- El programa debe contar con un mecanismo de inicio de sesión que valide las
credenciales almacenadas.
- En caso de un inicio de sesión satisfactorio, el programa debe definir
claramente los roles de usuario estándar y administrador con permisos
diferenciados. Es decir que, el programa de consola, debe permitir tanto a los
usuarios estándar como administradores el acceso restringido a ciertas
funciones según su rol mediante opciones en un menú de consola. Ej, el
usuario estándar no debería modificar su rol o bien eliminar otros usuarios.
- El programa debe manejar correctamente los errores de entrada y
proporcionar mensajes informativos.
---

### Requerimientos no funcionales
- Modularidad. El código fuente debe estar estructurado en módulos, clases y
funciones independientes para facilitar la escalabilidad, mantenimiento y
comprensión.
- Legibilidad. El código fuente debe ser claro, con variables, funciones,
módulos y clases descriptivas.
- Usabilidad. La interfaz de consola debe ser intuitiva y permitir al usuario
interactuar fácilmente con el programa. (Mensajes claros)
---

### Sugerencias para la escritura del código fuente

(Convenciones de nomenclatura estándar - comunidad de Python):
- Archivos y Directorios
    - Archivos Python: Utilizar el formato snake_case en minusculas. Ejemplo: main.py, module1.py.
    - Directorios: Utilizar nombres en minúsculas sin espacios ni caracteres especiales. Ejemplo: docs, src.
- Funciones. Utilizar el formato snake_case en minúsculas comenzando la primera palabra con un verbo en infinitivo. Ejemplo: obtener_usuario, actualizar_datos.
   - Variables. Utilizar el formato snake_case. Ejemplo: contador, nombre_usuario.
   - Constantes. Utilizar el formato snake_case en mayúsculas. Ejemplo: MAX_INTENTOS.
---


