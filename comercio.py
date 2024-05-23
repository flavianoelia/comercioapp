# Definición de la clase Producto con sus atributos
class Producto:# definimos de la clase Producto y sus atributos 
    def __init__(self,nombre:str,marca:str,precio_compra:float,precio_venta:float,stock:int):
        self.nombre = nombre 
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock

class Proveedor:
    # Definición de la clase Proveedor con sus atributos
    def __init__(self,nombre:str,tel:int,direccion:str):
        self.nombre = nombre
        self.telefono = tel
        self.direccion = direccion
        
        
class Venta:
     # Definición de la clase Venta con sus atributos
    def __init__(self,n_factura:int,anio,mes,dia,p_vendido, cantidad):
        self.n_factura = n_factura
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.p_vendido = p_vendido
        self.cantidad = cantidad
        
       #self.monto = p_vendido * cantidad
        
    """def comprar(self,cantidad): #definimos el metodo comprar para poder utilizar los atributos de la clase 
        self.stock = self.stock + cantidad
       """ 
    """def vender(self,cantidad):
        if self.stock >0:
            self.stock = self.stock - cantidad
        else:
            print ("Esto no es posible")            
 """

class Comercio:
    def __init__(self):
        self.productos = []
        self.proveedores = []
        self.ventas = []
     
    def contar_producto(self):
        # Devuelve la cantidad de proveedores en la lista
        # Devuelve la cantidad de productos en la lista 
        return len(self.productos)
   
    def contar_proveedor(self):
         # Devuelve la cantidad de ventas en la lista
        #se cuenta la lista (assert_comercio) 
        return len(self.proveedores)
       
    def contar_venta(self):
        #se cuenta la lista (assert_comercio) 
        return len(self.ventas)
    
    def agregar_producto(self,nombre:str,marca:str,precio_compra:float,precio_venta:float,stock:int):#definimos el metodo
        # Agrega un producto a la lista de productos
        producto = Producto (nombre, marca,precio_compra, precio_venta,stock)
        self.productos.append(producto)
        
    def eliminiar_producto (self,nombre):
         # Elimina un producto de la lista según el nombre
        for producto in self.productos: #busca el producto en el stock
            if producto.nombre == nombre: #nombre del producto que se desea eliminar
                self.productos.remove(producto)
                return 1
        return -1 #devuelve el numero de productos que se han eliminado
    
    def buscar_producto(self, nombre):
        # Busca un producto en la lista según el nombre
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto.precio_venta, producto.marca, producto.stock, producto.precio_compra,producto.nombre
        return -1
    
    def modificar_producto(self, nombre,nuevo_nombre,nuevo_marca,nuevo_precio_compra, nuevo_precio_venta,nuevo_stock):
        # Modifica los atributos de un producto según el nombre
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.nombre = nuevo_nombre
                producto.marca = nuevo_marca
                producto.precio_compra = nuevo_precio_compra
                producto.precio_venta = nuevo_precio_venta
                producto.stock = nuevo_stock
                
    def imprimir_productos(self):
         # Imprime la información de todos los productos en la lista
        for producto in self.productos:
            print(f"{producto.nombre}: {producto.marca}: {producto.stock}")
        
    def agregar_proveedor (self, nombre,tel,direccion ):#definimos el metodo
                # Agrega un proveedor a la lista de proveedores
        proveedor = Proveedor ( nombre,tel,direccion )
        self.proveedores.append(proveedor)
    def eliminiar_proveedor (self, nombre ):
        # Elimina un proveedor de la lista según el nombre
        for proveedor in self.proveedores:
            if proveedor.nombre == nombre:
                self.proveedores.remove ( proveedor )
                return 1
        return -1
        
        
    def agregar_venta ( self,n_factura,anio,mes,dia,p_vendido, cantidad ):#definimos el metodo
        # Agrega una venta a la lista de ventas
        venta = Venta (n_factura,anio,mes,dia,p_vendido, cantidad )
        self.ventas.append(venta)
        
    def eliminiar_venta (self, n_factura):
         # Elimina una venta de la lista según el número de factura
        for venta in self.ventas:
            if venta.n_factura == n_factura:
                self.ventas.remove ( venta)
                return 1
        return -1