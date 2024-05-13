"""
    Este es el archivo principal de la aplicación, recuerden no compartir datos sensibles en este apartado, recomiendo usar .env en todo momento.
"""

from flask import Flask, session, render_template,request,flash, redirect,url_for,send_from_directory
from Helpers.User import *
from Helpers.Product import *
from Helpers.Class.user_class import *
from Helpers.cart import *
from Helpers.order import *

import os

if __name__ == '__main__':

    app = Flask(__name__,static_folder='static')
    app.secret_key = "YOUR_SECRET_KEY"

    """
        El parámetro de host en 0.0.0.0 hará que puedan ver el render de las rutas de la
        página desde la ip de su máquina, pueden probarlo con su celular u otra máquina
        siempre que esten conectados en la misma red.

        También recuersen hacerlo usando https y no http.

        Ejemplo: https://192.168.100.10:5050

        Si quieren cambiar el protocolo de https a http, solo quiten ssl_context como parámetro.
    """

    @app.route('/static/<path:filename>')
    def serve_static(filename):
        return send_from_directory(app.static_folder, filename)

    # Ruta para la página principal
    @app.route('/')
    def index():
        user = session.get('user')
        Product = select_products()
       
    
        return render_template('index.html',user = user, Product = Product)

    @app.route('/add_product_cart/<int:id>', methods=['POST'] )
    def add_product_cart(id):
        user = session.get('user')['id']
        if request.method == 'POST':
            cantidad = request.form['cantidad']
        
        add_product(user,id,cantidad)

        return redirect(url_for('index'))
    

    @app.route('/my_cart')
    def my_cart():
        user = session.get('user')
        id = session.get('user')['id']
        articulos = get_cart(id)
        subtotal = get_subtotal(id)

        return render_template('my_cart.html', user = user, articulos = articulos, subtotal = subtotal)

    @app.route('/remove_product_cart/<int:id>',methods = ['POST'])
    def remove_product_cart(id):
        user_id = session.get('user')['id']
        remove_carr(user_id,id)

        return redirect(url_for('my_cart'))
    
    @app.route('/update_shopping_cart', methods=['POST'])
    def update_shopping_cart():
        user = session.get('user')
        articulos = get_cart(user['id'])
        subtotal = get_subtotal(user['id'])

        if request.method == 'POST':
            envio = request.form['envio']
            if envio == 'estandar':
                costo = 160.0
            elif envio == 'expres':
                costo = 260.0
            else:
                costo = 0.0

            total = subtotal + costo

        return render_template('my_cart.html', user = user,articulos=articulos, costo=costo,subtotal = subtotal, total = total)

    @app.route('/show_order')
    def show_order():
        user = session.get('user')
        user_id = session.get('user')['id']
        print(user_id)
        print(get_orders(user_id))
        
        return redirect(url_for('index')) 


    @app.route('/my_orders')
    def my_orders():
        user = session.get('user')
        user_id = session.get('user')['id']
        orders = get_orders(user_id)
        print(orders)

        return render_template('my_orders.html', user = user, orders = orders)


    @app.route('/pago')
    def pago():
        user = session.get('user')['id']
        new_order(user)
        clear_carr(user)

        return redirect(url_for('index'))




    @app.route('/pay')
    def pay():

        return render_template('pay.html')

    @app.route('/product_detail/<int:id>')
    def product_detail(id):
        user = session.get('user')
        product = select_product_id(id)
        
        return render_template('product_detail.html',user = user, product = product)
    
    @app.route('/section_detail/<string:league>')
    def section_detail(league:str):
        user = session.get('user')
        Product = select_league(league) 

        return render_template('section_detail.html',user = user, Product = Product)
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

        
            if not new_user(name, username, email, password):
                flash('Error')
                return redirect('/register')
            return redirect('/login')
        else:
            return render_template('register.html')


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = select_user(username)  

            if user and user.password == password:
                session['user'] = user.to_dict()
                return redirect('/')
            else:

                error = 'Correo electrónico o contraseña inválidos'

        return render_template('login.html', error=error)
 
    @app.route('/logout')
    def logout():
        session.pop ('user',None)
        return redirect(url_for('index'))


    try:
        app.run(host = '0.0.0.0', port = 5050, debug = True)
    except KeyboardInterrupt:
        session.pop('user', None)