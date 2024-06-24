class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = 0 
    
    def sumar_puntos(self, puntos):
        self.puntaje += puntos
    
    def restablecer_puntaje(self):
        self.puntaje = 0

class Articulo:
    def __init__(self, identificador, nombre, descripcion, marca, precio, puntos):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = precio
        self.puntos = puntos if puntos >= 0 else 0  # aseguramos que los puntos no sean negativos
    
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
    
    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def actualizar_puntos(self, nuevos_puntos):
        if nuevos_puntos >= 0:
            self.puntos = nuevos_puntos
        else:
            print("Error: Los puntos no pueden ser negativos.")
    
    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Descripción: {self.descripcion}, " \
               f"Marca: {self.marca}, Precio: ${self.precio}, Puntos: {self.puntos}"
