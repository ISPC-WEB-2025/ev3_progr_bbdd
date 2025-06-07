from funciones_auxiliares import encriptar_password
from perfil import Perfil

class Usuario:
    def __init__(self, username, nombre, password, email="", telefono="", direccion=""):
        self.username = username
        self.password = encriptar_password(password)
        self.tipo = "usuario"  # Por defecto es usuario estándar

        # Crear perfil asociado
        self.perfil = Perfil(nombre, email, telefono, direccion)
    
    def verificar_password(self, password):
        """Verifica si la contraseña es correcta"""
        return self.password == encriptar_password(password)
    
    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'username': self.username,
            'nombre': self.perfil.nombre_completo,
            'tipo': self.tipo,
            'perfil': self.perfil.obtener_resumen()
        }