from src.utils.func_aux import pausar

class PerfilUtils:
    @staticmethod
    def mostrar_datos_actuales(perfil):
        """Muestra los datos actuales del perfil"""
        print("\n📋 DATOS ACTUALES:")
        print(f"Nombre: {perfil.nombre}")
        print(f"Apellido: {perfil.apellido}")
        print(f"Email: {perfil.email}")
        print(f"Teléfono: {perfil.telefono}")
        print(f"Dirección: {perfil.direccion}")
    
    @staticmethod
    def mostrar_opciones_edicion(es_admin=False):
        """Muestra las opciones de edición disponibles"""
        print("\n¿Qué datos desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Email")
        print("4. Teléfono")
        print("5. Dirección")
        print("6. Volver")
    
    @staticmethod
    def validar_nombre(nombre):
        """Valida el nombre"""
        if not nombre:
            print("\n❌ El nombre no puede estar vacío.")
            return False
        return True
    
    @staticmethod
    def validar_apellido(apellido):
        """Valida el apellido"""
        if not apellido:
            print("\n❌ El apellido no puede estar vacío.")
            return False
        return True
    
    @staticmethod
    def validar_email(email):
        """Valida el formato del email"""
        if email and ('@' not in email or '.' not in email):
            print("\n❌ El formato del email no es válido.")
            print("   Debe ser formato: usuario@dominio.com")
            return False
        return True
    
    @staticmethod
    def editar_campo(perfil, opcion, es_admin=False):
        """Edita un campo específico del perfil"""
        if opcion == '1':
            nombre = input("\nNuevo nombre: ").strip()
            if not PerfilUtils.validar_nombre(nombre):
                return False
            perfil.nombre = nombre
            print("\n✅ Nombre actualizado exitosamente.")
            
        elif opcion == '2':
            apellido = input("\nNuevo apellido: ").strip()
            if not PerfilUtils.validar_apellido(apellido):
                return False
            perfil.apellido = apellido
            print("\n✅ Apellido actualizado exitosamente.")
            
        elif opcion == '3':
            if not es_admin and perfil.ha_editado_datos_obligatorios:
                print("\n⚠️ Para modificar el email necesitas autorización del administrador.")
                return False
            email = input("\nNuevo email: ").strip()
            if not PerfilUtils.validar_email(email):
                return False
            perfil.email = email
            print("\n✅ Email actualizado exitosamente.")
            
        elif opcion == '4':
            if not es_admin and perfil.ha_editado_datos_obligatorios:
                print("\n⚠️ Para modificar el teléfono necesitas autorización del administrador.")
                return False
            telefono = input("\nNuevo teléfono: ").strip()
            perfil.telefono = telefono
            print("\n✅ Teléfono actualizado exitosamente.")
            
        elif opcion == '5':
            if not es_admin and perfil.ha_editado_datos_obligatorios:
                print("\n⚠️ Para modificar la dirección necesitas autorización del administrador.")
                return False
            direccion = input("\nNueva dirección: ").strip()
            perfil.direccion = direccion
            print("\n✅ Dirección actualizada exitosamente.")
            
        elif opcion == '6':
            return None
        
        else:
            print("\n❌ Opción no válida.")
            return False
        
        return True 