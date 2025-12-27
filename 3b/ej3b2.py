"""
Enunciado:
Desarrolla un decorador de clase en Python que se encargue de registrar en un log cada vez
que una función es llamada, mostrando el nombre de la función, los argumentos con los que
se llamó y, opcionalmente, permitiendo desactivar estos logs mediante un parámetro. 

La clase decorador a desarrollar es: 
    - LogMethodCalls:
        Parámetros print_logs (bool): Indica si se deben imprimir los logs de las llamadas a las
        funciones decoradas.
        Métodos:
            - __init__(self, print_logs: bool): Constructor que recibe el parámetro print_logs.
            - __call__(self, func: Callable) -> Callable: Método que recibe una función y devuelve
            una función decorada que registra las llamadas a la función original.
            - __get__(self, instance, cls): Método que devuelve el decorador si se llama desde la
            clase y la función decorada si se llama desde una instancia de la clase.


Funciones existentes:
    - load_csv(filename: str) -> pd.DataFrame: Carga un archivo CSV en un DataFrame de Pandas.
    - load_and_describe_csv(filename: str) -> pd.DataFrame: Carga un archivo CSV en un DataFrame
    de Pandas y devuelve su descripción.

Ejemplo de Uso:
    dataframe = load_csv(filename)
    description = load_and_describe_csv(filename)

Salida esperada:
    INFO:root:Calling load_csv('data/german_credit_data.csv')
    INFO:root:Calling load_and_describe_csv('data/german_credit_data.csv')
"""

from pathlib import Path
import logging
from types import MethodType
from typing import Callable, Any
import pandas as pd
import pytest
from ej3b2 import LogMethodCalls

def simple_function(x, y):
    return x + y

def test_LogMethodCalls_decorates_function():
    decorador = LogMethodCalls(print_logs=True)
    decorated_function = decorador(
        simple_function
    ), #Usa la función de utilidad renonmbrada
    assert (
        decorated_function(2, 3) == 5
    ), "The decorated function should return the result of 2 + 3 even with print_logs=True"

def test_LogMethodCalls_whit_print_logs_false():
    decorator = LogMethodCalls(print_logs=False)
    decorated_function = decorador(
        simple_function
    ) #Usa la funcion de utilidad renombrada
    assert (
        decorated_function(2, 3) == 5
    ), "The decorated function should return the rsult of 2 + 3 even with print_logs=False"


    # Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     path_parent = Path(__file__).parent
#     FILENAME_PATH = path_parent / 'data/german_credit_data.csv'
#     dataframe_credit = load_csv(FILENAME_PATH)
#     print(dataframe_credit.head(1))
#     description = load_and_describe_csv(FILENAME_PATH)
#     print(description)
