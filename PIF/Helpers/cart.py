from Helpers.conecction import *
from Helpers.Class.Product_class import*

def get_cart(id: int):
    futstore = conection()
    carrito : tuple
    producto : tuple
    compra : list = []

    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT Id_producto, Cantidad FROM carrito WHERE Id_usuario_carrito = '{id}'")
        carrito = cursor.fetchall()
        for id_producto in carrito:
            cursor.execute(f"SELECT * FROM jersey WHERE Id_Jersey = '{id_producto[0]}'")
            producto = cursor.fetchone()
            compra.append(Product(producto).to_dict())

    futstore.close()
    return compra

def get_subtotal(id:int):
    futstore = conection()

    subtotal = 0.0
    
    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT Id_producto, Cantidad FROM carrito WHERE Id_usuario_carrito = '{id}'")
        productos = cursor.fetchall()
        for id_producto, cantidad in productos:
            cursor.execute(f"SELECT Precio FROM jersey WHERE Id_Jersey = '{id_producto}'")
            precio = cursor.fetchone()[0]  # Obtiene el precio del producto
            subtotal += precio * cantidad  # Multiplica el precio por la cantidad de productos en el carrito

    futstore.close()
    return subtotal


def add_product(id_user: int, id_product: int,cant: int):
    futstore  = conection()

    carrito : tuple

    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT Id_carrito , Cantidad  FROM carrito WHERE Id_producto = '{id_product}' ")
        carrito = cursor.fetchone()
    
        if carrito: 
            cursor.execute(f"UPDATE carrito SET Cantidad = '{int(carrito[1])+ int(carrito[int(cant)])}'")
        else:
            cursor.execute(f"INSERT INTO carrito (Id_usuario_carrito,Id_producto,Cantidad) VALUES ('{id_user}','{id_product}','{cant}')")

    futstore.commit()
    futstore.close()


def remove_carr(user:int, product:int):
    futstore= conection()

    with futstore.cursor() as cursor:
        cursor.execute(f"DELETE FROM carrito WHERE Id_usuario_carrito = '{user}' AND Id_producto = '{product}'")
    
    futstore.commit()
    futstore.close()


def clear_carr(user:int):
    futstore = conection()

    with futstore.cursor() as cursor:
        cursor.execute(f"DELETE FROM carrito WHERE Id_usuario_carrito = '{user}' ")

    futstore.commit()
    futstore.close()