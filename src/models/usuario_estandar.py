from usuario import Usuario

class UsuarioEstandar(Usuario):
    def __init__(self, username, nombre, password, email="", telefono="", direccion=""):
        super().__init__(username, nombre, password, email, telefono, direccion)
    
    def puede_gestionar_usuarios(self):
        """Los usuarios estándar NO pueden gestionar usuarios"""
        return False
    
    def puede_ver_reportes(self):
        """Los usuarios estándar NO pueden ver reportes"""
        return False