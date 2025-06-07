class Perfil:
    def __init__(self, nombre_completo, email="", telefono="", direccion="", fecha_nacimiento=""):
        """Constructor del perfil de usuario"""
        # FALTARIAN COSAS COMO FECHA DE REGISTRO, ULTIMO ACCESO, ETC.
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento # Formato: YYYY-MM-DD
      
    
    def actualizar_email(self, nuevo_email):
        """Actualiza el email del perfil"""
        self.email = nuevo_email
    
    def actualizar_telefono(self, nuevo_telefono):
        """Actualiza el teléfono del perfil"""
        self.telefono = nuevo_telefono
    
    def actualizar_direccion(self, nueva_direccion):
        """Actualiza la dirección del perfil"""
        self.direccion = nueva_direccion
    
    def obtener_resumen(self):
        """Devuelve un resumen del perfil"""
        return {
            'nombre': self.nombre_completo,
            'email': self.email if self.email else "No registrado",
            'telefono': self.telefono if self.telefono else "No registrado",
            'direccion': self.direccion if self.direccion else "No registrada",
            'fecha_nacimiento': self.fecha_nacimiento if self.fecha_nacimiento else "No registrada"
        }
    
    def tiene_datos_completos(self):
        """Verifica si el perfil tiene todos los datos"""
        return all([self.email, self.telefono, self.direccion, self.fecha_nacimiento])