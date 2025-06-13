# Diagrama de Clases Actual

## Descripción General

Documentación actualizada del sistema, que está diseñado con una arquitectura orientada a objetos que separa las responsabilidades en diferentes clases. La estructura principal se basa en la gestión de usuarios y sus perfiles, con diferentes roles y niveles de acceso.

## Diagrama Mermaid

```mermaid
classDiagram
    class SistemaAut {
        -dict usuarios
        -Usuario usuario_actual
        +crear_usuarios_iniciales()
        +mostrar_credenciales_prueba()
        +intentar_login()
        +crear_nuevo_usuario(nombre_usuario, contrasena, datos_perfil)
        +verificar_credenciales(nombre_usuario, contrasena)
        +obtener_usuario_actual()
        +cerrar_sesion()
    }

    class Usuario {
        -_contador_usuarios : int
        -_usuarios : list
        -id_usuario : int
        -nombre_usuario : str
        -contrasena : str
        -perfil : Perfil
        +verificar_contrasena(contrasena)
        +es_admin()
        +obtener_tipo()
        +obtener_info()
    }

    class UsuarioEstandar {
        +es_admin()
        +obtener_tipo()
    }

    class Admin {
        +es_admin()
        +obtener_info()
    }

    class Perfil {
        -_contador_perfiles : int
        -id_perfil : int
        -nombre : str
        -apellido : str
        -email : str
        -telefono : str
        -direccion : str
        -ha_editado_datos_obligatorios : bool
        +__str__()
        +nombre_completo : property
        +actualizar_perfil(nombre, apellido, email, telefono, direccion)
        +mostrar_perfil()
        +obtener_resumen()
        +tiene_datos_completos()
    }

    class MenuBase {
        -SistemaAut sistema
        +mostrar_encabezado(titulo)
        +mostrar_opcion(numero, emoji, texto)
        +obtener_opcion(max_opciones)
        -_recopilar_datos_perfil() dict
        -_recopilar_datos_nuevo_usuario() dict
        +crear_usuario() bool
    }

    class MenuPrincipal {
        +mostrar_menu_principal()
    }

    class MenuAdmin {
        +mostrar_menu()
        +mostrar_encabezado(titulo)
        +mostrar_lista_usuarios()
        +gestionar_usuarios() bool
        +obtener_todos_usuarios() dict
        +ver_detalles_usuario()
    }

    classDiagram
    class MenuUsuario {
        -Usuario usuario
        +mostrar_menu()
        +mostrar_perfil_usuario()
    }

    class PerfilUtils {
        +<<Static>> mostrar_datos_actuales(perfil)
        +<<Static>> mostrar_opciones_edicion(es_admin)
        +<<Static>> validar_nombre(nombre) bool
        +<<Static>> validar_apellido(apellido) bool
        +<<Static>> validar_email(email) bool
        +<<Static>> editar_campo(perfil, opcion, es_admin) bool
    }


    SistemaAut "1" *-- "0..*" Usuario : contiene
    Usuario <|-- UsuarioEstandar : hereda
    Usuario <|-- Admin : hereda
    Usuario "1" *-- "1" Perfil : tiene
    MenuBase <|-- MenuPrincipal : hereda
    MenuBase <|-- MenuUsuario : hereda
    MenuBase <|-- MenuAdmin : hereda
    SistemaAut "1" -- "1" MenuPrincipal : usa
    SistemaAut "1" -- "1" MenuUsuario : usa
    SistemaAut "1" -- "1" MenuAdmin : usa
    PerfilUtils ..> Perfil : utiliza
```

## Descripción de Clases

### `SistemaAut`
- **Descripción:** La clase principal que gestiona el **sistema de autenticación** y la **base de datos de usuarios**. Es el punto central para interactuar con los usuarios registrados.
- **Atributos:**
    * `usuarios`: Un **diccionario** que almacena todos los objetos `Usuario` del sistema, usando el nombre de usuario como clave para un acceso rápido y eficiente.
    * `usuario_actual`: Una **referencia** al objeto `Usuario` que está actualmente logueado en el sistema.
