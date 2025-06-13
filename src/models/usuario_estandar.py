from src.models.usuario import Usuario
from src.models.perfil import Perfil
from src.utils.func_aux import *

class UsuarioEstandar(Usuario):
    def __init__(self, nombre_usuario, contrasena, datos_perfil):
        """Inicializa un nuevo usuario estándar con sus datos básicos y perfil"""
        super().__init__(nombre_usuario, contrasena, datos_perfil)

    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False

    def obtener_tipo(self):
        """Retorna el tipo de usuario"""
        return 'usuario_estandar'