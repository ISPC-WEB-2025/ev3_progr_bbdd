from src.menus.menu import MenuBase
from src.models.usuario_estandar import UsuarioEstandar
from src.models.admin import Admin
from src.utils.func_aux import *
from src.models.perfil import Perfil
from src.utils.perfil_utils import PerfilUtils
# from datetime import datetime

class MenuAdmin(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)
    
    def mostrar_menu(self):
        """Muestra el menú para administradores"""
        while True:
            self.mostrar_encabezado("👑 MENÚ ADMINISTRADOR")
            
            self.mostrar_opcion(1, "👥", "Gestión de Usuarios")
            self.mostrar_opcion(2, "✏️ ", "Editar mi perfil")
            self.mostrar_opcion(3, "⚙️ ", "Configuración del sistema")
            self.mostrar_opcion(4, "🚪", "Cerrar sesión")
            print()
            
            opcion = self.obtener_opcion(4)
            
            if opcion == '1':
                if self.gestionar_usuarios():  # Si retorna True, salir del menú admin
                    return
            elif opcion == '2':
                self.editar_perfil()
            elif opcion == '3':
                self.configuracion_sistema()
            elif opcion == '4':
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

    def gestionar_usuarios(self):
        """Menú de gestión de usuarios"""
        while True:
            self.mostrar_encabezado("👥 GESTIÓN DE USUARIOS")
            
            self.mostrar_opcion(1, "📝", "Ver lista de usuarios")
            self.mostrar_opcion(2, "➕", "Agregar usuario")
            self.mostrar_opcion(3, "🔍", "Ver detalles de usuario")
            self.mostrar_opcion(4, "✏️", " Editar perfil de usuario")
            self.mostrar_opcion(5, "⚙️ ", "Cambiar rol de usuario")
            self.mostrar_opcion(6, "❌", "Eliminar usuario")
            self.mostrar_opcion(7, "🏠", "Volver al menú principal")
            print()
            
            opcion = self.obtener_opcion(7)  # Limita las opciones válidas a 1-7
            
            if opcion == '1':
                self.mostrar_lista_usuarios()
            elif opcion == '2':
                if not self.crear_usuario():  # Si retorna False, continuar en el menú
                    continue
            elif opcion == '3':
                self.ver_detalles_usuario()
            elif opcion == '4':
                self.editar_perfil_usuario()
            elif opcion == '5':
                if self.cambiar_rol_usuario():  # Si admin cambia de rol, debe retornar a menú principal
                    return True  # Indicar que debemos salir del menú admin
            elif opcion == '6':
                if self.eliminar_usuario():  # Si se elimina el usuario actual, debe retornar a menú principal
                    return True  # Indicar que debemos salir del menú admin
            elif opcion == '7':
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
        
        return False  # Si llegamos aquí, continuamos en el menú admin
    
    def obtener_todos_usuarios(self):
        """Obtiene todos los usuarios del sistema"""
        return self.sistema.usuarios
    
    def ver_detalles_usuario(self):
        """Muestra detalles completos de un usuario"""
        self.mostrar_encabezado("🔍 DETALLES DE USUARIO")
        
        nombre_usuario = input("Usuario a consultar: ").strip().lower()
        
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
            
            esta_completo = "✅ Completo" if usuario.perfil.tiene_datos_completos() else "⚠️  Incompleto"
            print(f"   • Estado del perfil: {esta_completo}")
        else:
            print("\n❌ Usuario no encontrado.")
        
        pausar()
    
    # def agregar_usuario(self): 
    # método comentado ya que es redundante con el método usado en el menú inicial
    #  
    #     """Agrega un nuevo usuario al sistema"""
    #     self.mostrar_encabezado("➕ AGREGAR USUARIO")
        
    #     try:
    #         # 1. Solicitar nombre de usuario
    #         while True:
    #             nombre_usuario = input("Nombre de usuario: ").strip()
    #             if not nombre_usuario:
    #                 print("\n❌ El nombre de usuario no puede estar vacío.")
    #                 if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                     return False # Si no desea intentar de nuevo, retorna a menú principal
    #                 continue
    #             if nombre_usuario.lower() in self.sistema.usuarios:
    #                 print("\n❌ El nombre de usuario ya existe.")
    #                 if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                     return False # Si no desea intentar de nuevo, retorna a menú principal
    #                 continue
    #             break
            
    #         # 2. Solicitar y validar contraseña
    #         contrasena = None #inicializamos la contraseña
    #         while True:
    #             contrasena = input("Contraseña: ").strip()
    #             es_valida, mensaje = validar_contrasena(contrasena)
    #             if es_valida:
    #                 #contrasena = encriptar_contrasena(contrasena)
    #                 # Por motivos de seguridad, la contraseña debería ser encriptada antes de guardarla
    #                 break
    #             print(f"\n❌ {mensaje}")
    #             if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                 return False # Si no desea intentar de nuevo, retorna a menú principal
            
    #         # 3. Preguntar si desea completar el perfil ahora
    #         print("\n¿Desea completar los datos del perfil ahora?")
    #         print("1. Sí, completar ahora")
    #         print("2. No, completar más tarde")
            
    #         opcion = input("\nSeleccione una opción (1-2): ").strip()
            
    #         # Valores por defecto para datos opcionales
    #         nombre = ""
    #         apellido = ""
    #         email = ""
    #         telefono = ""
    #         direccion = ""
            
    #         if opcion == '1':
    #             print("\n📋 DATOS DEL PERFIL")
                
    #             # Validar nombre
    #             while True:
    #                 nombre = input("Nombre: ").strip()
    #                 if not nombre:
    #                     print("\n❌ El nombre es obligatorio.")
    #                     if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                         break  # Si no desea intentar de nuevo, continuamos con los datos vacíos
    #                     continue
    #                 break
                
    #             # Validar apellido
    #             while True:
    #                 apellido = input("Apellido: ").strip()
    #                 if not apellido:
    #                     print("\n❌ El apellido es obligatorio.")
    #                     if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                         break  # Si no desea intentar de nuevo, continuamos con los datos vacíos
    #                     continue
    #                 break
                
    #             # Email opcional pero con validación de formato
    #             while True:
    #                 email = input("Email (opcional): ").strip()
    #                 if not email:
    #                     break  # Si no hay email, continuamos
    #                 if '@' not in email or '.' not in email:
    #                     print("\n❌ El formato del email no es válido.")
    #                     print("   Debe ser formato: usuario@dominio.com")
    #                     if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
    #                         break  # Si no desea intentar de nuevo, continuamos con email vacío
    #                     continue
    #                 break
                
    #             # Teléfono y dirección son opcionales
    #             telefono = input("Teléfono (opcional): ").strip()
    #             direccion = input("Dirección (opcional): ").strip()
            
    #         # 5. Crear el perfil del usuario
    #         nuevo_perfil = Perfil(nombre=nombre, 
    #                               apellido=apellido, 
    #                               email=email, 
    #                               telefono=telefono, 
    #                               direccion=direccion)

    #         # 6. Crear el usuario (siempre como estándar)
    #         nuevo_usuario = UsuarioEstandar(nombre_usuario, contrasena, nuevo_perfil)

    #         # 7. Agregar al sistema
    #         self.sistema.usuarios[nombre_usuario.lower()] = nuevo_usuario
            
    #         # 8. Mostrar confirmación
    #         print(f"\n✅ Usuario '{nombre_usuario}' creado exitosamente como Usuario Estándar.")
    #         if nombre and apellido:
    #             print(f"   • Nombre: {nombre} {apellido}")
    #         if email:
    #             print(f"   • Email: {email}")
    #         if telefono:
    #             print(f"   • Teléfono: {telefono}")
    #         if direccion:
    #             print(f"   • Dirección: {direccion}")
    #         print(f"   • ID Perfil: {nuevo_usuario.perfil.id_perfil}")
            
    #         if not nombre or not apellido:
    #             print("\n⚠️  El perfil está incompleto. Deberá completar los datos obligatorios para continuar accediendo al sistema.")
            
    #     except Exception as e:
    #         print(f"\n❌ Error al crear el usuario: {str(e)}")
    #         print("Por favor, intente nuevamente.")
    #         return False 
        
    #     pausar()
    #     return True # Si el usuario se crea correctamente, retorna a menú principal

    def cambiar_rol_usuario(self):
        """Permite cambiar el rol de un usuario entre estándar y administrador"""
        self.mostrar_encabezado("🔄 CAMBIAR ROL DE USUARIO")
        
        nombre_usuario = input("Usuario a modificar: ").strip().lower()
        if nombre_usuario not in self.sistema.usuarios:
            print("\n❌ Usuario no encontrado.")
            pausar()
            return
        
        usuario_a_modificar = self.sistema.usuarios[nombre_usuario]
        rol_actual = "Administrador" if usuario_a_modificar.es_admin() else "Usuario Estándar"
        
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
        if (opcion == '1' and not usuario_a_modificar.es_admin()) or (opcion == '2' and usuario_a_modificar.es_admin()):
            print(f"\n⚠️ El usuario ya es {nuevo_rol}.")
            pausar()
            return
            
        # Confirmar cambio
        confirmacion = input(f"\n¿Está seguro de cambiar el rol de '{nombre_usuario}' a {nuevo_rol}? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("\n❌ Operación cancelada.")
            pausar()
            return
            
        # Verificar si es el único administrador
        if opcion == '1' and usuario_a_modificar.es_admin():
            admins = [u for u in self.sistema.usuarios.values() if u.es_admin()]
            if len(admins) == 1:
                print("\n❌ No se puede cambiar el rol del único administrador del sistema.")
                pausar()
                return
            
        # Crear nuevo usuario con el rol seleccionado
        perfil = usuario_a_modificar.perfil
        if opcion == '1':
            nuevo_usuario = UsuarioEstandar(nombre_usuario, usuario_a_modificar.contrasena, 
                                            usuario_a_modificar.perfil)
        else:
            nuevo_usuario = Admin(nombre_usuario, usuario_a_modificar.contrasena, 
                                    usuario_a_modificar.perfil)

        # Reemplazar usuario existente
        self.sistema.usuarios[nombre_usuario] = nuevo_usuario
        
        # Si el usuario modificado es el administrador actual y se cambió a usuario estándar,
        # cerrar la sesión y volver al menú principal
        if (nombre_usuario == self.sistema.usuario_actual.nombre_usuario.lower() and 
            opcion == '1'):
            print("\n⚠️ Has cambiado tu rol a Usuario Estándar.")
            print("Cerrando sesión...")
            self.sistema.usuario_actual = None  # Borramos el usuario actual
            pausar()
            return True  # True indica que debemos volver al menú principal
        
        print(f"\n✅ Rol de '{nombre_usuario}' cambiado exitosamente a {nuevo_rol}.")
        pausar()
        return False  # False indica que podemos continuar en el menú actual
    
    def eliminar_usuario(self):
        """Elimina un usuario del sistema"""
        self.mostrar_encabezado("❌ ELIMINAR USUARIO")
        
        nombre_usuario = input("Usuario a eliminar: ").strip().lower()
        
        if nombre_usuario not in self.sistema.usuarios:
            print("\n❌ Usuario no encontrado.")
            pausar()
            return False
            
        usuario = self.sistema.usuarios[nombre_usuario]
        
        # Verificar si es el único administrador
        if usuario.es_admin():
            admins = [u for u in self.sistema.usuarios.values() if u.es_admin()]
            if len(admins) == 1:
                print("\n❌ No se puede eliminar el único administrador del sistema.")
                pausar()
                return False
        
        confirmacion = input(f"\n¿Está seguro de eliminar al usuario '{nombre_usuario}'? (s/n): ").strip().lower()
        if confirmacion != 's':
            print("\n❌ Operación cancelada.")
            pausar()
            return False
            
        # Si el usuario a eliminar es el usuario actual
        if nombre_usuario == self.sistema.usuario_actual.nombre_usuario.lower():
            print("\n⚠️ Has eliminado tu propia cuenta.")
            print("Cerrando sesión...")
            del self.sistema.usuarios[nombre_usuario]
            self.sistema.cerrar_sesion()  # Usamos el método cerrar_sesion() en lugar de asignar None directamente
            pausar()
            return True  # True indica que debemos volver al menú principal
        else:
            del self.sistema.usuarios[nombre_usuario]
            print(f"\n✅ Usuario '{nombre_usuario}' eliminado exitosamente.")
            pausar()
            return False
    
    
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
    
    def editar_perfil(self):
        """Permite al administrador editar su perfil"""
        while True:
            self.mostrar_encabezado("✏️  EDITAR PERFIL")
            
            usuario = self.sistema.usuario_actual
            perfil = usuario.perfil
            
            # Mostrar datos actuales
            PerfilUtils.mostrar_datos_actuales(perfil)
            
            # Mostrar opciones de edición
            PerfilUtils.mostrar_opciones_edicion(es_admin=True)
            
            opcion = input("\nSeleccione una opción (1-6): ").strip()
            
            # Editar campo seleccionado
            resultado = PerfilUtils.editar_campo(perfil, opcion, es_admin=True)
            
            # Si el resultado es None, significa que el usuario eligió volver
            if resultado is None:
                break
            
            pausar()
    
    def editar_perfil_usuario(self):
        """Permite al administrador editar el perfil de otro usuario"""
        self.mostrar_encabezado("✏️ EDITAR PERFIL DE USUARIO")
        
        nombre_usuario = input("Usuario a modificar: ").strip().lower()
        if nombre_usuario not in self.sistema.usuarios:
            print("\n❌ Usuario no encontrado.")
            pausar()
            return
        
        usuario = self.sistema.usuarios[nombre_usuario]
        perfil = usuario.perfil
        
        while True:
            self.mostrar_encabezado("✏️ EDITAR PERFIL DE USUARIO")
            print(f"Usuario: {nombre_usuario}")
            
            # Mostrar datos actuales
            PerfilUtils.mostrar_datos_actuales(perfil)
            
            # Mostrar opciones de edición
            PerfilUtils.mostrar_opciones_edicion(es_admin=True)
            
            opcion = input("\nSeleccione una opción (1-6): ").strip()
            
            # Editar campo seleccionado
            resultado = PerfilUtils.editar_campo(perfil, opcion, es_admin=True)
            
            # Si el resultado es None, significa que el usuario eligió volver
            if resultado is None:
                break
            
            pausar()
    