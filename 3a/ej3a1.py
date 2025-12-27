"""
Enunciado:
Desarrolla un sistema orientado a objetos en Python que permita gestionar productos de diferentes categorías (Libros,
Electrónicos y Ropa) en un pedido. Cada tipo de producto deberá incluir métodos específicos para describir sus
atributos únicos, así como un mecanismo para ajustar y obtener el precio, asegurando que este no sea negativo. El
diagrama UML de las clases a implementar se encuentra en 'images/UML_ej3a1.png'

Las clases y métodos a implementar son los siguientes:

- Una clase abstracta Product que define la estructura básica de un producto, incluyendo su nombre, precio, y un método
abstracto describe_product() para obtener una descripción del producto.
- Clases concretas Book, Electronic, y Clothing que heredan de Product y sobrescriben el método describe_product() para
incluir detalles específicos de cada tipo de producto, como autor y ISBN para libros, marca y modelo para electrónicos,
y talla y color para ropa.
- Un atributo price con su respectivo getter y setter en la clase Product para obtener y establecer el precio del producto,
con una validación que impide precios negativos.
- Una clase Order que permite agregar productos de cualquier tipo a un pedido y calcular el precio total del pedido.

Ejemplo:
    order = Order()
    order.add_product(Book("The Little Prince", 20, "Antoine de Saint-Exupéry", "978-3-16-148410-0"))

Salida esperada:
- El precio total del pedido.
- Una descripción detallada de cada producto en el pedido, incluyendo su categoría, nombre, detalles específicos (como
autor, marca, talla, etc.), y precio.
"""


from abc import ABC, abstractmethod
from typing import List
import pytest
import ej3a1.py Book, Electronic, Clothing, Order

def test_product_creation():
    book = Book("Test Book", 10.0, "Test Author", "1234567890")
    assert book._name == "Test Book"
    assert book.price == 10.0
    assert book.author == "Test Author"
    assert book.isbn == "1234567890"

def test_product_price_settimg():
    electronic = Electronic("Test Electronic", 100.0, "Test Bramd", "Test Model")
    electronic.price = 150.0
    assert electronic.price == 150.0

def test_product_negative_price_setting():
    clothing = Clothing("Test Clothing", 20.0, "L", "Red")
    with pytest.raises(ValueError):
        clothing.price = -10.0

def test_order_addition_and_total_calculation():
    orden = Order()
    order.add_product(Book("Test Book", 10.0, "Test Author", "1234567890"))
    order.add_product(Electronic("Test Electronic", 100.0, "Test Brand", "Test Model"))
    order.add_product(Clothing("Test Clothing", 20.0, "L", "Red"))
    assert len(order.products) == 3
    assert order.calculate_total() == 130.0

def test_product_description():
    book = Book("Test Book", 10.0, "Test Author", "1234567890")
    description = book.describe_product()
    assert description == "Book: Test Book, Author: Test Author, ISBN:1234567890, Price: $10.0"


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     order = Order()
#     order.add_product(Book("The Little Prince", 20, "Antoine de Saint-Exupéry", "978-3-16-148410-0"))
#     order.add_product(Electronic("Smartphone", 799.99, "Apple", "X1000"))
#     order.add_product(Clothing("T-shirt", 18.99, "M", "Black"))

#     for product in order.products:
#         print(product.describe_product())
#     print(f"{f'Total order price: ${order.calculate_total()}':*^50}")
