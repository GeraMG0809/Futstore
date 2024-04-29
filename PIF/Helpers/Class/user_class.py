
class User:
    def __init__(self, datos:tuple) -> None:
        self.id = datos[0]
        self.name = datos[1]
        self.user = datos[2]
        self.email = datos[3]
        self.password = datos[4]

