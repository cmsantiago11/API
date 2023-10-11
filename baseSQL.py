#librerias
import sqlite3

#objetos y funciones
#crear la tabal del motor de bases de datos
def ComandCreateTable():
    comandoSQL = '''
        CREATE TABLE IF NOT EXISTS Personas(
            id integer PRIMARY KEY,
            nombre TEXT,
            peso integer,
            talla float
        )
    '''
    return comandoSQL

class BD():
    def __init__(self, archivo):
        self.conn = sqlite3.connect(f'{archivo}.db',check_same_thread=False)
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.cursor.execute(ComandCreateTable())
        self.conn.commit()

    #Crud -> C create :: insert
    def insertData(self, nombre, peso, talla):
        comando = f'INSERT INTO Personas(nombre, peso, talla) VALUES("{nombre}", {peso}, {talla})'
        #comando = 'INSERT INTO Personas(nombre, peso, talla) VALUES(?,?,?)', (nombre, peso, talla)
        self.cursor.execute(comando)
        self.conn.commit()

    #cRud -> R read :: select
    def consultar_todos(self):
        self.cursor.execute('SELECT * FROM Personas')
        return self.cursor.fetchall()
    
    def consultar_id(self, indice):
        self.cursor.execute(f'SELECT * FROM Personas WHERE id={indice}')
        return self.cursor.fetchone()
    
    def consultar_talla(self, indice):
        self.cursor.execute(f'SELECT * FROM Personas WHERE talla={indice}')
        return self.cursor.fetchall()
    
    #crUd -> U update :: update
    def actualizar(self, id, peso, talla):
        comando = f'UPDATE Personas SET peso={peso}, talla={talla} WHERE id={id}'
        self.cursor.execute(comando)
        self.conn.commit()
    
    #cruD -> D delete :: delete
    def eliminar(self, id):
        comando = f'DELETE FROM Personas WHERE id={id}'
        self.cursor.execute(comando)
        self.conn.commit()

#main

if __name__ == "__main__":
    miBD = BD('DatosPersona')
    #miBD.createTable()

    #miBD.insertData('Edison', 80, 1.72)
    resultado = miBD.consultar_todos()
    print("----- Datos en la base de datos -----")
    for item in resultado:
        print(item)
    
    print("-"*30)
    dato = miBD.consultar_id(1)
    print(dato)
    print("-"*30)


    dato = miBD.consultar_talla(1.72)
    print(dato)
    print("-"*30)
    
    miBD.actualizar(int(input("ID: ")),int(input("Peso: ")),float(input("Talla: ")))
    resultado = miBD.consultar_todos()
    print("----- Datos en la base de datos -----")
    for item in resultado:
        print(item)
    
    print("-"*30)
    miBD.eliminar(int(input("ID: ")))
    resultado = miBD.consultar_todos()
    print("----- Datos en la base de datos -----")
    for item in resultado:
        print(item)
    print("-"*30)
