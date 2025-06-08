from src.utils.func_aux import encriptar_contrasena
from perfil import Perfil

class Usuario:
 # Usamos un contador estático para generar IDs
    _next_id_usuario = 1

    def __init__(self, nombre_usuario, nombre, contrasena, email="", telefono="", direccion=""):
        self.id = Usuario._next_id_usuario # Asigna el ID actual
        Usuario._next_id_usuario += 1 # Incrementa el contador para el siguiente usuario
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