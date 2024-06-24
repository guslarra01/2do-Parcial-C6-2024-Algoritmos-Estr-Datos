class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = 0

    def sumar_puntos(self, puntos):
        self.puntaje += puntos

    def restar_puntos(self, puntos):
        self.puntaje -= puntos

comprador1 = Comprador("Theo", "Unab 2024", "24062024", "01/01/2015")
print(comprador1.nombre)
print(comprador1.puntaje)

comprador1.sumar_puntos(20)
print(comprador1.puntaje)

comprador1.restar_puntos(10)
print(comprador1.puntaje)
