from src.models.perfil import Perfil

class Usuario:
    _contador_usuarios = 0  # Contador para generar IDs únicos para los usuarios
    
    def __init__(self, nombre_usuario, nombre, apellido, contrasena, email, telefono="", direccion="", perfil_id=None):
        Usuario._contador_usuarios += 1  # Incrementamos primero
        self.id_usuario = Usuario._contador_usuarios  # Luego asignamos
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.perfil = Perfil(nombre, apellido, email, telefono, direccion, perfil_id)
    
    def verificar_contrasena(self, contrasena):
        """Verifica si la contraseña es correcta"""
        return self.contrasena == contrasena
    
    def es_admin(self):
        """Indica si el usuario es administrador"""
        return False
    
    def actualizar_perfil(self, nombre=None, apellido=None, email=None, telefono=None, direccion=None):
        """Actualiza los datos del perfil"""
        self.perfil.actualizar_perfil(nombre, apellido, email, telefono, direccion)

    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'id_usuario': self.id_usuario,
            'nombre_usuario': self.nombre_usuario,
            'nombre': self.perfil.nombre,
            'apellido': self.perfil.apellido,
            'tipo': 'usuario',
            'perfil': self.perfil.obtener_resumen()
        }