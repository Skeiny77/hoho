import os
from flask import Flask, request,render_template, jsonify
from form import Login
import database
import traceback

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        form = Login()
        return render_template('login.html', form=form)
    else:
        usu = request.form['usuario']
        con = request.form['contrasena']
        resultado = database.sql_login(usu, con)
        return jsonify({"datos":resultado})

@app.route('/js', methods=['GET','POST'])
def js():
    if request.method == 'GET':
        try:
            usuarios = database.sql_inyeccion_javascript()
        except:
            print(traceback.print_exc())
        return usuarios[0]
