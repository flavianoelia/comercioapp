from comercio import *


#test si la listas estan vacias
producto = Comercio()
assert producto.contar_producto() == 0

producto = Comercio()
assert producto.contar_proveedor() == 0

producto = Comercio()
assert producto.contar_venta() == 0

def test_comercio():
    # Crear instancia de Comercio
    comercio = Comercio()
    
    # Pruebas para agregar productos
    comercio.agregar_producto("Laptop", "Marca1", 800.0, 1200.0, 10)
    assert comercio.contar_producto() == 1

    comercio.agregar_producto("Teléfono", "Marca2", 300.0, 500.0, 20)
    assert comercio.contar_producto() == 2

    # Pruebas para eliminar productos
    comercio.eliminiar_producto("Laptop")
    assert comercio.contar_producto() == 1

    # Pruebas para buscar productos
    producto_info = comercio.buscar_producto("Teléfono")
    assert producto_info == (500.0, "Marca2", 20, 300.0, "Teléfono")

    # Pruebas para modificar productos
    comercio.modificar_producto("Teléfono", "NuevoTeléfono", "NuevaMarca", 400.0, 600.0, 25)
    producto_modificado = comercio.buscar_producto("NuevoTeléfono")
    assert producto_modificado == (600.0, "NuevaMarca", 25, 400.0, "NuevoTeléfono")

    # Pruebas para agregar proveedores
    comercio.agregar_proveedor("Proveedor1", 123456789, "Dirección1")
    assert comercio.contar_proveedor() == 1

    comercio.agregar_proveedor("Proveedor2", 987654321, "Dirección2")
    assert comercio.contar_proveedor() == 2

    # Pruebas para eliminar proveedores
    comercio.eliminiar_proveedor("Proveedor1")
    assert comercio.contar_proveedor() == 1

    # Pruebas para agregar ventas
    comercio.agregar_venta(1, 2023, 11, 15, 600.0, 5)
    assert comercio.contar_venta() == 1

    comercio.agregar_venta(2, 2023, 11, 16, 1200.0, 2)
    assert comercio.contar_venta() == 2

    # Pruebas para eliminar ventas
    comercio.eliminiar_venta(1)
    assert comercio.contar_venta() == 1

test_comercio()


    

 