"""
    Este es el archivo principal de la aplicación, recuerden no compartir datos sensibles en este apartado, recomiendo usar .env en todo momento.
"""

from flask import Flask, session, render_template,request,flash, redirect
from Helpers.User import *
from Helpers.Class.user_class import *
import os

if __name__ == '__main__':

    app = Flask(__name__)
    app.secret_key = "YOUR_SECRET_KEY"

    """
        El parámetro de host en 0.0.0.0 hará que puedan ver el render de las rutas de la
        página desde la ip de su máquina, pueden probarlo con su celular u otra máquina
        siempre que esten conectados en la misma red.

        También recuersen hacerlo usando https y no http.

        Ejemplo: https://192.168.100.10:5050

        Si quieren cambiar el protocolo de https a http, solo quiten ssl_context como parámetro.
    """

    # Ruta para la página principal
    @app.route('/')
    def index():
        username = session.get('username')
        return render_template('index.html',username = username)

    @app.route('/product')
    def product():
        return render_template('product.html')
    
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            print(name)
            print(username)
            print(email)
            print(password)
        
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
                print('logeo exitoso')
                return redirect('/')
            else:

                error = 'Correo electrónico o contraseña inválidos'

        return render_template('login.html', error=error)
 


    try:
        app.run(host = '0.0.0.0', port = 5050, debug = True)
    except KeyboardInterrupt:
        session.pop('user', None)