- **Métodos principales:**
    * `crear_usuarios_iniciales()`: **Inicializa el sistema** cargando un conjunto predefinido de usuarios para facilitar pruebas y el uso inicial de la aplicación.
    * `mostrar_credenciales_prueba()`: **Presenta al usuario las credenciales** de los usuarios predefinidos (administrador y estándar), útil para fines de demostración o prueba.
    * `intentar_login()`: **Orquesta el proceso de inicio de sesión**, solicitando credenciales al usuario y delegando la verificación. Retorna `True` si el inicio de sesión es exitoso y `False` si falla.
    * `crear_nuevo_usuario(nombre_usuario, contrasena, datos_perfil)`: **Registra un nuevo usuario** en el sistema con el nombre de usuario, contraseña y datos de perfil proporcionados. Retorna la instancia del `Usuario` recién creado o `None` si la creación no pudo completarse (ej., el nombre de usuario ya existe).
    * `verificar_credenciales(nombre_usuario, contrasena)`: **Valida las credenciales** (nombre de usuario y contraseña) proporcionadas contra los usuarios registrados. Retorna `True` si las credenciales son correctas y `False` en caso contrario.
    * `obtener_usuario_actual()`: **Devuelve el objeto `Usuario`** que está actualmente logueado en el sistema.
    * `cerrar_sesion()`: **Finaliza la sesión activa** del `usuario_actual`, estableciendo su referencia a `None`.

---

### `Usuario` (Clase Base Abstracta)
- **Descripción:** Una **clase base abstracta** que define la estructura y el comportamiento común para todos los tipos de usuarios en el sistema. Las clases que hereden de `Usuario` deben implementar sus métodos abstractos.
- **Atributos:**
    * `_contador_usuarios`: Un **atributo de clase** utilizado para generar `id_usuario` únicos y secuenciales para cada nuevo usuario.
    * `_usuarios`: Un **atributo de clase (lista)** que mantiene un registro de todas las instancias de `Usuario` creadas.
    * `id_usuario`: Un **identificador único** asignado a cada instancia de usuario.
    * `nombre_usuario`: El **nombre de usuario** único utilizado para la autenticación y el login.
    * `contrasena`: La **contraseña** asociada a este usuario.
    * `perfil`: Una **referencia** a un objeto `Perfil` que contiene los datos personales y biográficos del usuario.
- **Métodos principales:**
    * `verificar_contrasena(contrasena)`: **Compara** la contraseña proporcionada con la contraseña almacenada del usuario. Retorna `True` si coinciden, `False` en caso contrario.
    * `es_admin()`: Un **método abstracto** que debe ser implementado por las subclases para indicar si el usuario tiene el rol de administrador. Retorna un `bool`.
    * `obtener_tipo()`: Un **método abstracto** que debe ser implementado por las subclases para devolver una cadena que represente el tipo específico de usuario (ej., 'admin', 'usuario_estandar').
    * `obtener_info()`: **Devuelve un diccionario** que contiene información básica y relevante del usuario, incluyendo su ID y los datos clave de su perfil.

---

### `UsuarioEstandar`
- **Descripción:** Esta clase representa a un **usuario estándar** del sistema. Hereda todas las características de `Usuario` y define su comportamiento específico.
- **Métodos principales:**
    * `es_admin()`: **Sobrescribe** el método abstracto de `Usuario`. Siempre retorna `False`, indicando que este tipo de usuario no tiene privilegios de administrador.
    * `obtener_tipo()`: **Sobrescribe** el método abstracto de `Usuario`. Siempre retorna la cadena `'usuario_estandar'`.

---

