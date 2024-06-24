class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = 0  
        self.__articulos_comprados = []  
    
    def sumar_puntos(self, puntos):
        self.puntaje += puntos
    
    def restablecer_puntaje(self):
        self.puntaje = 0
    
    def comprar_articulo(self, articulo):
        articulo.comprar(self)
    
    def agregar_articulo_comprado(self, articulo):
        self.__articulos_comprados.append(articulo)
    
    def listar_articulos_comprados(self):
        print(f"Artículos comprados por {self.nombre}:")
        for articulo in self.__articulos_comprados:
            print(articulo)
        print(f"Total de artículos comprados: {len(self.__articulos_comprados)}")
    
    def encontrar_articulo(self, identificador):
        for articulo in self.__articulos_comprados:
            if articulo.identificador == identificador:
                return True
        return False
    
    def eliminar_articulo(self, identificador):
        eliminados = 0
        for articulo in self.__articulos_comprados[:]:
            if articulo.identificador == identificador:
                self.puntaje -= articulo.puntos
                self.__articulos_comprados.remove(articulo)
                eliminados += 1
        return eliminados
