class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Encapsulamiento
    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    def mostrar_producto(self):
        print(f"{self.nombre} - Precio: ${self.__precio} - Stock: {self.__stock}")