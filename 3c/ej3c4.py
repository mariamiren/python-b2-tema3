"""
Descripción:
Implementarás una función que aplica descuentos a precios de productos. Utilizando functools.partial,
crearás dos versiones especializadas de esta función: una para clientes VIP con un descuento del 20%,
y otra para nuevos clientes con un descuento del 10%. Este ejercicio te enseñará cómo simplificar tu
código y hacerlo más reutilizable con partial.

Instrucciones:
    - Crear Función de Descuento: Define apply_discount(), que toma un precio y un porcentaje de descuento,
    retornando el precio después del descuento.
    - Especializar con partial: Usa partial para crear vip_discount y new_customer_discount, preconfigurados 
    on descuentos del 20% y 10% respectivamente.
    - Demostrar su Uso: Calcula y muestra los precios finales para un cliente VIP y un nuevo cliente,
    partiendo de un precio original de 100.

Salida Esperada:
    Original Price: 100
    VIP Price: 80
    New Customer Price: 90
"""


from functools import partial
from ej3c4 import apply_discount


def apply_discount(price: float, discount: float) -> float:
    """Applies a discount to the price and returns the final price."""
    return price - (price * discount / 100)

#Create specilized discount functions
vip_discount = partial(apply_discount, discount=20)
new_customer_discount = partial(apply_discount, discount=10)

def apply_discount():
    #Test the generic discount function
    assert apply_discount(100, 20) == 80
    assert apply_discount(100, 10) == 90
    
def vip_discount():
    #Test the VIP discount
    assert vip_discount(100) == 80
    
def new_customer_discount():
    #Test the new customer discount
    assert new_customer_discount(100) == 90



# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     original_price = 100
#     vip_price = vip_discount(original_price)
#     new_customer_price = new_customer_discount(original_price)

#     print(f"Original Price: {original_price}")
#     print(f"VIP Price: {vip_price}")
#     print(f"New Customer Price: {new_customer_price}")
