from func_aux import pausar
from menu import Menu

class MenuUsuario(Menu):
    def __init__(self, usuario):
        super().__init__(usuario)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del usuario estándar"""
        while True:
            self.mostrar_encabezado("MENÚ USUARIO")
            
            self.mostrar_opcion(1, "👤", "Ver Mi Perfil Completo")
            self.mostrar_opcion(2, "✏️", "Editar Mi Perfil")
            self.mostrar_opcion(3, "📋", "Mis Actividades")
            self.mostrar_opcion(4, "⚙️", "Configuración Personal")
            self.mostrar_opcion(5, "❓", "Ayuda")
            self.mostrar_opcion(6, "🚪", "Cerrar Sesión")
            
            opcion = self.obtener_opcion(6)
            
            if opcion == '1':
                self.ver_perfil_completo()
            elif opcion == '2':
                self.editar_perfil()
            elif opcion == '3':
                self.ver_actividades()
            elif opcion == '4':
                self.configuracion_personal()
            elif opcion == '5':
                self.mostrar_ayuda()
            elif opcion == '6':
                print(f"\n👋 Hasta luego, {self.usuario.perfil.nombre_completo}!")
                pausar()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def ver_perfil_completo(self):
        """Muestra el perfil completo del usuario"""
        self.mostrar_encabezado("MI PERFIL COMPLETO")
        
        perfil = self.usuario.perfil.obtener_resumen()
        
        print("👤 INFORMACIÓN PERSONAL:")
        print(f"   • Usuario: {self.usuario.username}")
        print(f"   • Nombre completo: {perfil['nombre']}")
        print(f"   • Email: {perfil['email']}")
        print(f"   • Teléfono: {perfil['telefono']}")
        print(f"   • Dirección: {perfil['direccion']}")
        
        print("\n🏷️ INFORMACIÓN DE CUENTA:")
        print(f"   • Tipo de cuenta: {self.usuario.tipo}")
        print(f"   • Fecha de registro: {perfil['fecha_registro']}")
        print(f"   • Último acceso: {perfil['ultimo_acceso']}")
        print(f"   • Total de sesiones: {perfil['total_sesiones']}")
        
        completitud = "✅ Completo" if self.usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
        print(f"   • Estado del perfil: {completitud}")
        
        if not self.usuario.perfil.tiene_datos_completos():
            print("\n💡 Tip: Completa tu perfil para acceder a todas las funcionalidades")
        
        print()
        pausar()
    
    def editar_perfil(self):
        """Permite editar el perfil del usuario"""
        self.mostrar_encabezado("EDITAR MI PERFIL")
        
        print("¿Qué información deseas actualizar?")
        print()
        self.mostrar_opcion(1, "📧", "Email")
        self.mostrar_opcion(2, "📞", "Teléfono")
        self.mostrar_opcion(3, "🏠", "Dirección")
        self.mostrar_opcion(4, "🔙", "Volver")
        
        opcion = self.obtener_opcion(4)
        
        if opcion == '1':
            nuevo_email = input("Nuevo email: ").strip()
            if nuevo_email:
                self.usuario.perfil.actualizar_email(nuevo_email)
                print(f"✅ Email actualizado a: {nuevo_email}")
            else:
                print("❌ Email no válido")
        
        elif opcion == '2':
            nuevo_telefono = input("Nuevo teléfono: ").strip()
            if nuevo_telefono:
                self.usuario.perfil.actualizar_telefono(nuevo_telefono)
                print(f"✅ Teléfono actualizado a: {nuevo_telefono}")
        
        elif opcion == '3':
            nueva_direccion = input("Nueva dirección: ").strip()
            if nueva_direccion:
                self.usuario.perfil.actualizar_direccion(nueva_direccion)
                print(f"✅ Dirección actualizada a: {nueva_direccion}")
        
        if opcion in ['1', '2', '3']:
            print("\n💾 Cambios guardados exitosamente")
        
        pausar()
    
    def ver_actividades(self):
        """Muestra las actividades del usuario"""
        self.mostrar_encabezado("MIS ACTIVIDADES")
        
        perfil = self.usuario.perfil.obtener_resumen()
        
        print("📋 ACTIVIDADES RECIENTES:")
        print("   • Inicio de sesión exitoso")
        print("   • Acceso al perfil personal")
        print("   • Navegación por el menú principal")
        if hasattr(self, '_perfil_editado'):
            print("   • Perfil actualizado")
        
        print(f"\n📊 ESTADÍSTICAS PERSONALES:")
        print(f"   • Sesiones totales: {perfil['total_sesiones']}")
        print(f"   • Última sesión: {perfil['ultimo_acceso']}")
        print(f"   • Miembro desde: {perfil['fecha_registro']}")
        
        completitud = "✅ Completo" if self.usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
        print(f"   • Estado del perfil: {completitud}")
        print()
        
        pausar()
    
    def configuracion_personal(self):
        """Configuración personal del usuario"""
        self.mostrar_encabezado("CONFIGURACIÓN PERSONAL")
        
        print("⚙️ OPCIONES DISPONIBLES:")
        print("   • Cambiar contraseña: Disponible")
        print("   • Actualizar información: Disponible")
        print("   • Configurar notificaciones: Disponible")
        print("   • Tema de interfaz: Clásico")
        print()
        print("ℹ️  Para realizar cambios, contacta al administrador.")
        print()
        
        pausar()
    
    def mostrar_ayuda(self):
        """Muestra la ayuda del sistema"""
        self.mostrar_encabezado("AYUDA")
        
        print("❓ PREGUNTAS FRECUENTES:")
        print()
        print("¿Cómo cambio mi contraseña?")
        print("   → Contacta al administrador del sistema")
        print()
        print("¿Cómo actualizo mi información?")
        print("   → Ve a Configuración Personal")
        print()
        print("¿Olvidé mi contraseña?")
        print("   → Contacta al administrador para restablecerla")
        print()
        print("📧 Contacto: admin@sistema.com")
        print()
        
        pausar()