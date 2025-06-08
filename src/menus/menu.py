from src.utils.func_aux import limpiar_pantalla, mostrar_titulo, pausar
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
                        menu_admin = MenuAdmin(self.sistema)
                        menu_admin.mostrar_menu()
                    else:
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
        
        username = input("Nombre de usuario: ").strip()
        if username in self.sistema.usuarios:
            print("\n❌ Este nombre de usuario ya existe.")
            pausar()
            return
        
        nombre = input("Nombre completo: ").strip()
        password = input("Contraseña: ").strip()
        email = input("Email: ").strip()
        telefono = input("Teléfono: ").strip()
        direccion = input("Dirección: ").strip()
        
        nuevo_usuario = UsuarioEstandar(username, nombre, password, email, telefono, direccion)
        self.sistema.usuarios[username] = nuevo_usuario
        
        print("\n✅ Usuario creado exitosamente!")
        pausar()

