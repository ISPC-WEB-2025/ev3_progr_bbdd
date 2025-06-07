from usuario_estandar import UsuarioEstandar
from func_aux import*
from admin import Admin

class SistemaAut:
    def __init__(self):
        self.usuarios = {}
        self.usuario_actual = None
        self.crear_usuarios_iniciales()
    
    def crear_usuarios_iniciales(self):
        """Crea los usuarios predeterminados del sistema"""
        # Crear admin con perfil completo
        admin = Admin("admin", "Administrador del Sistema", "admin123", 
                     "admin@sistema.com", "+54-11-1234-5678", "Av. Principal 123, CABA")
        self.usuarios["admin"] = admin
        
        # Crear usuarios estándar con diferentes niveles de información
        usuario1 = UsuarioEstandar("usuario1", "Juan Pérez", "user123", 
                                  "juan.perez@email.com", "+54-11-9876-5432", "Calle Falsa 456, Córdoba")
        self.usuarios["usuario1"] = usuario1
        
        usuario2 = UsuarioEstandar("maria", "María García", "maria456", 
                                  "maria.garcia@email.com", "", "Av. Libertador 789, Rosario")
        self.usuarios["maria"] = usuario2
    
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