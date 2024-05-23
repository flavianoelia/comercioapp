
from comercio import Producto, Proveedor, Venta, Comercio 

def menu():
     # Función que muestra el menú y solicita la opción al usuario
    opcion = 0
    while opcion < 1 or opcion > 10:
        print("--")
        print("(1) Agregar un producto") #comprar nuevo producto
        print("(2) Eliminar un producto")
        print("(3) Dar de alta nuevo proveedor")
        print("(4) Dar de baja proveedor")
        print("(5) Hacer una venta")
        print("(6) Eliminar una venta")
        print("(7) Buscar producto")
        print("(8) Editar producto")
        print("(9) Informacion básica Producto")
        print("(10) Salir")
        print("--")
        opcion = int(input("Elija una opción: "))
        print("--")
    return opcion


def ejecutar(comercio):
     # Función principal que utiliza el menú e interactúa con el usuario
    opcion = 0
    #agregar_producto(self,nombre:str,marca:str,precio_compra:float,precio_venta:float)
    while opcion != 10:
        opcion = menu()
        if opcion == 1:
             # Agregar un nuevo producto
            nombre = input("Nombre: ")
            marca = input("Marca: ")
            precio_compra = input("Precio de costo: ")
            precio_venta = input("Precio de venta: ")
            stock = input("Stock: ")
            comercio.agregar_producto(nombre,marca,precio_compra,precio_venta,stock)
            print("Producto agregado")
        if opcion == 2:
             # Eliminar un producto
            nombre = input("Nombre: ")
            respuesta = comercio.eliminiar_producto(nombre)
            if respuesta != -1:
                print(f"{nombre} ha sido eliminado del comercio.")
            else:
                print(f"{nombre} no se encuentra en el comercio .")
        if opcion == 3:
            # Dar de alta nuevo proveedor
            nombre = input("Nombre: ")
            tel = input("Telefono: ")
            direccion = input("Direccion: ")
            comercio.agregar_proveedor(nombre,tel,direccion)
            print("Proveedor agregado")
        if opcion == 4:
             # Dar de baja proveedor
            nombre = input("Nombre: ")
            respuesta = comercio.eliminiar_proveedor(nombre)
            if respuesta != -1:
                print(f"{nombre} ha sido eliminado del comercio.")
            else:
                print(f"{nombre} no se encuentra en la lista de proveedores.")
        if opcion == 5:
            # Hacer una venta
            n_factura = input("N_Factura: ")
            anio = input("Añio: ")
            mes = input("Mes: ")
            dia = input("Dia: ")
            p_vendido = input("Precio Venta: ")
            cantidad = input("Cantidad: ")
            #monto = p_vendido * cantidad
            comercio.agregar_venta(n_factura,anio,mes,dia,p_vendido, cantidad)
            print("Venta agregado")
        if opcion == 6:
            # Eliminar una venta
            n_factura = input("Numero de Factura: ")
            respuesta = comercio.eliminiar_venta(n_factura)
            if respuesta != -1:
                print(f"{n_factura} ha sido eliminado de las ventas.")
            else:
                print(f"{n_factura} no se encuentra en las ventas.")
        if opcion == 7:
            # Buscar producto
            nombre = input("Nombre: ")
            respuesta = comercio.buscar_producto(nombre)
            if respuesta != -1:
                print(f"El producto {nombre} :  \nStock: ",producto.stock,"\nPrecio de Venta: ",producto.precio_venta,"\nMarca: ",producto.marca)
            else:
                print(f"{nombre} no se encuentra en el comercio.")
        if opcion == 8:
            # Editar producto
            nombre= input("Ingrese el nombre del producto que desea editar: ")
            respuesta = comercio.buscar_producto(nombre)
            if respuesta != -1:
                nuevo_nombre = input("Ingrese los nuevos datos del producto \nNombre: ")
                nuevo_marca=input ("Marca: ")
                nuevo_precio_compra=input ("Precio de Compra: ")
                nuevo_precio_venta=input ("Precio de Venta: ")
                nuevo_stock=input ("Stock: ")
                comercio.modificar_producto(nombre,nuevo_nombre,nuevo_marca,nuevo_precio_compra, nuevo_precio_venta,nuevo_stock)
            else:
                print(f"{nombre} no se encuentra en el Comercio.")     
        if opcion == 9:
            # Información básica Producto
            print("INFORMACION BASICA \n ")
            comercio.imprimir_productos()
   

if __name__ == "__main__":
    # Inicializar el objeto Comercio y ejecutar el programa
    comercio = Comercio()
    ejecutar(comercio)