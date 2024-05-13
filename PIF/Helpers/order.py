from Helpers.conecction import * 
from Helpers.Class.order_class import*


def new_order(id:int):
    futstore = conection()

    productos : tuple


    with futstore.cursor() as cursor:
        cursor.execute(f"INSERT INTO historial_ventas (Id_usuario2) VALUES ('{id}')")
        futstore.commit()

    with futstore.cursor() as cursor:
        cursor.execute(f"SELECT Id_producto , Cantidad  FROM carrito WHERE Id_usuario_carrito = '{id}'")
        productos = cursor.fetchall()


        cursor.execute(f"SELECT Id_venta FROM historial_ventas  WHERE Id_venta = (SELECT MAX(Id_venta) FROM historial_ventas WHERE Id_usuario2 = '{id}')")
        id_venta = cursor.fetchone()[0]

        for product in productos:
            cursor.execute(f"INSERT INTO ordenes (Id_venta2, Id_producto, Cantidad) VALUES ({id_venta}, {product[0]}, {product[1]})")
            futstore.commit()


    futstore.close()


def get_orders(id: int):
    futstore = conection()
    
    sales_id : tuple
    orders : list = []
    orders_data : list= []

    with futstore.cursor() as cursor:   
        cursor.execute(f"SELECT Id_venta FROM historial_ventas WHERE Id_usuario2 = '{id}'")
        sales_id = cursor.fetchall()
        
        for Id in sales_id:
            cursor.execute(f"SELECT * FROM ordenes WHERE Id_venta2 = '{Id[0]}'")   
            orders_data += cursor.fetchall()

        for order_data in orders_data:
            orders.append(Order(order_data).to_dict())
 
    futstore.close()
    return orders
