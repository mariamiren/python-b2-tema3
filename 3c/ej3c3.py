"""
Enunciado:

En este ejercicio práctico, aprenderás a utilizar el módulo itertools de Python, enfocándote
en la función product para generar combinaciones de contraseñas. Se te proveerá un conjunto
limitado de caracteres, incluyendo letras mayúsculas, minúsculas, dígitos y símbolos especiales.
Tu objetivo será utilizar estas letras para crear todas las posibles combinaciones de contraseñas
de una longitud específica.

Instrucciones:
    - Define una función generate_passwords() que acepte los siguientes parámetros: conjuntos de 
    caracteres que incluyan letras mayúsculas ('AZ'), letras minúsculas ('xy'), dígitos ('09') y
    símbolos especiales ('@#'), y la longitud deseada de las contraseñas.
    - Dentro de la función, utiliza la función product de itertools para generar todas las posibles 
    combinaciones de estos caracteres, formando contraseñas de la longitud especificada.
    - Convierte cada combinación de caracteres de las contraseñas generadas en una cadena y 
    almacénalas en una lista.
    - Retorna la lista de contraseñas generadas.
    - Fuera de la función, llama a generate_passwords() con los parámetros adecuados y almacena el 
    resultado.
    - Calcula y muestra el número total de contraseñas generadas.
    - Imprime las primeras 10 contraseñas de la lista para verificar tu solución.

Salida esperada:
    Number of passwords generated: 4096
    First 10 passwords generated: ['AAAA', 'AAAB', 'AAAC', 'AAAD', 'AAAx', 'AAAy', 'AAAz',
    'AAA0', 'AAA1', 'AAA2']
"""

import itertools
from typing import List
from ej3c3 import generate_passwords

def test_generate_password_length():
    """
    Test para asegurar que la longitud de las contraseñas generadas es correcta.
    """
    password_length = 4
    password = generate_password(password_length)
    for password in passwords:
        assert len(password) == password_length, "The length of the generated password is incorrect."


def generate_passwords_count():
    """
    Test to verify the number of generate passwords. 
    """
    password_length = 4
    expected_count = (2 + 2 + 2 +2) ** password_length #Cada grupo tioene 2 caracteres, repetido por la longitud de la contraseña
    passwords = generate_passwords(password_legth)
    assert len(passwords) == expected_count, "The number of generated passwords is incorrect."

def generate_passwords_uniqueness():
    """
    Test to ensure that the generate passwords are unique.
    """
    password_length = 4
    passwords = generate_passwords(passwords_length)
    assert len(password) == len(set(passwords)), "The generated password are unique"

def generate_passwords_content():
    """
     Test to ensure that the generate passwords contain only valid characters.
     """
     password_length = 2
     valid_characters = "AZxy09@#"
     passwords = generate_passwords(passwords_length)
     for passwords in passwords:
         assert all(c in valid_characters for c in password), "The generated password contain invalid characters."
    
# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     PASSWORD_LENGHT = 4
#     password_list = generate_passwords(PASSWORD_LENGHT)
#     print(f"Number of passwords generated: {len(password_list)}")
#     print("First 10 passwords generated:", password_list[:10])