### `Admin`
- **Descripción:** Esta clase representa a un **administrador** del sistema. Hereda las características de `Usuario` y proporciona el comportamiento asociado a los privilegios elevados.
- **Métodos principales:**
    * `es_admin()`: **Sobrescribe** el método abstracto de `Usuario`. Siempre retorna `True`, confirmando que este tipo de usuario es un administrador.
    * `obtener_tipo()`: **Sobrescribe** el método abstracto de `Usuario`. Siempre retorna la cadena `'admin'`.
    * `obtener_info()`: **Sobrescribe** el método de `Usuario`. Devuelve información específica del administrador. (Aunque en el código original pueda ser idéntico al de `Usuario`, su presencia aquí permite un comportamiento polimórfico si se necesitara una lógica distinta en el futuro).

---

### `Perfil`
- **Descripción:** La clase `Perfil` se encarga de gestionar y almacenar la **información personal detallada** de un usuario en el sistema.
- **Atributos:**
    * `_contador_perfiles`: Un **atributo de clase** utilizado para generar `id_perfil` únicos y secuenciales para cada nuevo perfil.
    * `id_perfil`: Un **identificador único** asignado a cada instancia de perfil.
    * `nombre`: El **nombre de pila** del usuario.
    * `apellido`: El **apellido** del usuario.
    * `email`: La **dirección de correo electrónico** del usuario (opcional).
    * `telefono`: El **número de teléfono** del usuario (opcional).
    * `direccion`: La **dirección física** del usuario (opcional).
    * `ha_editado_datos_obligatorios`: Un **indicador booleano** que podría usarse para controlar si el usuario ya ha completado y/o modificado los datos esenciales de su perfil.
- **Métodos principales:**
    * `__str__()`: **Proporciona una representación en cadena** del objeto `Perfil`, útil para depuración o para una impresión rápida de su ID, nombre y apellido.
    * `nombre_completo`: Una **propiedad de solo lectura** que combina los atributos `nombre` y `apellido` para retornar el nombre completo del usuario de forma conveniente.
    * `actualizar_perfil(nombre, apellido, email, telefono, direccion)`: **Modifica los datos del perfil** con los valores proporcionados. Solo actualiza los campos para los que se pasan valores (no `None`).
    * `mostrar_perfil()`: **Imprime todos los datos** del perfil de forma clara y formateada en la consola.
    * `obtener_resumen()`: **Devuelve un diccionario** que contiene un subconjunto de los datos del perfil, útil para serialización o para mostrar información resumida.
    * `tiene_datos_completos()`: **Verifica** si el perfil contiene los datos considerados obligatorios (según la lógica actual, `nombre` y `apellido`). Retorna `True` o `False`.

---

### `MenuBase`
- **Descripción:** La clase `MenuBase` sirve como **clase base para todos los menús** de la aplicación. Ofrece funcionalidades comunes para la interacción con el usuario y la presentación estandarizada de información.
- **Atributos:**
    * `sistema`: Una **referencia** a la instancia de `SistemaAut` que le permite a los menús interactuar con la lógica central del sistema, como la autenticación o la gestión de usuarios.
- **Métodos principales:**
    * `mostrar_encabezado(titulo)`: **Muestra un encabezado** estilizado en la consola, incluyendo el título del menú y, si hay un usuario logueado, su nombre completo para contextualizar la interfaz.
    * `mostrar_opcion(numero, emoji, texto)`: **Formatea y presenta visualmente** una opción individual dentro de un menú, usando un número, un emoji y una descripción textual.
    * `obtener_opcion(max_opciones)`: **Gestiona la entrada de opciones** del usuario. Solicita al usuario que seleccione una opción y valida que sea un número dentro del rango permitido, reintentando si es inválido. Retorna la opción válida como una cadena o `None` en caso de fallo repetido.
    * `_recopilar_datos_perfil()`: Un **método auxiliar privado** que guía al usuario a través del proceso de entrada de datos para un perfil, incluyendo validaciones básicas. Retorna un `dict` con los datos recopilados.
    * `_recopilar_datos_nuevo_usuario()`: Un **método auxiliar privado** que recopila la información esencial (nombre de usuario, contraseña y, opcionalmente, datos de perfil) necesaria para registrar un nuevo usuario. Retorna un `dict` con toda la información consolidada.
    * `crear_usuario()`: **Centraliza la lógica para crear un nuevo usuario**, utilizando los métodos privados de recolección de datos y delegando la creación final a la instancia de `SistemaAut`. Retorna `True` si el usuario fue creado exitosamente, `False` si la operación se cancela o falla.

