import os
import hashlib
# from datetime import datetime

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('clear' if os.name == 'posix' else 'cls')

def validar_contrasena(contrasena):
    """
    Valida que la contraseña tenga al menos 6 caracteres, letras y números
    usando funciones de cadena y any().
    """
    if len(contrasena) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."

    tiene_letras = any(c.isalpha() for c in contrasena)
    if not tiene_letras:
        return False, "La contraseña debe contener al menos una letra."

    tiene_numeros = any(c.isdigit() for c in contrasena)
    if not tiene_numeros:
        return False, "La contraseña debe contener al menos un número."

    return True, "Contraseña válida."

# def encriptar_contrasena(contrasena):
#     """Encripta la contraseña usando SHA256"""
#     return hashlib.sha256(contrasena.encode()).hexdigest()

def mostrar_titulo(titulo):
    """Muestra un título centrado con líneas decorativas"""
    ancho = max(len(titulo) + 4, 50)  # Mínimo 50 caracteres de ancho
    print("=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho)
    print()

def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("Presiona Enter para continuar...")
