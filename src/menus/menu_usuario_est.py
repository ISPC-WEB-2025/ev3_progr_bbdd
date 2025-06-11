from .menu import MenuBase
from src.utils.func_aux import pausar, limpiar_pantalla

class MenuUsuario(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.usuario = sistema.usuario_actual
        if not self.usuario:
            raise ValueError("No hay un usuario activo. Por favor, inicie sesión primero.")
    
    def mostrar_menu(self):
        """Muestra el menú para usuarios estándar"""
        while True:
            self.mostrar_encabezado("👤 MENÚ USUARIO")
            print("1. Ver mi perfil")
            print("2. Editar mi perfil")
            print("3. Cerrar sesión")
            print()
            
            opcion = input("Seleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                self.mostrar_perfil_usuario()
            elif opcion == "2":
                self.editar_perfil()
            elif opcion == "3":
                self.sistema.cerrar_sesion()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()
    
    def mostrar_perfil_usuario(self):
        """Muestra el perfil del usuario actual"""
        self.mostrar_encabezado("👤 MI PERFIL")
        
        usuario = self.sistema.usuario_actual
        print(f"Usuario: {usuario.nombre_usuario}")
        print(f"Nombre: {usuario.perfil.nombre_completo}")
        print(f"Email: {usuario.perfil.email}")
        print(f"Teléfono: {usuario.perfil.telefono}")
        print(f"Dirección: {usuario.perfil.direccion}")
        
        pausar()
    
    # def mostrar_menu_principal(self):
    #     """Muestra el menú principal del usuario estándar"""
    #     while True:
    #         self.mostrar_encabezado("MENÚ USUARIO")
            
    #         self.mostrar_opcion(1, "👤", "Ver Mi Perfil Completo")
    #         self.mostrar_opcion(2, "✏️", "Editar Mi Perfil")
    #         self.mostrar_opcion(3, "📋", "Mis Actividades")
    #         self.mostrar_opcion(4, "⚙️", "Configuración Personal")
    #         self.mostrar_opcion(5, "❓", "Ayuda")
    #         self.mostrar_opcion(6, "🚪", "Cerrar Sesión")
            
    #         opcion = self.obtener_opcion(6)
            
    #         if opcion == '1':
    #             self.ver_perfil_completo()
    #         elif opcion == '2':
    #             self.editar_perfil()
    #         elif opcion == '3':
    #             self.ver_actividades()
    #         elif opcion == '4':
    #             self.configuracion_personal()
    #         elif opcion == '5':
    #             self.mostrar_ayuda()
    #         elif opcion == '6':
    #             print(f"\n👋 Hasta luego, {self.usuario.perfil.nombre_completo}!")
    #             pausar()
    #             break
    #         else:
    #             print("\n❌ Opción no válida.")
    #             pausar()
    
    def ver_perfil_completo(self):
        """Muestra el perfil completo del usuario"""
        self.mostrar_encabezado("MI PERFIL COMPLETO")
        
        perfil = self.usuario.perfil.obtener_resumen()
        
        print("👤 INFORMACIÓN PERSONAL:")
        print(f"   • Usuario: {self.usuario.nombre_usuario}")
        print(f"   • Nombre completo: {perfil['nombre']}")
        print(f"   • Email: {perfil['email']}")
        print(f"   • Teléfono: {perfil['telefono']}")
        print(f"   • Dirección: {perfil['direccion']}")
        
        print("\n🏷️ INFORMACIÓN DE CUENTA:")
        print(f"   • Tipo de cuenta: {self.usuario.tipo}")
        print(f"   • Fecha de registro: {perfil['fecha_registro']}")
        print(f"   • Último acceso: {perfil['ultimo_acceso']}")
        print(f"   • Total de sesiones: {perfil['total_sesiones']}")
        
        perfil_completo = "✅ Completo" if self.usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
        print(f"   • Estado del perfil: {perfil_completo}")
        
        if not self.usuario.perfil.tiene_datos_completos():
            print("\n💡 Tip: Completa tu perfil para acceder a todas las funcionalidades")
        
        print()
        pausar()
    
    def editar_perfil(self):
        """Permite editar el perfil del usuario"""
        usuario = self.sistema.usuario_actual
        
        while True:
            #limpiar_pantalla()            
            self._perfil_editado = False  
            self.mostrar_encabezado("EDITAR MI PERFIL")

            print("¿Qué información deseas actualizar?")
            print()
            # Muestro datos actuales y opciones de edición
            self.mostrar_opcion(1, "📧", f"Email: [{usuario.perfil.email}]")
            self.mostrar_opcion(2, "📞", f"Teléfono: [{usuario.perfil.telefono}]")
            self.mostrar_opcion(3, "🏠", f"Dirección: [{usuario.perfil.direccion}]")
            self.mostrar_opcion(4, "🔙", "Volver")
            
            opcion = self.obtener_opcion(4)
            
            if opcion == '1':
                nuevo_email = input("Nuevo email: ").strip()
                if nuevo_email:
                    usuario.perfil.email = nuevo_email
                    print(f"✅ Email actualizado a: {nuevo_email}")
                    self._perfil_editado = True
                else:
                    print("❌ No se actualizó el Email")
            
            elif opcion == '2':
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                if nuevo_telefono:
                    usuario.perfil.telefono = nuevo_telefono
                    print(f"✅ Teléfono actualizado a: {nuevo_telefono}")
                    self._perfil_editado = True
                else:
                    print("❌ No se actualizó el Teléfono")

            elif opcion == '3':
                nueva_direccion = input("Nueva dirección: ").strip()
                if nueva_direccion:
                    usuario.perfil.direccion = nueva_direccion
                    print(f"✅ Dirección actualizada a: {nueva_direccion}")
                    self._perfil_editado = True
            
            elif opcion == '4':
                print("\n🔙 Volviendo al menú principal...")
                #pausar()
                return

            if self._perfil_editado == True:
                # Marcar que el perfil ha sido editado
                print("\n💾 Cambios guardados exitosamente")
            
            #pausar()
            

    # Métodos comentados para evitar confusiones, ya que no se usan en el menú actual.

    # def ver_actividades(self):
    #     """Muestra las actividades del usuario"""
    #     self.mostrar_encabezado("MIS ACTIVIDADES")
        
    #     perfil = self.usuario.perfil.obtener_resumen()
        
    #     print("📋 ACTIVIDADES RECIENTES:")
    #     print("   • Inicio de sesión exitoso")
    #     print("   • Acceso al perfil personal")
    #     print("   • Navegación por el menú principal")
    #     if hasattr(self, '_perfil_editado'):
    #         print("   • Perfil actualizado")
        
    #     print(f"\n📊 ESTADÍSTICAS PERSONALES:")
    #     print(f"   • Sesiones totales: {perfil['total_sesiones']}")
    #     print(f"   • Última sesión: {perfil['ultimo_acceso']}")
    #     print(f"   • Miembro desde: {perfil['fecha_registro']}")
        
    #     completitud = "✅ Completo" if self.usuario.perfil.tiene_datos_completos() else "⚠️ Incompleto"
    #     print(f"   • Estado del perfil: {completitud}")
    #     print()
        
    #     pausar()
    
    # def configuracion_personal(self):
    #     """Configuración personal del usuario"""
    #     self.mostrar_encabezado("CONFIGURACIÓN PERSONAL")
        
    #     print("⚙️ OPCIONES DISPONIBLES:")
    #     print("   • Cambiar contraseña: Disponible")
    #     print("   • Actualizar información: Disponible")
    #     print("   • Configurar notificaciones: Disponible")
    #     print("   • Tema de interfaz: Clásico")
    #     print()
    #     print("ℹ️  Para realizar cambios, contacta al administrador.")
    #     print()
        
    #     pausar()
    
    # def mostrar_ayuda(self):
    #     """Muestra la ayuda del sistema"""
    #     self.mostrar_encabezado("AYUDA")
        
    #     print("❓ PREGUNTAS FRECUENTES:")
    #     print()
    #     print("¿Cómo cambio mi contraseña?")
    #     print("   → Contacta al administrador del sistema")
    #     print()
    #     print("¿Cómo actualizo mi información?")
    #     print("   → Ve a Configuración Personal")
    #     print()
    #     print("¿Olvidé mi contraseña?")
    #     print("   → Contacta al administrador para restablecerla")
    #     print()
    #     print("📧 Contacto: admin@sistema.com")
    #     print()
        
    #     pausar()