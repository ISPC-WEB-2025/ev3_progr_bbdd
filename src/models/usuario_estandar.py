from src.models.usuario import Usuario
from src.models.perfil import Perfil
from src.utils.func_aux import *

class UsuarioEstandar(Usuario):
    def __init__(self, nombre_usuario, nombre, apellido, contrasena, email, telefono="", direccion="", perfil_id=None):
        super().__init__(nombre_usuario, nombre, apellido, contrasena, email, telefono, direccion, perfil_id)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == contrasena
    
    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False

    def obtener_info(self):
        """Devuelve información básica del usuario"""
        info = super().obtener_info()
        info['tipo'] = 'usuario_estandar'
        return info