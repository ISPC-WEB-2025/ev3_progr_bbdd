class Perfil:
    _contador_perfiles = 3    # Empezamos desde 3 porque existen 3 perfiles predet.
    
    def __init__(self, nombre, apellido, email="", telefono="", direccion="", id_perfil=None):
        if id_perfil is None:
            Perfil._contador_perfiles += 1
            self.id_perfil = Perfil._contador_perfiles
        else:
            self.id_perfil = id_perfil
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    @property
    def nombre_completo(self):
        """Retorna el nombre completo del usuario"""
        return f"{self.nombre} {self.apellido}"
    
    def actualizar_perfil(self, nombre=None, apellido=None, email=None, telefono=None, direccion=None):
        """Actualiza los datos del perfil"""
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if direccion:
            self.direccion = direccion
    
    def mostrar_perfil(self):
        """Muestra los datos del perfil"""
        print(f"ID Perfil: {self.id_perfil}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
    
    def obtener_resumen(self):
        """Retorna un diccionario con el resumen del perfil"""
        return {
            'id_perfil': self.id_perfil,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'telefono': self.telefono,
            'direccion': self.direccion
        }
    
    def tiene_datos_completos(self):
        """Verifica si el perfil tiene todos los datos obligatorios completos"""
        return bool(self.nombre and self.apellido and self.email) 