from funciones_auxiliares import pausar
from menu_usuario_estandar import MenuUsuario


class SistemaCompleto:
    def __init__(self):
        self.auth = SistemaAuth()
    
    def ejecutar(self):
        """Método principal que ejecuta todo el sistema"""
        print("🚀 Iniciando Sistema de Gestión...")
        print("Cargando componentes...")
        pausar()
        
        # Mostrar credenciales de prueba
        self.auth.mostrar_credenciales_prueba()
        
        # Intentar login
        if self.auth.intentar_login():
            usuario_actual = self.auth.obtener_usuario_actual()
            
            # Crear el menú apropiado según el tipo de usuario
            if usuario_actual.tipo == "admin":
                menu = MenuAdmin(usuario_actual)
                menu.mostrar_menu_principal()
            else:
                menu = MenuUsuario(usuario_actual)
                menu.mostrar_menu_principal()
            
            # Cerrar sesión
            self.auth.cerrar_sesion()
        
        print("\n🔒 Sistema cerrado. ¡Hasta la próxima!")