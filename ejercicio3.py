class Articulo:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
        self.siguiente = None 

    def __repr__(self):
        return f"Articulo({self.nombre}, {self.puntos})"
      ss Comprador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.articulos_comprados = []

    def comprar_articulo(self, articulo, cantidad):
        self.articulos_comprados.extend([articulo] * cantidad)
    def puntaje_total(self):
        return sum(articulo.puntos for articulo in self.articulos_comprados)
      def __repr__(self):
        return f"Comprador({self.nombre})"
