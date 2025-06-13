from src.utils.func_aux import *
from src.models.usuario_estandar import UsuarioEstandar
from src.models.perfil import Perfil

class MenuBase:
    def __init__(self, sistema):
        self.sistema = sistema
    
    def mostrar_encabezado(self, titulo):
        """Muestra el encabezado del menú"""
        limpiar_pantalla()
        mostrar_titulo(titulo)
        if hasattr(self.sistema, 'usuario_actual') and self.sistema.usuario_actual:
            print(f"Usuario: {self.sistema.usuario_actual.perfil.nombre_completo}")
        print()
    
    def mostrar_opcion(self, numero, emoji, texto):
        """Muestra una opción del menú con formato"""
        print(f"{numero}. {emoji} {texto}")
    
    def obtener_opcion(self, max_opciones):
        """Obtiene y valida la opción seleccionada por el usuario"""
        while True:
            opcion = input(f"\nSeleccione una opción (1-{max_opciones}): ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= max_opciones:
                return opcion
            else:
                print("\n❌ Opción no válida.")
                pausar()
                return None
    
    def _recopilar_datos_perfil(self):
        """
        Método auxiliar para recolectar los datos específicos del perfil.
        Devuelve un diccionario con los datos del perfil.
        """
        datos_perfil = {}
        print("\n📋 DATOS DEL PERFIL")

        # --- Validaciones y Recolección de Datos de Perfil ---
        # Nombre (obligatorio)
        while True:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("\n❌ El nombre es obligatorio.")
                if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    break # Salimos del bucle, nombre queda vacío
                continue
            break
        datos_perfil['nombre'] = nombre

        # Apellido (obligatorio)
        while True:
            apellido = input("Apellido: ").strip()
            if not apellido:
                print("\n❌ El apellido es obligatorio.")
                if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    break
                continue
            break
        datos_perfil['apellido'] = apellido

        # Email (opcional pero con validación de formato)
        while True:
            email = input("Email (opcional): ").strip()
            if not email:
                break
            if '@' not in email or '.' not in email:
                print("\n❌ El formato del email no es válido.")
                print("   Debe ser formato: usuario@dominio.com")
                if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                    break
                continue
            break
        datos_perfil['email'] = email

        datos_perfil['telefono'] = input("Teléfono (opcional): ").strip()
        datos_perfil['direccion'] = input("Dirección (opcional): ").strip()

        return datos_perfil
    

    def _recopilar_datos_nuevo_usuario(self):
        """Recopila los datos necesarios para crear un nuevo usuario"""       
        self.mostrar_encabezado("👤 CREAR NUEVO USUARIO")
        datos_recopilados = {}

        # 1. Solicitar nombre de usuario
        nombre_usuario = None
        while True: # Bucle para asegurar un nombre de usuario único
            nombre_usuario_input = input("Nombre de usuario: ").strip()
            nombre_usuario_normalizado = nombre_usuario_input.lower() # Normalizar para la verificación

            if nombre_usuario_normalizado in self.sistema.usuarios:
                print("\n❌ Este nombre de usuario ya existe. Por favor, elija otro.")
                # No pausar aquí para permitir un nuevo intento inmediato en el bucle
            else:
                break # Nombre de usuario único, salimos del bucle
        nombre_usuario = nombre_usuario_normalizado
        datos_recopilados['nombre_usuario'] = nombre_usuario
        print(f"\n✅ Nombre de usuario '{nombre_usuario}' aceptado.")
                
        # 2. Recoger y validar contraseña
        contrasena = None
        while True:
            contrasena = input("Contraseña: ").strip()
            es_valida, mensaje = validar_contrasena(contrasena)
            if es_valida:
                break
            print(f"\n❌ {mensaje}")
            if input("\n¿Desea intentar de nuevo? (s/n): ").lower() != 's':
                return 
        datos_recopilados['contrasena'] = contrasena
        print(f"\n✅ Contraseña aceptada para '{nombre_usuario}'.")
        
        #3. Recoger datos del perfil
        # Preguntar si desea completar el perfil ahora
        datos_perfil = {}
        print("\n¿Desea completar los datos del perfil ahora?")
        print("1. Sí, completar ahora")
        print("2. No, completar más tarde")
            
        opcion = input("\nSeleccione una opción (1-2): ").strip()
        if opcion == "1":
            datos_perfil = self._recopilar_datos_perfil()
        elif opcion == "2":
            print("\n✅ Puede completar el perfil más tarde.")
        else:
            print("\n❌ Opción no válida. No se completará el perfil ahora.")
            pausar()
        datos_recopilados['datos_perfil'] = datos_perfil
        return datos_recopilados
    
    def crear_usuario(self):
        """Permite crear un nuevo usuario estándar, delegando la lógica al sistema."""

        # 1. Recolecta todos los datos usando el método común de MenuBase
        datos = self._recopilar_datos_nuevo_usuario()
        if datos is None: # Si el usuario canceló en algún punto de la recolección
            return False

        # 2. Delega la creación real del usuario al sistema
        
        nuevo_usuario = self.sistema.crear_nuevo_usuario(
            nombre_usuario=datos['nombre_usuario'],
            contrasena=datos['contrasena'],
            datos_perfil=datos['datos_perfil']   # Este menú siempre crea usuarios estándar
        )

        # 3. Muestra el resultado de la operación
        if nuevo_usuario:
            print(f"\n✅ Usuario '{nuevo_usuario.nombre_usuario}' creado exitosamente como Usuario Estándar.")
            # Accede a los datos del perfil a través de nuevo_usuario.perfil
            if nuevo_usuario.perfil.nombre and nuevo_usuario.perfil.apellido:
                print(f"    • Nombre: {nuevo_usuario.perfil.nombre} {nuevo_usuario.perfil.apellido}")
            if nuevo_usuario.perfil.email:
                print(f"    • Email: {nuevo_usuario.perfil.email}")
            if nuevo_usuario.perfil.telefono:
                print(f"    • Teléfono: {nuevo_usuario.perfil.telefono}")
            if nuevo_usuario.perfil.direccion:
                print(f"    • Dirección: {nuevo_usuario.perfil.direccion}")
            print(f"    • ID Perfil: {nuevo_usuario.perfil.id_perfil}")

            if not nuevo_usuario.perfil.tiene_datos_completos():
                print("\n⚠️  El perfil está incompleto. Deberá completar los datos obligatorios para continuar accediendo al sistema.")
            pausar() # Usa pausar() de func_aux
            return True
        else:
            print("\n❌ No se pudo crear el usuario (posiblemente ya existe o hubo un error interno).")
            pausar() # Usa pausar() de func_aux
            return False


class MenuPrincipal(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)    

    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        while True:
            self.mostrar_encabezado("🏢 SISTEMA DE GESTIÓN")
            print("1. Iniciar sesión")
            print("2. Crear nuevo usuario")
            print("3. Ver credenciales de prueba")
            print("4. Salir")
            print()
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                if self.sistema.intentar_login():
                    if self.sistema.usuario_actual.es_admin():
                        # Importamos aquí para evitar importación circular
                        from src.menus.menu_admin import MenuAdmin
                        menu_admin = MenuAdmin(self.sistema)
                        menu_admin.mostrar_menu()
                    else:
                        # Importamos aquí para evitar importación circular
                        from src.menus.menu_usuario_est import MenuUsuario
                        menu_usuario = MenuUsuario(self.sistema)
                        menu_usuario.mostrar_menu()
            elif opcion == "2":
                self.crear_usuario()
            elif opcion == "3":
                self.sistema.mostrar_credenciales_prueba()
            elif opcion == "4":
                print("\n👋 ¡Gracias por usar el sistema!")
                break
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")
                pausar()
    
    
      
        

