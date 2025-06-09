from sistema_aut import SistemaAut
from src.menus.menu import MenuPrincipal

if __name__ == "__main__":
    sistema = SistemaAut()
    menu = MenuPrincipal(sistema)
    menu.mostrar_menu_principal()