---

### `MenuPrincipal`
- **Descripción:** Esta clase gestiona el **menú inicial de la aplicación**, que es la primera interfaz que el usuario ve al ejecutar el sistema, antes o al iniciar sesión.
- **Métodos principales:**
    * `mostrar_menu_principal()`: **Presenta las opciones principales** del sistema, como "Iniciar sesión", "Crear nuevo usuario", "Ver credenciales de prueba" y "Salir". Maneja la navegación a los menús específicos (`MenuAdmin`, `MenuUsuario`) o la llamada a las funciones de `SistemaAut` según la elección del usuario.

---

### `MenuUsuario`
- **Descripción:** La clase `MenuUsuario` gestiona el **menú y las acciones disponibles para un usuario estándar** una vez que ha iniciado sesión en el sistema.
- **Atributos:**
    * `usuario`: Una **referencia directa** al objeto `Usuario` que está actualmente logueado. Este atributo se inicializa en el constructor y asegura que siempre haya un usuario activo al instanciar este menú.
- **Métodos principales:**
    * `mostrar_menu()`: **Presenta las opciones específicas** para un usuario estándar (principalmente "Ver mi perfil", "Editar mi perfil" y "Cerrar sesión") y maneja las selecciones del usuario.
    * `mostrar_perfil_usuario()`: **Muestra en detalle los datos del perfil** del usuario actualmente logueado, accediendo a la información a través del atributo `self.usuario`.
    * `editar_perfil()`: **Permite al usuario editar su propio perfil**, delegando la lógica de edición de campos a los métodos estáticos de `PerfilUtils`.

---

### `MenuAdmin`
- **Descripción:** La clase `MenuAdmin` gestiona el **menú y las operaciones avanzadas disponibles para un usuario con rol de administrador**.
- **Métodos principales:**
    * `mostrar_menu()`: **Muestra el menú principal** para administradores, ofreciendo opciones de gestión de usuarios, edición de perfil propio y acceso a la configuración del sistema.
    * `mostrar_encabezado(titulo)`: **Sobrescribe** el método de `MenuBase`. Aunque en el código actual su implementación es similar, permite que el menú de administrador tenga un encabezado específico si se necesitara en el futuro.
    * `mostrar_lista_usuarios()`: **Lista todos los usuarios** registrados en el sistema, categorizándolos explícitamente como administradores o usuarios estándar, y mostrando información relevante de cada uno.
    * `gestionar_usuarios()`: **Presenta un submenú dedicado** a diversas operaciones de administración de usuarios, como ver la lista, agregar, ver detalles, editar perfiles, cambiar roles y eliminar usuarios.
    * `obtener_todos_usuarios()`: **Devuelve un diccionario** con todos los objetos `Usuario` que el `SistemaAut` tiene registrados, facilitando el acceso a la base de usuarios para la administración.
    * `ver_detalles_usuario()`: **Permite al administrador consultar los detalles completos** del perfil y el tipo de un usuario específico, buscando por su nombre de usuario.
    * `editar_perfil()`: **Permite al administrador editar su propio perfil**, utilizando la lógica de `PerfilUtils`.
    * `configuracion_sistema()`: **(Método Placeholder)** Este método representa la funcionalidad para acceder a opciones de configuración más amplias del sistema, cuya implementación detallada no se proporcionó en el código.
    * `agregar_usuario()`: **Invoca el método `crear_usuario`** (heredado de `MenuBase`) para permitir al administrador registrar un nuevo usuario en el sistema.
    * `eliminar_usuario()`: **Maneja el proceso de eliminación** de un usuario del sistema, incluyendo una confirmación. Retorna `True` si el usuario actualmente logueado es eliminado, lo que requiere un cierre de sesión.
    * `cambiar_rol_usuario()`: **Permite a un administrador modificar el rol** de un usuario existente (por ejemplo, de estándar a administrador o viceversa). Retorna `True` si el administrador actual cambia su propio rol, lo que implicaría un cierre de sesión para aplicar los cambios.
    * `editar_perfil_usuario()`: **Permite al administrador editar el perfil de *cualquier* usuario** en el sistema, utilizando la funcionalidad de `PerfilUtils`.

