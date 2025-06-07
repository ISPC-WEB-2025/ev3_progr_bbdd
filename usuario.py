from funciones_auxiliares import encriptar_password

class Usuario:
    def __init__(self, username, nombre, password):
        self.username = username
        self.nombre = nombre
        self.password = encriptar_password(password)
        self.tipo = "usuario"  # Por defecto es usuario estándar
    
    def verificar_password(self, password):
        """Verifica si la contraseña es correcta"""
        return self.password == encriptar_password(password)
    
    def obtener_info(self):
        """Devuelve información básica del usuario"""
        return {
            'username': self.username,
            'nombre': self.nombre,
            'tipo': self.tipo
        }