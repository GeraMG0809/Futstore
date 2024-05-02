

class Cart:
    def __init__(self,datos: tuple) -> None:
        self.id = datos[0]
        self.id_usuario = datos[1]
        self.id_producto = datos[2]
        self.cantidad = datos[3]


    def to_dict(self):
        return{'Id':self.id,
               'id_usuario':self.id_usuario,
               'id_producto':self.id_producto,
               'cantidad':self.cantidad}
    
    def from_dict(cls,data):
        return cls(data['id'],
                   data['id_usuario'],
                   data['id_producto'],
                   data['cantidad'])