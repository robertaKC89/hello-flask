from flask import Flask # 1º.creo aplicación importandolibrería

"""
Para ejecutar la app de Flask necesitamos un servidor web.
Flask proporciona uno para desarrollo pero necesitamos
un par de variables de entorno.

- Linux/Mac
  export FLASK_APP=hello     (hello es el nombre del archivo sin extensión)
  export FLASK_ENV=development    (puede ser también "production")

- Windows
  set FLASK_APP=hello
  set FLASK_ENV=development
"""

# 2º.instancio Flask (es class y me pide nombre. Le pongo el mismo nombre de archivo)
app = Flask(__name__)

# 3º.a cada ruta (más de una) Flask puede decorar una función con @ para especificarle cosas desde fuera
@app.route("/")
@app.route("/index")
@app.route('/hola')
def hola():    # Flask va a ejecutar un método que devuelva por ejemplo cadena (ver grabación smartphone)
    return 'Hola, soy Flask, quien eres tu usuario?'

# vuelvo a insertar decorador para que la funcion esté vinculada a una ruta
@app.route("/adiós")
def otra():
    return 'adiós usuario'
