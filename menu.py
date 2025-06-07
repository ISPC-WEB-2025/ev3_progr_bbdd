from funciones_auxiliares import limpiar_pantalla
from funciones_auxiliares import mostrar_titulo

class Menu:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def mostrar_encabezado(self, titulo):
        """Muestra el encabezado del menú"""
        limpiar_pantalla()
        mostrar_titulo(f"📋 {titulo}")
        print(f"Usuario: {self.usuario.perfil.nombre_completo} ({self.usuario.tipo})")
        print()
    
    def mostrar_opcion(self, numero, icono, texto):
        """Muestra una opción del menú"""
        print(f"{numero}. {icono} {texto}")
    
    def obtener_opcion(self, max_opciones):
        """Obtiene la opción seleccionada por el usuario"""
        print()
        opcion = input(f"Selecciona una opción (1-{max_opciones}): ").strip()
        return opcion