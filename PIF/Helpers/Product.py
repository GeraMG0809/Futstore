from Helpers.conecction import * 
from Helpers.Class.Product_class import*

def select_products():
    futstore = conection()
    products = list

    with futstore.cursor() as cursor:
        cursor.execute('SELECT * FROM jersey')
        products = cursor.fetchall()
    
    productos : list = []
    for product in products:
        productos.append(Product(product).to_dict())

    futstore.close()
    return productos

def select_product_id(id: int):
    futstore = conection()
    product : tuple

    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT * FROM jersey WHERE Id_Jersey = '{id}'")
        product = cursor.fetchone()

    producto : tuple = ()
    producto = (Product(product).to_dict())
    
    futstore.close()
    return producto


def new_product(marca:str,modelo: str,precio: float, talla: int ,imagen:str):
    futstore = conection()


    with futstore.cursor() as cursor:
        cursor.execute("INSERT INTO jersey (Modelo,Marca,Precio,Talla,Imagen) VALUES (%s,%s,%s,%s,%s)", (modelo,marca,precio,talla,imagen))

    futstore.commit()
    futstore.close()

def delete_product(id: str):
    futstore = conection()

    with futstore.cursor() as cursor:
        cursor.execute(f"UPDATE jersery SET Estado = 'Inactivo' WHERE Id_Jersey = '{id}'")
    
    futstore.commit()
    futstore.close()

def select_product_brand(marca :str):
    futstore = conection()

    products = list=[]
    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT * FROM jersey WHERE Marca = '{marca}'")
        products= cursor.fetchall()

    productos_marca = list = []
    for product in products:
        productos_marca.append(Product(product).to_dict())
    
    futstore.close()
    return productos_marca


def select_league(league: str):
    futstore = conection()

    
    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT * FROM jersey WHERE Marca = '{league}'")
        jerseys = cursor.fetchall()

    products = list = []
    for jersey in jerseys:
        products.append(Product(jersey).to_dict())
        

    futstore.close()
    return products