from func_aux import encriptar_contrasena
from perfil import Perfil

class Usuario:
    def __init__(self, nombre_usuario, nombre, contrasena, email="", telefono="", direccion=""):
        self.nombre_usuario = nombre_usuario
        self.contrasena = encriptar_contrasena(contrasena)
        self.tipo = "usuario"  # Por defecto es usuario estándar

        # Crear perfil asociado
        self.perfil = Perfil(nombre, email, telefono, direccion)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == encriptar_contrasena(contrasena)

    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'nombre_usuario': self.nombre_usuario,
            'nombre': self.perfil.nombre_completo,
            'tipo': self.tipo,
            'perfil': self.perfil.obtener_resumen()
        }