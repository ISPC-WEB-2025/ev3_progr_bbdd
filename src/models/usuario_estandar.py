from src.models.usuario import Usuario
from src.utils.func_aux import *

class UsuarioEstandar(Usuario):
    def __init__(self, username, nombre_completo, password, email="", telefono="", direccion=""):
        super().__init__(username, nombre_completo, password, email, telefono, direccion)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == contrasena
    
    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False
    
    def actualizar_perfil(self, nombre_completo=None, email=None, telefono=None, direccion=None):
        """Actualiza los datos del perfil"""
        self.perfil.actualizar_perfil(nombre_completo, email, telefono, direccion)