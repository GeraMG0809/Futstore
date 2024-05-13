
class Order:
    def __init__(self,datos :tuple) -> None:
        self.Id = datos[0]
        self.Id_venta = datos[1]
        self.Id_producto = datos[2]
        self.Cantidad = datos[3]


    def to_dict(self):
        return{'Id': self.Id,
               'Id_venta': self.Id_venta,
               'Id_producto':self.Id_producto,
               'Cantidad': self.Cantidad}


    def from_dict(cls,data):
        return cls(data['Id'],
                   data['Id_venta'],
                   data['Id_producto'],
                   data['Cantidad'])