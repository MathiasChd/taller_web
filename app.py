from unicodedata import name
from flask import Flask, escape, request, render_template, url_for     #Importamos la libreria

app = Flask(__name__)               #Iniciamos la app con el nomnbre

@app.route('/')                     #Definimos que en la ruta de inicio sera aplicada la funcion hola 
def hola():
    return 'Hi Penguins!'

@app.route('/coach')                #Creamos la ruta coach
def hola_coaches():                 #Definicion de la funcion que sera devuelta
    nombre = 'Enma'                 #Inicializamos un dato
    devolver = request.args.get('nombre', nombre)   #Definimos que sera devuelto y renderizado
    return f'Hola,{escape(devolver)} '              #Retornamos al html

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')