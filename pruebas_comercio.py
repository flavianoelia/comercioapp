import unittest

class TestComercio(unittest.TestCase):
    def setUp(self):
        self.comercio = Comercio()

    def test_agregar_producto(self):
        self.comercio.agregar_producto("Laptop", "Marca1", 800.0, 1200.0, 10)
        self.assertEqual(self.comercio.contar_producto(), 1)

    def test_eliminar_producto(self):
        self.comercio.agregar_producto("Laptop", "Marca1", 800.0, 1200.0, 10)
        self.comercio.eliminiar_producto("Laptop")
        self.assertEqual(self.comercio.contar_producto(), 0)

    def test_buscar_producto(self):
        self.comercio.agregar_producto("Laptop", "Marca1", 800.0, 1200.0, 10)
        producto_info = self.comercio.buscar_producto("Laptop")
        self.assertEqual(producto_info, (1200.0, "Marca1", 10, 800.0, "Laptop"))

    def test_modificar_producto(self):
        self.comercio.agregar_producto("Laptop", "Marca1", 800.0, 1200.0, 10)
        self.comercio.modificar_producto("Laptop", "NuevaLaptop", "NuevaMarca", 1000.0, 1500.0, 15)
        producto_modificado = self.comercio.buscar_producto("NuevaLaptop")
        self.assertEqual(producto_modificado, (1500.0, "NuevaMarca", 15, 1000.0, "NuevaLaptop"))

    def test_contar_proveedor(self):
        self.comercio.agregar_proveedor("Proveedor1", 123456789, "Dirección1")
        self.assertEqual(self.comercio.contar_proveedor(), 1)

    def test_eliminar_proveedor(self):
        self.comercio.agregar_proveedor("Proveedor1", 123456789, "Dirección1")
        self.comercio.eliminiar_proveedor("Proveedor1")
        self.assertEqual(self.comercio.contar_proveedor(), 0)

    def test_agregar_venta(self):
        self.comercio.agregar_venta(1, 2023, 11, 15, 1200.0, 5)
        self.assertEqual(self.comercio.contar_venta(), 1)

    def test_eliminar_venta(self):
        self.comercio.agregar_venta(1, 2023, 11, 15, 1200.0, 5)
        self.comercio.eliminiar_venta(1)
        self.assertEqual(self.comercio.contar_venta(), 0)

if __name__ == '__main__':
    unittest.main
