import os
import bcrypt # Importamos la librería bcrypt

def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia de usuario."""
    os.system('cls' if os.name == 'nt' else 'clear')

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

def generar_contrasena_hash(contrasena: str) -> bytes:
    """
    Genera un hash seguro de la contraseña utilizando bcrypt.
    La contraseña debe ser codificada a bytes antes de hashear.
    El hash resultante también es en bytes.
    """
    # bcrypt necesita una 'salt' (sal- cadena de caracteres) generada aleatoriamente.
    # gen_salt() genera una sal segura. El factor de trabajo (rounds) define
    # la dificultad (más alto = más lento = más seguro). 12 es un buen valor por defecto.
    hashed_contra = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt(rounds=12))
    return hashed_contra

def verificar_contrasena_hash(contrasena: str, hashed_contra: bytes) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con un hash bcrypt dado.
    """
    # bcrypt.checkpw toma la contraseña en texto plano (codificada) y el hash almacenado
    # y compara si coinciden.
    return bcrypt.checkpw(contrasena.encode('utf-8'), hashed_contra)