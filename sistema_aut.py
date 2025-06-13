from src.models.usuario_estandar import UsuarioEstandar
from src.utils.func_aux import *
from src.models.admin import Admin
from src.models.perfil import Perfil


class SistemaAut:
    """Clase para manejar el sistema de autenticación de usuarios"""
    def __init__(self):
        self.usuarios = {} # Diccionario para almacenar usuarios
        self.usuario_actual = None # Usuario que está logueado actualmente
        self.crear_usuarios_iniciales() 
    
    def crear_usuarios_iniciales(self):
        """Crea los usuarios predeterminados del sistema"""
        # Crear administrador
        perfil_admin = Perfil(
            nombre="Administrador",
            apellido="Sistema",
            email="admin@sistema.com",
            telefono="+54-11-1234-5678",
            direccion="Av. Principal 123, CABA",
            id_perfil=1 # Usamos el ID predefinido para este perfil
        )
        admin = Admin("admin", "admin123", perfil_admin)
        self.usuarios[admin.nombre_usuario.lower()] = admin

        # Crear usuarios estándar
        perfil_usuario1 = Perfil(
            nombre="Juan",
            apellido="Pérez",
            email="juan.perez@email.com",
            telefono="+54-11-9876-5432",
            direccion="Calle Falsa 456",
            id_perfil=2
        )
        usuario1 = UsuarioEstandar("usuario1", "user123", perfil_usuario1)
        self.usuarios[usuario1.nombre_usuario.lower()] = usuario1

        perfil_usuario2 = Perfil(
            nombre="María",
            apellido="García",
            email="maria.garcia@email.com",
            telefono="",
            direccion="Av. Libertador 789",
            id_perfil=3
        )
        usuario2 = UsuarioEstandar("maria", "maria456", perfil_usuario2)
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
