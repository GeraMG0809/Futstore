

class Product:
    def __init__(self,datos: tuple) -> None:
        self.Id = datos[0]
        self.Modelo = datos[1]
        self.Marca = datos[2]
        self.Precio = datos[3]
        self.Talla = datos[4]
        self.Imagen = datos[5]
        self.Estado = datos[6]  
    