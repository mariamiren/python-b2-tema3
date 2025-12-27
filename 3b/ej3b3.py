"""
Enunciado:
Desarrolla una clase en Python que actúe como una fábrica de decoradores para el registro de
logs, diseñada para facilitar el monitoreo de diferentes aspectos de la ejecución de funciones.
Esta clase, llamada DecoratorFactoryLogs, debe ofrecer tres tipos de decoradores: uno para
registrar el inicio y fin de ejecuciones de funciones, otro para detalles de depuración, y un
tercer decorador que permite guardar los registros en un archivo de log personalizado.

Implementación de la Clase DecoratorFactoryLogs:
    - log_decorator: Crea un decorador que registre cuando una función inicia y termina su
    ejecución, incluyendo el nombre de la función, argumentos y valores de los argumentos pasados.
    - debug_log_decorator: Desarrolla un decorador que registre información detallada útil para
    la depuración, incluyendo una representación textual de los argumentos y valores de los kwargs
    pasados a la función.
    - save_log_decorator: Crea un decorador que registre información en un archivo personalizado,
    especificado a través de un parámetro en el decorador. Este decorador debe ser capaz de crear
    y utilizar un logger específico para la función decorada.

Uso de Decoradores:
    - Aplica el Log Decorator a la función creada llamada add(a, b) que suma dos números.
    - Utiliza el Debug Log Decorator en la función subtract(a, b) que resta el segundo número del primero.
    - Emplea el Save Log Decorator en una función multiply(a, b) que multiplica dos números y guarda los
    registros en un archivo de log personalizado.

Ejemplo de Uso:

factory = DecoratorFactoryLogs()
@factory.log_decorator(message="Log Decorator:")
def add(a, b):
    return a + b
    
Salida esperada:
    2021-08-25 12:00:00,000 - INFO - Log Decorator: Starting: add with args: (2, 3), kwargs: {}
    2021-08-25 12:00:00,000 - INFO - Log Decorator: Finishing: add
"""


import logging
from functools import wraps
from typing import Callable, Any
import os
from io import stringIO
from ej3b3 import (
    DecoratorFactoryLogs, 
    log_directory, 
)  #Asegurate de ajustar el import segun tu estructura de proyecto

#Ensuring the directory for logs exists
log_directory = "data/outputs/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

Def test_log_decorator():
    factory = DecoratorFactoryLogs()
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)  #Adjunta el handler antes de la prueba

    @factory.log_decorator(message="Test Log Decorator:")
    def test_function():
        pass

    test_function()

    logger.removeHandler(handler) #Limpieza: remover el handler despues de la prueba
    logs = stream.getvalue()
    assert "Test Log Decorator:" in logs
    assert "Starting: test_function" in logs
    assert "Finishing: test_function" in logs

 def test_debug_log_decorator():
    factory = DecoratorFactoryLogs()

    @factory.debug_log_decorator(message="Test Debug Decorator:")
    def test_function_debug(x):
        return x

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    test_function_debug(10)

    handler.flush()
    logs = stream.getvalue()
    assert "Test Debug Decorator:" in logs
    assert "Executing: test_function_debug" in logs
    assert "10" in logs  #Verifica que el argumento este en los logs
    logger.removeHandler(handler)

 def save_log_decorator():
    factory = DecoratorFactoryLogs()
    custom_log_path = f"{log_directory}/test_custom_log.log"

    @factory.save_log_decorator():
        message="Test Save Log Decorator:", filepath=custom_log_path
    )
    def  function_save(x, y):
         return x + y

    test_function_save(2, 3)

    with open(custom_log_path, "r") as file:
         logs = file.read()

    assert "Test Save Log Decorator: " in logs
    assert "Executing: test_function_save in logs
    assert "2" in logs and "3" in logs  #Verifica que los argumentos esten en los logs
    os.remove(custom_log_path)



# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     print("Addition:", add(2, 3))
#     print("Subtraction:", subtract(10, 5))
#     print("Multiplication:", multiply(2, 4))
#     print("Logs saved in:", log_directory)
