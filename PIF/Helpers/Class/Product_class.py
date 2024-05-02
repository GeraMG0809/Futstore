

class Product:
    def __init__(self,datos: tuple) -> None:
        self.Id = datos[0]
        self.Modelo = datos[1]
        self.Marca = datos[2]
        self.Precio = datos[3]
        self.Talla = datos[4]
        self.Imagen = datos[5]
        self.Estado = datos[6]  

    def to_dict(self):
        return{'Id': self.Id,
                'Modelo': self.Modelo,
                'Marca': self.Marca,
                'Precio': self.Precio,
                'Talla': self.Talla,
                'Imagen': self.Imagen,
                'Estado': self.Estado}
    
    def from_dict(cls,data):
        return cls(data['Id'],
                   data['Modelo'],
                   data['Marca'],
                   data['Precio'],
                   data['Talla'],
                   data['Imagen'],
                   data['Estado'])
    