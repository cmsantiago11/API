#librerias o paquetes
from flask import Flask, request

#clases o funciones
app = Flask(__name__)

#rutas
@app.route('/')
def home():
    return '''
    <H1>Hola, soy Python</H1>
    <p>Esta es una pagina de prueba de Flask y HTML</p> 
    <img width="150" height="120" src="https://img.freepik.com/foto-gratis/hombre-usando-tableta-trabajar-conectarse-otros_23-2149369110.jpg?w=740&t=st=1696384423~exp=1696385023~hmac=364bfef95dc54da9756ce4284f2e4a3c4d25d21192c2b5f523d9e1f7c92be745">
    '''

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f"Hola {nombre}, que bueno que estes aqui!"

@app.route('/saludar/<nombre>,<edad>')
def saludar2(nombre, edad):
    return f"Hola {nombre}, que bueno que estes aqui, en tus {edad}!"

@app.route('/dolares/<pesos>')
def pes2dol(pesos):
    #try:
    dolares = round(float(pesos)/4350,2)
    return f"Tienes {pesos}, que equivalen a {dolares}!"
    #except:
    #    return "Error, el tipo de dato ingresado no es valido"

@app.route('/pesos/<dolares>')
def dol2pes(dolares):
    pesos = round(float(dolares)*4350,2)
    return f"Tienes {dolares}, que equivalen a {pesos}!"

@app.route('/lista_deseos/<string:parametros>')
def deseos(parametros):
    texto1 = request.args.get('deseo1','')
    texto2 = request.args.get('deseo2','')
    texto3 = request.args.get('deseo3','')
    xyz = int(request.args.get('dinero',''))

    return f'''
        Sus deseos son: <br>
        <ol start='1'>
        <li>Deseo 1: {texto1}</li>
        <li>Deseo 2: {texto2}</li>
        <li>Deseo 3: {texto3}</li>
        <li>Y en tu cuenta hay: ${(xyz)*1000} pesos</li>
        </ol>
    '''

#main

if __name__ == '__main__':
    app.run(debug=True, port=5001)