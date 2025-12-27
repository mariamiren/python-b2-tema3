"""
Enunciado:

En este ejercicio, trabajarás con conceptos de programación funcional en Python, específicamente
con funciones lambda y la función map. Tu tarea será realizar una conversión de temperatura de
grados Celsius a Fahrenheit.

Se te proporciona una lista de temperaturas en grados Celsius. Deberás escribir una función lambda
que convierta cada temperatura a grados Fahrenheit. Luego, utilizarás la función map para aplicar
esta conversión a toda la lista. Finalmente, imprimirás ambas listas, la original en Celsius y
la convertida en Fahrenheit, para verificar los resultados.

Instrucciones:
    - Crea una función lambda que convierta temperaturas de Celsius a Fahrenheit. La fórmula para 
    la conversión es: F = (C * 9/5) + 32
    - Utiliza la función filter para seleccionar las temperaturas en Celsius menores a 60, ya que
    los registros mayores a 60 se deben a errores en la medición.
    - Utiliza la función map para aplicar tu función lambda a una lista de temperaturas en Celsius, 
    llamada: temperatures_celsius.
    - La función map te devolverá un objeto map. Convierte este objeto a una lista utilizando la
    función list.


Ejemplo de Salida Esperada:
    Temperatures in Celsius: [0, 10, 20, 35, 45, 60]
    Temperatures in Fahrenheit: [32.0, 50.0, 68.0, 95.0, 113.0, 140.0]
"""

temperatures_celsius = [54, 84, 38, 104, 101, 107, 55, 1, 38, 31, 109, 6, 91, 46, 16, 28, 74, 102, 20, 39]
filter_temperatures_celsius = list(filter(lambda x:))
convert_to_fahrenheit = lambda celsius: 
temperatures_fahrenheit = list(map())

from ej3c1 import convert_to_fahrenheit

def test_convert_to_fahrenheit():
    test_cases = [
        (0, 32),
        (10, 50),
        (20, 68),
        (35, 95),
        (45, 113),
        (60, 140),
    ]
    for celsius, expected in test_cases:
        result = convert_to_fahrenheit(celsius)
        assert result == expected, f"Expected {expected} for {celsius}C, got {result}"

def filter_celsius(temperatures):
    return list(filter(lambda x: x < 60, temperatures))

def filter_celsius():
    test_temperatures = [54, 84, 38, 104, 101, 107, 55, 1, 38, 31, 109, 6, 91, 46, 16, 28, 74, 102, 20, 39
    expected_filtered = [54, 38, 55, 1, 38, 31, 6, 46, 16, 28, 20, 39]
    filtered_temperatures = filter_celsius(test_temperatures)
    assert (
        filtered_temperatures == expected_filtered
    ), f"Expected {expected_filtered}, got {filtered_temperatures}"


# Para probar el código, descomenta las siguientes líneas
# print("Temperatures in Celsius:", temperatures_celsius)
# print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
