from src.utils.func_aux import *
from src.models.usuario_estandar import UsuarioEstandar
from src.models.perfil import Perfil

class MenuBase:
    def __init__(self, sistema):
        self.sistema = sistema
    
    def mostrar_encabezado(self, titulo):
        """Muestra el encabezado del menú"""
        limpiar_pantalla()
        mostrar_titulo(titulo)
        if hasattr(self.sistema, 'usuario_actual') and self.sistema.usuario_actual:
            print(f"Usuario: {self.sistema.usuario_actual.perfil.nombre_completo}")
        print()
    
    def mostrar_opcion(self, numero, emoji, texto):
        """Muestra una opción del menú con formato"""
        print(f"{numero}. {emoji} {texto}")
    
    def obtener_opcion(self, max_opciones):
        """Obtiene y valida la opción seleccionada por el usuario"""
        while True:
            opcion = input(f"\nSeleccione una opción (1-{max_opciones}): ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= max_opciones:
                return opcion
            else:
                print("\n❌ Opción no válida.")
                pausar()
                return None


class MenuPrincipal(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)    

    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        while True:
            self.mostrar_encabezado("🏢 SISTEMA DE GESTIÓN")
            print("1. Iniciar sesión")
            print("2. Crear nuevo usuario")
            print("3. Ver credenciales de prueba")
            print("4. Salir")
            print()
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                if self.sistema.intentar_login():
                    if self.sistema.usuario_actual.es_admin():
                        # Importamos aquí para evitar importación circular
                        from src.menus.menu_admin import MenuAdmin
                        menu_admin = MenuAdmin(self.sistema)
                        menu_admin.mostrar_menu()
                    else:
                        # Importamos aquí para evitar importación circular
                        from src.menus.menu_usuario_est import MenuUsuario
                        menu_usuario = MenuUsuario(self.sistema)
                        menu_usuario.mostrar_menu()
            elif opcion == "2":
                self.crear_nuevo_usuario()
            elif opcion == "3":
                self.sistema.mostrar_credenciales_prueba()
            elif opcion == "4":
                print("\n👋 ¡Gracias por usar el sistema!")
                break
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")
                pausar()
    
    def crear_nuevo_usuario(self):
        """Permite crear un nuevo usuario estándar"""
        self.mostrar_encabezado("👤 CREAR NUEVO USUARIO")
        
        # 1. Solicitar nombre de usuario
        while True: # Bucle para asegurar un nombre de usuario único
            nombre_usuario_input = input("Nombre de usuario: ").strip()
            nombre_usuario_normalizado = nombre_usuario_input.lower() # Normalizar para la verificación

            if nombre_usuario_normalizado in self.sistema.usuarios:
                print("\n❌ Este nombre de usuario ya existe. Por favor, elija otro.")
                # No pausar aquí para permitir un nuevo intento inmediato en el bucle
            else:
                break # Nombre de usuario único, salimos del bucle
        nombre_usuario = nombre_usuario_normalizado
        
        
        # 2. Solicitar y validar contraseña
        while True:
            contrasena = input("Contraseña: ").strip()
            es_valida, mensaje = validar_contrasena(contrasena)
            if es_valida:
                break
            print(f"\n❌ {mensaje}")
            if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                return
        
        # 3. Solicitar datos del perfil
        print("\n📋 DATOS DEL PERFIL")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        email = input("Email: ").strip()
        telefono = input("Teléfono: ").strip()
        direccion = input("Dirección: ").strip()
        nuevo_perfil = Perfil(nombre, apellido, email, telefono, direccion)
        
        # 4. Crear el usuario
        nuevo_usuario = UsuarioEstandar(nombre_usuario, contrasena, nuevo_perfil)
        self.sistema.usuarios[nombre_usuario] = nuevo_usuario
        
        print("\n✅ Usuario creado exitosamente!")
        pausar()

