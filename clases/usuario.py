class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_usuario(self):
        print(f"Usuario: {self.nombre}")


# Herencia
class Cliente(Usuario):
    def comprar(self):
        print(f"{self.nombre} está realizando una compra.")


class Administrador(Usuario):
    def administrar(self):
        print(f"{self.nombre} está administrando la tienda.")