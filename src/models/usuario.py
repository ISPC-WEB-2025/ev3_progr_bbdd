from src.models.perfil import Perfil

class Usuario:
    _contador_usuarios = 0  # Contador de clase para generar IDs únicos
    
    def __init__(self, nombre_usuario, nombre, apellido, contrasena, email, telefono="", direccion="", perfil_id=None):
        self.id_usuario = Usuario._contador_usuarios + 1  # Incrementamos después de asignar
        Usuario._contador_usuarios = self.id_usuario  # Actualizamos el contador
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