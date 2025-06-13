from src.models.usuario_estandar import UsuarioEstandar
from src.utils.func_aux import *
from src.models.admin import Admin


class SistemaAut:
    def __init__(self):
        self.usuarios = {} # Diccionario para almacenar usuarios
        self.usuario_actual = None # Usuario que está logueado actualmente
        self.crear_usuarios_iniciales() 
    
    def crear_usuarios_iniciales(self):
        """Crea los usuarios predeterminados del sistema"""
        # Crear administrador
        admin = Admin("admin", "Administrador", "Sistema", "admin123",
                     "admin@sistema.com", "+54-11-1234-5678", "Av. Principal 123, CABA", perfil_id=1)
        self.usuarios[admin.nombre_usuario.lower()] = admin
        
        # Crear usuarios estándar
        usuario1 = UsuarioEstandar("usuario1", "Juan", "Pérez", "user123",
                                  "juan.perez@email.com", "+54-11-9876-5432", "Calle Falsa 456", perfil_id=2)
        self.usuarios[usuario1.nombre_usuario.lower()] = usuario1
        
        usuario2 = UsuarioEstandar("maria", "María", "García", "maria456",
                                  "maria.garcia@email.com", "", "Av. Libertador 789", perfil_id=3)
        self.usuarios[usuario2.nombre_usuario.lower()] = usuario2


    
    def mostrar_credenciales_prueba(self):
        """Muestra las credenciales de prueba"""
        limpiar_pantalla()
        mostrar_titulo("🔑 CREDENCIALES DE PRUEBA")
        print("👑 ADMINISTRADOR:")
        print("   Usuario: admin")
        print("   Contraseña: admin123")
        print()
        print("👤 USUARIOS ESTÁNDAR:")
        print("   Usuario: usuario1 | Contraseña: user123")
        print("   Usuario: maria    | Contraseña: maria456")
        print()
        pausar()

    def intentar_login(self):
        """Maneja el proceso completo de login"""
        intentos = 0
        max_intentos = 3
        
        while intentos < max_intentos:
            limpiar_pantalla()
            mostrar_titulo("🚀 SISTEMA DE LOGIN")
            
            if intentos > 0:
                print(f"⚠️  Intento {intentos + 1} de {max_intentos}")
                print()
            
            # Pedir credenciales
            nombre_usuario = input("👤 Usuario (o 's' para salir): ").strip()
            if nombre_usuario.lower() == 's':
                print("\n👋 Operación cancelada por el usuario.")
                pausar()
                return False
                
            contrasena = input("🔐 Contraseña: ").strip()
           
            # Verificar login
            if self.verificar_credenciales(nombre_usuario, contrasena):
                self.usuario_actual = self.usuarios[nombre_usuario.lower()]
                limpiar_pantalla()
                mostrar_titulo("🔑 LOGIN EXITOSO")              
                print(f"\n✅ ¡Bienvenido, {self.usuario_actual.perfil.nombre_completo}!")
                pausar()
                return True
            else:
                intentos += 1
                if intentos < max_intentos:
                    print("\n❌ Credenciales incorrectas.")
                    pausar()
                else:
                    print("\n❌ Máximo de intentos alcanzado. Acceso denegado.")
                    pausar()
                    return False
        
        return False
    
    def verificar_credenciales(self, nombre_usuario, contrasena):
        """Verifica si las credenciales son válidas"""
        nombre_usuario = nombre_usuario.lower()
        if nombre_usuario in self.usuarios:
            return self.usuarios[nombre_usuario].verificar_contrasena(contrasena)
        return False
    
    def obtener_usuario_actual(self):
        """Devuelve el usuario que está logueado"""
        return self.usuario_actual
    
    def cerrar_sesion(self):
        """Cierra la sesión actual"""
        self.usuario_actual = None
        print("\n🔒 Sesión cerrada.")
