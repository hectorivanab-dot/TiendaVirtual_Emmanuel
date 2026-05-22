class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def mostrar_carrito(self):
        print("\nProductos en el carrito:")

        for producto in self.items:
            print(f"- {producto.nombre}: ${producto.obtener_precio()}")

    def calcular_total(self):
        total = 0

        for producto in self.items:
            total += producto.obtener_precio()

        return total

    def vaciar_carrito(self):
        self.items.clear()
        print("Carrito vaciado.")

    def eliminar_producto(self, producto):
        self.items.remove(producto)       