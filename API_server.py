#librerias
from flask import Flask, request, jsonify
from baseSQL import *


#clases o funciones
app = Flask(__name__)
bd = BD('DatosPersona')

@app.route('/')
def home():
    return "Aplicar API con datos"


@app.route('/personas', methods=['GET'])
def obtener_personas():
    resultado = bd.consultar_todos()
    return resultado

#main
if __name__ == '__main__':
    app.run(debug=True, port=5001)