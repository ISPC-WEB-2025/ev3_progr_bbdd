from src.models.usuario import Usuario
from src.models.perfil import Perfil
from src.utils.func_aux import *

class Admin(Usuario):
    def __init__(self, nombre_usuario, contrasena, datos_perfil):
        """Inicializa un nuevo usuario administrador con sus datos básicos y perfil"""
        super().__init__(nombre_usuario, contrasena, datos_perfil)

    def es_admin(self):
        """Indica si el usuario es administrador"""
        return True
    
    def obtener_tipo(self):
        """Retorna el tipo de usuario"""
        return 'admin'