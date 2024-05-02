
class User:
    def __init__(self, datos:tuple) -> None:
        self.id = datos[0]
        self.name = datos[1]
        self.user = datos[2]
        self.email = datos[3]
        self.password = datos[4]

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'user': self.user,
                'email': self.email,
                'password': self.password}
    
    def from_dict(cls,data):
        return cls(data['id'],
                   data['name'],
                   data['user'],
                   data['email'],
                   data['password'])
   
