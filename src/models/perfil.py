class Perfil:
    def __init__(self, nombre_completo, email="", telefono="", direccion=""):
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def actualizar_perfil(self, nombre_completo=None, email=None, telefono=None, direccion=None):
        """Actualiza los datos del perfil"""
        if nombre_completo:
            self.nombre_completo = nombre_completo
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if direccion:
            self.direccion = direccion
    
    def mostrar_perfil(self):
        """Muestra los datos del perfil"""
        print(f"Nombre: {self.nombre_completo}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}") 