from src.menus.menu import MenuBase
from src.models.usuario_estandar import UsuarioEstandar
from src.models.admin import Admin
from src.utils.func_aux import pausar, validar_contrasena
# from datetime import datetime

# Simulamos el almacenamiento de usuarios en memoria
# Esta estructura será modificada por las funciones de gestión de usuarios
# No está duplicado?    
USUARIOS_REGISTRADOS = {
    'admin': Admin("admin", "Administrador", "del Sistema", "admin123", 
                    "admin@sistema.com", "+54-11-1234-5678", "Av. Principal 123", perfil_id=1),
    'usuario1': UsuarioEstandar("usuario1", "Juan", "Pérez", "user123", 
                                "juan.perez@email.com", "+54-11-9876-5432", "Calle Falsa 456", perfil_id=2),
    'maria': UsuarioEstandar("maria", "María", "García", "maria456", 
                              "maria.garcia@email.com", "", "Av. Libertador 789", perfil_id=3)
}

class MenuAdmin(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)
    
    def mostrar_opcion(self, numero, emoji, texto):
        """Muestra una opción del menú con formato"""
        print(f"{numero}. {emoji} {texto}")
    
    def obtener_opcion(self, max_opciones):
        """Obtiene y valida la opción seleccionada por el usuario"""
        while True:
            opcion = input(f"Seleccione una opción (1-{max_opciones}): ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= max_opciones:
                return opcion
            print("\n❌ Opción no válida.")
            pausar()
    
    def mostrar_menu(self):
        """Muestra el menú para administradores"""
        while True:
            self.mostrar_encabezado("👑 MENÚ ADMINISTRADOR")
            
            self.mostrar_opcion(1, "👥", "Gestión de Usuarios")
            self.mostrar_opcion(2, "⚙️", "Configuración del sistema")
            self.mostrar_opcion(3, "🚪", "Cerrar sesión")
            print()
            
            opcion = self.obtener_opcion(3)
            
            if opcion == '1':
                self.gestionar_usuarios()
            elif opcion == '2':
                self.configuracion_sistema()
            elif opcion == '3':
                self.sistema.cerrar_sesion()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def mostrar_encabezado(self, titulo):
        """Muestra el encabezado del menú"""
        from src.utils.func_aux import limpiar_pantalla, mostrar_titulo
        limpiar_pantalla()
        mostrar_titulo(titulo)
        if hasattr(self.sistema, 'usuario_actual') and self.sistema.usuario_actual:
            print(f"Usuario: {self.sistema.usuario_actual.perfil.nombre_completo}")
        print()
    
    def mostrar_lista_usuarios(self):
        """Muestra la lista de usuarios registrados"""
        self.mostrar_encabezado("👥 LISTA DE USUARIOS")
        
        print("👑 ADMINISTRADORES:")
        for nombre_usuario, usuario in self.sistema.usuarios.items():
            if usuario.es_admin():
                info = usuario.obtener_info()
                print(f"\nID: {info['id_usuario']} | Usuario: {nombre_usuario}")
                print(f"Nombre: {info['nombre']} {info['apellido']}")
                print(f"Email: {usuario.perfil.email}")
                print(f"ID Perfil: {usuario.perfil.id_perfil}")
                print("-" * 40)
        
        print("\n👤 USUARIOS ESTÁNDAR:")
        for nombre_usuario, usuario in self.sistema.usuarios.items():
            if not usuario.es_admin():
                info = usuario.obtener_info()
                print(f"\nID: {info['id_usuario']} | Usuario: {nombre_usuario}")
                print(f"Nombre: {info['nombre']} {info['apellido']}")
                print(f"Email: {usuario.perfil.email}")
                print(f"ID Perfil: {usuario.perfil.id_perfil}")
                print("-" * 40)
        
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
        while True:
            self.mostrar_encabezado("👥 GESTIÓN DE USUARIOS")
            
            self.mostrar_opcion(1, "📝", "Ver lista de usuarios")
            self.mostrar_opcion(2, "➕", "Agregar usuario")
            self.mostrar_opcion(3, "🔍", "Ver detalles de usuario")
            self.mostrar_opcion(4, "⚙️ ", "Cambiar rol de usuario")
            self.mostrar_opcion(5, "❌", "Eliminar usuario")
            self.mostrar_opcion(6, "🏠", "Volver al menú principal")
            print()
            
            opcion = self.obtener_opcion(6)  # Limita las opciones válidas a 1-6
            
            if opcion == '1':
                self.mostrar_lista_usuarios()
            elif opcion == '2':
                self.agregar_usuario()
            elif opcion == '3':
                self.ver_detalles_usuario()
            elif opcion == '4':
                self.cambiar_rol_usuario()
            elif opcion == '5':
                self.eliminar_usuario()
            elif opcion == '6':
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def obtener_todos_usuarios(self):
        """Obtiene todos los usuarios del sistema"""
        return self.sistema.usuarios
    
    def ver_detalles_usuario(self):
        """Muestra detalles completos de un usuario"""
        self.mostrar_encabezado("🔍 DETALLES DE USUARIO")
        
        nombre_usuario = input("Usuario a consultar: ").strip()
        
        if nombre_usuario in self.sistema.usuarios:
            usuario = self.sistema.usuarios[nombre_usuario]
            info = usuario.obtener_info()
            perfil = usuario.perfil.obtener_resumen()
            
            print(f"\n📋 PERFIL DE {nombre_usuario.upper()}:")
            print(f"   • ID Usuario: {info['id_usuario']}")
            print(f"   • ID Perfil: {perfil['id_perfil']}")
            print(f"   • Nombre: {info['nombre']}")
            print(f"   • Apellido: {info['apellido']}")
            print(f"   • Email: {perfil['email']}")
            print(f"   • Teléfono: {perfil['telefono']}")
            print(f"   • Dirección: {perfil['direccion']}")
            print(f"   • Tipo de cuenta: {'👑 Administrador' if usuario.es_admin() else '👤 Usuario Estándar'}")
            
            esta_completo = "✅ Completo" if usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
            print(f"   • Estado del perfil: {esta_completo}")
        else:
            print("\n❌ Usuario no encontrado.")
        
        pausar()
    
    def agregar_usuario(self):
        """Agrega un nuevo usuario al sistema"""
        self.mostrar_encabezado("➕ AGREGAR USUARIO")
        
        # 1. Solicitar nombre de usuario
        nombre_usuario = input("Nombre de usuario: ").strip()
        if nombre_usuario in self.sistema.usuarios:
            print("\n❌ El nombre de usuario ya existe.")
            pausar()
            return
        
        # 2. Solicitar y validar contraseña
        while True:
            contrasena = input("Contraseña: ").strip()
            es_valida, mensaje = validar_contrasena(contrasena)
            if es_valida:
                break
            print(f"\n❌ {mensaje}")
            if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                return
        
        # 3. Solicitar datos del perfil
        print("\n📋 DATOS DEL PERFIL")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        email = input("Email: ").strip()
        telefono = input("Teléfono (opcional): ").strip()
        direccion = input("Dirección (opcional): ").strip()
        
        # 4. Crear el usuario (siempre como estándar)
        nuevo_usuario = UsuarioEstandar(nombre_usuario, nombre, apellido, contrasena, 
                                      email, telefono, direccion)
        
        # 5. Agregar al sistema
        self.sistema.usuarios[nombre_usuario] = nuevo_usuario
        
        # 6. Mostrar confirmación
        print(f"\n✅ Usuario '{nombre_usuario}' creado exitosamente como Usuario Estándar.")
        print(f"   • Nombre: {nombre} {apellido}")
        print(f"   • Email: {email}")
        if telefono:
            print(f"   • Teléfono: {telefono}")
        if direccion:
            print(f"   • Dirección: {direccion}")
        
        pausar()

    def cambiar_rol_usuario(self):
        """Permite cambiar el rol de un usuario entre estándar y administrador"""
        self.mostrar_encabezado("🔄 CAMBIAR ROL DE USUARIO")
        
        nombre_usuario = input("Usuario a modificar: ").strip()
        if nombre_usuario not in self.sistema.usuarios:
            print("\n❌ Usuario no encontrado.")
            pausar()
            return
            
        usuario = self.sistema.usuarios[nombre_usuario]
        rol_actual = "Administrador" if usuario.es_admin() else "Usuario Estándar"
        
        print(f"\nRol actual: {rol_actual}")
        print("\n¿A qué rol desea cambiarlo?")
        print("1. Usuario Estándar")
        print("2. Administrador")
        
        opcion = input("\nSeleccione una opción (1-2): ").strip()
        
        if opcion not in ['1', '2']:
            print("\n❌ Opción no válida.")
            pausar()
            return
            
        nuevo_rol = "Usuario Estándar" if opcion == '1' else "Administrador"
        
        # Si el usuario ya tiene el rol seleccionado
        if (opcion == '1' and not usuario.es_admin()) or (opcion == '2' and usuario.es_admin()):
            print(f"\n⚠️ El usuario ya es {nuevo_rol}.")
            pausar()
            return
            
        # Confirmar cambio
        confirmacion = input(f"\n¿Está seguro de cambiar el rol de '{nombre_usuario}' a {nuevo_rol}? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("\n❌ Operación cancelada.")
            pausar()
            return
            
        # Crear nuevo usuario con el rol seleccionado
        perfil = usuario.perfil
        if opcion == '1':
            nuevo_usuario = UsuarioEstandar(nombre_usuario, perfil.nombre, perfil.apellido, 
                                          usuario.contrasena, perfil.email, perfil.telefono, 
                                          perfil.direccion, perfil_id=perfil.id_perfil)
        else:
            nuevo_usuario = Admin(nombre_usuario, perfil.nombre, perfil.apellido, 
                                usuario.contrasena, perfil.email, perfil.telefono, 
                                perfil.direccion, perfil_id=perfil.id_perfil)
        
        # Reemplazar usuario existente
        self.sistema.usuarios[nombre_usuario] = nuevo_usuario
        
        print(f"\n✅ Rol de '{nombre_usuario}' cambiado exitosamente a {nuevo_rol}.")
        pausar()
    
    def eliminar_usuario(self):
        """Elimina un usuario del sistema"""
        self.mostrar_encabezado("❌ ELIMINAR USUARIO")
        
        nombre_usuario = input("Usuario a eliminar: ").strip()
        
        if nombre_usuario not in self.sistema.usuarios:
            print("\n❌ Usuario no encontrado.")
            pausar()
            return
            
        usuario = self.sistema.usuarios[nombre_usuario]
        
        # Verificar si es el único administrador
        if usuario.es_admin():
            admins = [u for u in self.sistema.usuarios.values() if u.es_admin()]
            if len(admins) == 1:
                print("\n❌ No se puede eliminar el único administrador del sistema.")
                pausar()
                return
        
        confirmacion = input(f"\n¿Está seguro de eliminar al usuario '{nombre_usuario}'? (s/n): ").strip().lower()
        if confirmacion == 's':
            del self.sistema.usuarios[nombre_usuario]
            print(f"\n✅ Usuario '{nombre_usuario}' eliminado exitosamente.")
        else:
            print("\n❌ Operación cancelada.")
        
        pausar()
    
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
        
        # Información de actividad reciente (simulada)
        print("\n📋 ACTIVIDAD RECIENTE:")
        print("   • Último inicio de sesión: Hace 5 minutos")
        print("   • Última modificación: Hace 10 minutos")
        print("   • Estado del sistema: Activo")
        
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

    def configuracion_sistema(self):
        """Muestra y permite modificar la configuración del sistema"""
        while True:
            self.mostrar_encabezado("⚙️ CONFIGURACIÓN DEL SISTEMA")
            
            print("1. Cambiar contraseña de administrador")
            print("2. Ver políticas de contraseñas")
            print("3. Configurar notificaciones")
            print("4. Volver al menú principal")
            print()
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                self.cambiar_contrasena_admin()
            elif opcion == "2":
                self.mostrar_politicas_contrasena()
            elif opcion == "3":
                self.configurar_notificaciones()
            elif opcion == "4":
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def cambiar_contrasena_admin(self):
        """Permite cambiar la contraseña del administrador actual"""
        self.mostrar_encabezado("🔐 CAMBIAR CONTRASEÑA")
        
        contrasena_actual = input("Contraseña actual: ").strip()
        if self.sistema.usuario_actual.verificar_contrasena(contrasena_actual):
            while True:
                nueva_contrasena = input("Nueva contraseña: ").strip()
                es_valida, mensaje = validar_contrasena(nueva_contrasena)
                if es_valida:
                    confirmar = input("Confirmar nueva contraseña: ").strip()
                    if nueva_contrasena == confirmar:
                        self.sistema.usuario_actual.contrasena = nueva_contrasena
                        print("\n✅ Contraseña actualizada exitosamente.")
                        break
                    else:
                        print("\n❌ Las contraseñas no coinciden.")
                else:
                    print(f"\n❌ {mensaje}")
                    if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                        break
        else:
            print("\n❌ Contraseña actual incorrecta.")
        
        pausar()
    
    def mostrar_politicas_contrasena(self):
        """Muestra las políticas de contraseñas del sistema"""
        self.mostrar_encabezado("📝 POLÍTICAS DE CONTRASEÑAS")
        
        print("Requisitos de contraseña:")
        print("   • Longitud mínima: 6 caracteres")
        print("   • Debe contener al menos una letra")
        print("   • Debe contener al menos un número")
        print("   • No se permiten caracteres especiales")
        print("\n💡 Recomendaciones:")
        print("   • Use una contraseña única para este sistema")
        print("   • No comparta su contraseña con nadie")
        print("   • Cambie su contraseña periódicamente")
        
        pausar()
    
    def configurar_notificaciones(self):
        """Permite configurar las notificaciones del sistema"""
        self.mostrar_encabezado("🔔 CONFIGURACIÓN DE NOTIFICACIONES")
        
        print("Estado actual de las notificaciones:")
        print("   • Notificaciones por email: Activadas")
        print("   • Notificaciones de seguridad: Activadas")
        print("   • Reportes semanales: Desactivados")
        print("\n⚠️  Esta funcionalidad está en desarrollo.")
        print("   Las notificaciones se implementarán en una futura versión.")
        
        pausar()
    