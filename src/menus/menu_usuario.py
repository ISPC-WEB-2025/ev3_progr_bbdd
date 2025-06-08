from src.utils.func_aux import pausar
from src.utils.perfil_utils import PerfilUtils
from .menu import MenuBase      

class MenuUsuario(MenuBase):
    def __init__(self, sistema):
        super().__init__(sistema)
    
    def mostrar_menu(self):
        """Muestra el menú para usuarios estándar"""
        while True:
            self.mostrar_encabezado("👤 MENÚ USUARIO")
            
            self.mostrar_opcion(1, "👤", "Ver mi perfil")
            self.mostrar_opcion(2, "✏️", "Editar mi perfil")
            self.mostrar_opcion(3, "🚪", "Cerrar sesión")
            print()
            
            opcion = self.obtener_opcion(3)
            
            if opcion == '1':
                self.ver_mi_perfil()
            elif opcion == '2':
                self.editar_perfil()
            elif opcion == '3':
                self.sistema.cerrar_sesion()
                break
            else:
                print("\n❌ Opción no válida.")
                pausar()

    def editar_perfil(self):
        """Permite al usuario editar su perfil"""
        self.mostrar_encabezado("✏️ EDITAR PERFIL")
        
        usuario = self.sistema.usuario_actual
        perfil = usuario.perfil
        
        # Verificar si ya ha editado sus datos obligatorios
        if perfil.ha_editado_datos_obligatorios:
            print("\n⚠️ Ya has editado tus datos obligatorios una vez.")
            print("Para realizar más cambios, necesitas autorización del administrador.")
            pausar()
            return
        
        # Mostrar datos actuales
        PerfilUtils.mostrar_datos_actuales(perfil)
        
        # Mostrar opciones de edición
        PerfilUtils.mostrar_opciones_edicion()
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        # Editar campo seleccionado
        resultado = PerfilUtils.editar_campo(perfil, opcion)
        
        if resultado is True:
            # Si se editó nombre o apellido, marcar como editado
            if opcion in ['1', '2']:
                perfil.ha_editado_datos_obligatorios = True
        
        pausar() 