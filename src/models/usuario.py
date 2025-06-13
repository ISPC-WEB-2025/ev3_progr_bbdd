from abc import ABC, abstractmethod
from src.models.perfil import Perfil

class Usuario(ABC):
    _contador_usuarios = 0  # Contador para generar IDs únicos para los usuarios
    _usuarios = []  # Lista para almacenar usuarios en memoria
    
    def __init__(self, nombre_usuario, nombre, apellido, contrasena, email, telefono="", direccion="", perfil_id=None):
        Usuario._contador_usuarios += 1  # Incrementamos primero
        self.id_usuario = Usuario._contador_usuarios  # Luego asignamos
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.perfil = Perfil(nombre, apellido, email, telefono, direccion, perfil_id)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == contrasena
    
    @abstractmethod
    def es_admin(self):
        """Indica si el usuario es administrador"""
        pass # Método abstracto que debe ser implementado por las subclases
    
    @abstractmethod
    def obtener_tipo(self):
        """Devuelve el tipo de usuario"""
        pass # Método abstracto que debe ser implementado por las subclases
    
    # CREAR PERFIL

    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'id_usuario': self.id_usuario,
            'nombre_usuario': self.nombre_usuario,
            'nombre': self.perfil.nombre,
            'apellido': self.perfil.apellido,
            'tipo': self.obtener_tipo(),
            'perfil': self.perfil.obtener_resumen()
        }

    @classmethod
    def obtener_todos(cls):
        """Devuelve una lista de todos los usuarios"""
        return cls._usuarios.copy() # Retorna una copia para evitar modificaciones externas
    
    @classmethod
    def obtener_usuario(cls, nombre_usuario):
        """Busca un usuario por nombre de usuario"""
        for usuario in cls._usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None
    
