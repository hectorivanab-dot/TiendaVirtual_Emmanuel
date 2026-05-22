from clases.producto import Producto
from clases.carrito import Carrito
from clases.usuario import Cliente

# Crear productos
producto1 = Producto("Arroz", 5000, 10)
producto2 = Producto("Leche", 3500, 20)

# Crear carrito
carrito = Carrito()

# Agregar productos
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

# Mostrar carrito
print("=== TIENDA VIRTUAL ===")
carrito.mostrar_carrito()

# Mostrar total
print(f"Total: ${carrito.calcular_total()}")

print("Factura generada correctamente")