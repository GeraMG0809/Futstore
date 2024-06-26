from Helpers.conecction import conection
from typing import Union
from Helpers.Class.user_class import *
import hashlib



def truncate(string, length):
    return string[:length]

def new_user(name:str , user_name: str, email:str,password:str) -> bool:
    futstore = conection()

    with futstore.cursor() as cursor: 
        cursor.execute(f"SELECT COUNT(*) FROM Usuario WHERE Correo = '{email}'")
        user = cursor.fetchone()

    if  user != (0,):
        return False
    
    with futstore.cursor() as cursor: 
        cursor.execute(f"SELECT COUNT(*) FROM Usuario WHERE Nombre_usuario = '{user_name}'")
        user = cursor.fetchone()
        
    if  user != (0,):
        return False

    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    hashed_password = truncate(hashed_password, 15)
    
    with futstore.cursor() as cursor:
        cursor.execute("INSERT INTO Usuario(Nombre_cliente, Nombre_usuario, Correo, Contraseña) VALUES (%s, %s, %s, %s)", (name, user_name, email, hashed_password))

    futstore.commit()
    futstore.close()
    return True



def select_user(username: str) -> Union[User, None]:
    futstore = conection()
    user_data: tuple

    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT Id_usuario, Nombre_cliente, Nombre_usuario, Correo, Contraseña FROM Usuario WHERE Nombre_usuario = '{username}'")
        user_data = cursor.fetchone()

    futstore.close()

    if user_data:
        user = User(user_data)
        return user
    else:
        return None


def select_user_id(id:int):
    futstore = conection()

    user:tuple
    with futstore.cursor() as cursor: 
        cursor.execute(f"SELECT Id,Nombre_cliente,Nombre_usuario,Correo FROM Usuario WHERE Id = '{id}'")
        user = cursor.fetchone()

    futstore.close()
    return user

def delete_user(id:int):
    futstore = conection()

    with futstore.cursor() as cursor: 
        cursor.execute(f"UPDATE Usuario SET Estado = 'Inactivo' WHERE Id = '{id}'")
    
    futstore.commit()
    futstore.close()


def select_user_all():
    futstore = conection()

    users : list
    with futstore.cursor() as cursor:
        cursor.execute("SELECT Id,Nombre_cliente, Nombre_usuario,Correo FROM Usuario WHERE Estado = 'Activo' ")
        users = cursor.fetchall()
    
    futstore.close()
    return users