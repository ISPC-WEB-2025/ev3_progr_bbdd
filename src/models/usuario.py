from src.models.perfil import Perfil

class Usuario:
    def __init__(self, nombre_usuario, nombre_completo, contrasena, email="", telefono="", direccion=""):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.perfil = Perfil(nombre_completo, email, telefono, direccion)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == contrasena
    
    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False
    
    def actualizar_perfil(self, nombre_completo=None, email=None, telefono=None, direccion=None):
        """Actualiza los datos del perfil"""
        self.perfil.actualizar_perfil(nombre_completo, email, telefono, direccion)

    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'nombre_usuario': self.nombre_usuario,
            'nombre': self.perfil.nombre_completo,
            'tipo': 'usuario',
            'perfil': self.perfil.obtener_resumen()
        }