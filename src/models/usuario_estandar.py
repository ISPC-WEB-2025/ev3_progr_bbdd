from src.models.usuario import Usuario
from src.models.perfil import Perfil
from src.utils.func_aux import *

class UsuarioEstandar(Usuario):
    def __init__(self, nombre_usuario, nombre, apellido, contrasena, email, telefono="", direccion="", perfil_id=None):
        super().__init__(nombre_usuario, nombre, apellido, contrasena, email, telefono, direccion, perfil_id)
    
    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False

    def obtener_tipo(self):
        """Retorna el tipo de usuario"""
        return 'usuario_estandar'