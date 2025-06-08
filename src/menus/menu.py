from src.utils.func_aux import *
from src.models.usuario_estandar import UsuarioEstandar

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
        nombre_usuario = input("Nombre de usuario: ").strip()
        if nombre_usuario in self.sistema.usuarios:
            print("\n❌ Este nombre de usuario ya existe.")
            pausar()
            return
        
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
        
        # 4. Crear el usuario
        nuevo_usuario = UsuarioEstandar(nombre_usuario, nombre, apellido, contrasena, email, telefono, direccion)
        self.sistema.usuarios[nombre_usuario] = nuevo_usuario
        
        print("\n✅ Usuario creado exitosamente!")
        pausar()

