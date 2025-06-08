from menu import MenuBase
from src.models.usuario_estandar import UsuarioEstandar
from src.models.admin import Admin
from src.utils.func_aux import pausar
# from datetime import datetime

# Simulamos el almacenamiento de usuarios en memoria
# Esta estructura será modificada por las funciones de gestión de usuarios
# No está duplicado?    
USUARIOS_REGISTRADOS = {
    'admin': Admin("admin", "Administrador del Sistema", "admin123", 
                    "admin@sistema.com", "+54-11-1234-5678", "Av. Principal 123"),
    'usuario1': UsuarioEstandar("usuario1", "Juan Pérez", "user123", 
                                "juan.perez@email.com", "+54-11-9876-5432", "Calle Falsa 456"),
    'maria': UsuarioEstandar("maria", "María García", "maria456", 
                              "maria.garcia@email.com", "", "Av. Libertador 789")
}

class MenuAdmin(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)
    
    def mostrar_menu(self):
        """Muestra el menú para administradores"""
        while True:
            self.mostrar_encabezado("👑 MENÚ ADMINISTRADOR")
            print("1. Ver lista de usuarios")
            print("2. Cerrar sesión")
            print()
            
            opcion = input("Seleccione una opción (1-2): ").strip()
            
            if opcion == "1":
                self.mostrar_lista_usuarios()
            elif opcion == "2":
                self.sistema.cerrar_sesion()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def mostrar_lista_usuarios(self):
        """Muestra la lista de usuarios registrados"""
        self.mostrar_encabezado("👥 LISTA DE USUARIOS")
        
        for username, usuario in self.sistema.usuarios.items():
            print(f"\nUsuario: {username}")
            print(f"Nombre: {usuario.perfil.nombre_completo}")
            print(f"Email: {usuario.perfil.email}")
            print("-" * 30)
        
        pausar()

    def mostrar_menu_principal(self):
        """Muestra el menú principal del administrador"""
        while True:
            self.mostrar_encabezado("PANEL DE ADMINISTRADOR")
            
            self.mostrar_opcion(1, "👥", "Gestionar Usuarios")
            self.mostrar_opcion(2, "📊", "Ver Reportes del Sistema")
            self.mostrar_opcion(3, "⚙️", "Configuración")
            self.mostrar_opcion(4, "🚪", "Cerrar Sesión")
            
            opcion = self.obtener_opcion(4) # Limita las opciones válidas a 1-4
            
            if opcion == '1':
                self.gestionar_usuarios()
            elif opcion == '2':
                self.ver_reportes()
            elif opcion == '3':
                self.configuracion()  
            elif opcion == '4':
                print("\n👋 Cerrando sesión de administrador...")
                pausar()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def gestionar_usuarios(self):
        """Menú de gestión de usuarios"""
        self.mostrar_encabezado("GESTIÓN DE USUARIOS")
        
        print("👑 Administradores:")
        for nombre_usuario, usuario in {k: v for k, v in self.obtener_todos_usuarios().items() if v.tipo == 'admin'}.items():
            perfil = usuario.perfil.obtener_resumen()
            print(f"   - {nombre_usuario} ({perfil['nombre']}) | Email: {perfil['email']}")
        
        print()
        print("👤 Usuarios Estándar:")
        for nombre_usuario, usuario in {k: v for k, v in self.obtener_todos_usuarios().items() if v.tipo == 'usuario'}.items():
            perfil = usuario.perfil.obtener_resumen()
            perfil_completo = "✅ Completo" if usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
            print(f"   - {nombre_usuario} ({perfil['nombre']}) | {perfil_completo}")
        
        print()
        
        self.mostrar_opcion(1, "➕", "Agregar Nuevo Usuario")
        self.mostrar_opcion(2, "📝", "Ver Detalles de Usuario")
        self.mostrar_opcion(3, "❌", "Eliminar Usuario")
        self.mostrar_opcion(4, "🔙", "Volver al Menú Principal")
        
        opcion = self.obtener_opcion(4)
        
        if opcion == '1':
            self.agregar_usuario()
        elif opcion == '2':
            self.ver_detalles_usuario()
        elif opcion == '3':
            self.eliminar_usuario()
        # Opción 4 vuelve automáticamente
        
        pausar()
    
    def obtener_todos_usuarios(self):
        """Obtiene todos los usuarios del sistema (simulado)"""
        # En una aplicación real, esto vendría de la base de datos
        # Aquí simulamos acceso a los usuarios del sistema
        return {
            'admin': Admin("admin", "Administrador del Sistema", "admin123", 
                          "admin@sistema.com", "+54-11-1234-5678", "Av. Principal 123"),
            'usuario1': UsuarioEstandar("usuario1", "Juan Pérez", "user123", 
                                       "juan.perez@email.com", "+54-11-9876-5432", "Calle Falsa 456"),
            'maria': UsuarioEstandar("maria", "María García", "maria456", 
                                    "maria.garcia@email.com", "", "Av. Libertador 789")
        }
    
    def ver_detalles_usuario(self):
        """Muestra detalles completos de un usuario"""
        print("\n--- VER DETALLES DE USUARIO ---")
        username = input("Usuario a consultar: ").strip()
        
        usuarios = self.obtener_todos_usuarios()
        if username in usuarios:
            usuario = usuarios[username]
            perfil = usuario.perfil.obtener_resumen()
            
            print(f"\n📋 PERFIL DE {username.upper()}:")
            print(f"   • Nombre completo: {perfil['nombre']}")
            print(f"   • Email: {perfil['email']}")
            print(f"   • Teléfono: {perfil['telefono']}")
            print(f"   • Dirección: {perfil['direccion']}")
            print(f"   • Tipo de cuenta: {usuario.tipo}")
   
            
            esta_completo = "✅ Completo" if usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
            print(f"   • Estado del perfil: {esta_completo}")
        else:
            print("❌ Usuario no encontrado.")
    
    def agregar_usuario(self):
        """Simula agregar un nuevo usuario con perfil completo"""
        print("\n--- AGREGAR USUARIO ---")
        username = input("Nombre de usuario: ").strip()
        nombre = input("Nombre completo: ").strip()
        email = input("Email: ").strip()
        telefono = input("Teléfono (opcional): ").strip()
        direccion = input("Dirección (opcional): ").strip()
        # .strip() es un método de cadena (string) que se utiliza para eliminar caracteres específicos
        # del principio y/o del final de una cadena de texto.
        # Por defecto, si no le pasas ningún argumento, .strip() eliminará los espacios en blanco

        print("\nTipo de usuario:")
        print("1. Usuario Estándar")
        print("2. Administrador")
        tipo = input("Selecciona (1-2): ").strip()
        
        tipo_texto = "Usuario Estándar" if tipo == '1' else "Administrador"
        
        print(f"\n✅ Usuario '{username}' creado exitosamente:")
        print(f"   • Nombre: {nombre}")
        print(f"   • Email: {email}")
        print(f"   • Tipo: {tipo_texto}")
        
        if telefono:
            print(f"   • Teléfono: {telefono}")
        if direccion:
            print(f"   • Dirección: {direccion}")
    
    def eliminar_usuario(self):
        """Simula eliminar un usuario"""
        print("\n--- ELIMINAR USUARIO ---")
        username = input("Usuario a eliminar: ").strip()
        
        confirmacion = input(f"¿Confirmas eliminar '{username}'? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            print(f"✅ Usuario '{username}' eliminado del sistema.")
        else:
            print("❌ Operación cancelada.")
    
    def ver_reportes(self):
        """Muestra reportes del sistema"""
        self.mostrar_encabezado("REPORTES DEL SISTEMA")
        
        usuarios = self.obtener_todos_usuarios()
        total_usuarios = len(usuarios)
        admins = len([u for u in usuarios.values() if u.tipo == 'admin'])
        usuarios_std = len([u for u in usuarios.values() if u.tipo == 'usuario'])
        perfiles_completos = len([u for u in usuarios.values() if u.perfil.tiene_datos_completos()])
        
        print("📊 ESTADÍSTICAS GENERALES:")
        print(f"   • Total de usuarios: {total_usuarios}")
        print(f"   • Administradores: {admins}")
        print(f"   • Usuarios estándar: {usuarios_std}")
        print(f"   • Perfiles completos: {perfiles_completos}/{total_usuarios}")
        
        
        print("\n📋 ACTIVIDAD RECIENTE:")
        for username, usuario in usuarios.items():
            perfil = usuario.perfil.obtener_resumen()            
        
        print()
        
        pausar()
    
    def configuracion(self):
        """Muestra configuración del sistema"""
        self.mostrar_encabezado("CONFIGURACIÓN DEL SISTEMA")
        
        print("⚙️ CONFIGURACIÓN ACTUAL:")
        print("   • Versión del sistema: 1.0.0")
        print("   • Máximo intentos de login: 3")
        print("   • Encriptación: SHA256")
        print("   • Estado del sistema: ✅ Operativo")
        print()
        
        pausar()

    '''
# Funciones adicionales para el menú de administración
# Estas funciones pueden ser descomentadas si se desea incluir en el menú
    def ver_logs(self):
        """Muestra logs del sistema"""
        self.mostrar_encabezado("LOGS DEL SISTEMA")
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("📝 EVENTOS RECIENTES:")
        print(f"   [{fecha_actual}] Sistema iniciado")
        print(f"   [{fecha_actual}] Login exitoso: {self.usuario.username}")
        print(f"   [{fecha_actual}] Acceso al panel de administración")
        print()
        
        pausar()
    '''
    