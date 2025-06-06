class UsuarioEstandar(Usuario):
    def __init__(self, username, nombre, password):
        super().__init__(username, nombre, password)
    
    def puede_gestionar_usuarios(self):
        """Los usuarios estándar NO pueden gestionar usuarios"""
        return False
    
    def puede_ver_reportes(self):
        """Los usuarios estándar NO pueden ver reportes"""
        return False