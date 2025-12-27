"""
Enunciado:

En este ejercicio, aplicarás conceptos de programación funcional en Python para enriquecer un
conjunto de datos representando libros. Utilizarás funciones lambda y la función map para añadir
un campo nuevo a cada libro que estime el tiempo de lectura basado en el número de páginas. 

Se te proporciona un archivo JSON que contiene una lista de diccionarios. Cada diccionario
representa un libro con los campos title, author y pages. Tu tarea es añadir un campo adicional
a cada libro llamado reading_time. Este campo estará basado en una estimación de 250 palabras por
página y una velocidad de lectura promedio de 200 palabras por minuto.

Instrucciones:
    - Carga los datos del archivo JSON books_data.json para obtener la lista de libros.
    - Crea una función lambda para calcular el tiempo de lectura estimado para cada libro. El tiempo de lectura se calcula con la fórmula: 
    reading_time = round(pages * 250 / 200), donde pages es el número de páginas del libro.
    - Utiliza la función map para aplicar tu función lambda a la lista de libros, añadiendo el campo reading_time a cada diccionario de libro.
    - Guarda el resultado en un nuevo archivo JSON dentro de un directorio llamado output. Asegúrate de crear el directorio si no existe.
    - Imprime los primeros 3 libros de la lista enriquecida para verificar que el campo reading_time ha sido añadido correctamente.

Ejemplo de Salida Esperada:
{'title': 'Book Title 1', 'author': 'Author A', 'pages': 300, 'reading_time': 375}
{'title': 'Book Title 2', 'author': 'Author B', 'pages': 150, 'reading_time': 188}
{'title': 'Book Title 3', 'author': 'Author C', 'pages': 450, 'reading_time': 562}
"""

from pathlib import Path
import json
import os
from typing import Dict, List
import pytest
form ej3c2 import calculate_reading_time

# Prueba para la aplicacion de la funcion lambsa con map
def test books with reading time():
    #Lista de libros de prueba
    books = [
        {"tittle": "Book Title 1", "author": "David Perry", "pages":879},
        {"tittle": "Book Title 2", "author": "Jacqueline Johnson", "pages":657},
        {"tittle": "Book Title 97", "author": "Linda Contreras", "pages":194}
]
books_with_reading_time = list(
    map(lambda book: (**book, "reading_time": calculate_reading_time(book)},
)
assert all(
    "reading_time" in book for book in books_with_reading_time
), "Not all books have a 'reading_time' field."
assert books_with_reading_time[0]["reading_time"] == round(
    (879 * 250) / 200
), "The reading time for the first book is incorrect."
assert books_with_reading_time[1]["reading_time"] == round(
    (657 * 250) / 200
), assert books_with_reading_time[2]["reading_time"] == round(
    (194 * 250) / 200
), "The reading time for the third book is incorrect."
    




# Para probar el código, descomenta las siguientes líneas
# save_directory: str = path / "data/output"
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)

# with open(f"{save_directory}/books_with_reading_time.json", "w") as file:
#     json.dump({"books": books_with_reading_time}, file)

# for book in books_with_reading_time[:3]:
#     print(book)
