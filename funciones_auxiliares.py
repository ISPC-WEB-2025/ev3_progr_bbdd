import os
import hashlib
from datetime import datetime

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('clear' if os.name == 'posix' else 'cls')

def encriptar_password(password):
    """Encripta la contraseña usando SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def mostrar_titulo(titulo):
    """Muestra un título con formato"""
    print("=" * len(titulo))
    print(titulo)
    print("=" * len(titulo))
    print()

def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("Presiona Enter para continuar...")