---

### `PerfilUtils`
- **Descripción:** La clase `PerfilUtils` es una **clase utilitaria** que agrupa **métodos estáticos** relacionados con la visualización, validación y edición de campos de perfiles. Su diseño como clase estática significa que no requiere una instancia para ser utilizada; sus métodos se llaman directamente a través del nombre de la clase.
- **Métodos principales:**
    * `mostrar_datos_actuales(perfil)`: **Muestra en consola** los datos personales actuales de un objeto `Perfil` dado.
    * `mostrar_opciones_edicion(es_admin)`: **Presenta las opciones de campos** que un usuario puede modificar en su perfil. El parámetro `es_admin` podría usarse para adaptar las opciones a diferentes roles, aunque la implementación actual las muestra de forma estándar.
    * `validar_nombre(nombre)`: **Valida** que la cadena de texto proporcionada para el `nombre` no esté vacía. Retorna un `bool` e imprime un mensaje si la validación falla.
    * `validar_apellido(apellido)`: **Valida** que la cadena de texto proporcionada para el `apellido` no esté vacía. Retorna un `bool` e imprime un mensaje si la validación falla.
    * `validar_email(email)`: **Valida el formato** de la dirección de `email` (si no está vacía), comprobando la presencia de `@` y `.`. Retorna un `bool` e imprime un mensaje si el formato es inválido.
    * `editar_campo(perfil, opcion, es_admin)`: **Permite editar un campo específico** del `perfil` dado, basándose en la `opción` elegida por el usuario. Aplica las validaciones pertinentes y, en algunos casos, restricciones si la edición no la realiza un administrador. Retorna `True` si la edición fue exitosa, `False` si falló (ej., validación) o `None` si el usuario elige "volver".

---

## Consideraciones de Diseño

### Separación de Responsabilidades
- Cada clase tiene una **responsabilidad única y bien definida** (ej., `SistemaAut` para la lógica de autenticación, `Perfil` para los datos personales, `MenuBase` y sus derivados para la interfaz de usuario).
- La **lógica de negocio está claramente separada** de la presentación de la interfaz de usuario, lo que mejora la modularidad.
- Los menús están **organizados lógicamente por tipo de usuario**, lo que simplifica la gestión de las funcionalidades específicas de cada rol.

### Extensibilidad
- El sistema ha sido diseñado para **permitir la adición de nuevos tipos de usuarios** (ej., `UsuarioPremium`) simplemente heredando de la clase `Usuario` e implementando los métodos abstractos necesarios.
- Los menús son **extensibles y modulares**, facilitando la incorporación de nuevas opciones o submenús sin afectar la estructura existente.
- Las **utilidades (`PerfilUtils`) están separadas para su reutilización**, lo que significa que la lógica de validación o presentación de perfiles puede ser usada por cualquier otra parte del sistema que la necesite.

### Seguridad
- Las **contraseñas se manejan de forma segura** (aunque el código final **debería implementar una encriptación robusta** como `hashlib.sha256` para ser seguro, en lugar de almacenarlas en texto plano).
- Los perfiles tienen un **control básico de edición** (`ha_editado_datos_obligatorios`) y ciertas **restricciones en la modificación de campos** según el rol del usuario, lo que añade una capa de protección a los datos.
- Los **roles están claramente definidos** (`es_admin()`, `obtener_tipo()`) para controlar eficazmente el acceso a funcionalidades sensibles del sistema.

### Mantenibilidad
- El código está **organizado en módulos lógicos** (clases), lo que facilita enormemente la comprensión, modificación y depuración del sistema.
- Las clases presentan una **estructura clara** con atributos y métodos bien definidos, adhiriéndose a los principios de la programación orientada a objetos para una base de código más limpia y manejable.