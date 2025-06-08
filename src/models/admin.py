from usuario import Usuario

class Admin(Usuario):
    def __init__(self, username, nombre, password, email="", telefono="", direccion=""):
        super().__init__(username, nombre, password, email, telefono, direccion)
        self.tipo = "admin"  # Sobrescribe el tipo
    
    def puede_gestionar_usuarios(self):
        """Los admins pueden gestionar usuarios"""
        return True
    
    def puede_ver_reportes(self):
        """Los admins pueden ver reportes"""
        return True