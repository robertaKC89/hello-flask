from flask import render_template
from . import app
from .models import ListaMovimientos

# a cada ruta Flask puede decorar una función con @ para especificarle cosas desde fuera
# estas rutas son para la estructura principal de mi app balance
@app .route ('/')
def home():
    '''
    muestra la lista de movimientos cargados
    '''
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    #llamo y ejecuto pasandole a Flask inicio.html xk lo buscará en templates
    #le paso también lista_movimientos lo que he creado en la plantilla movs de inicio.html
    return render_template("inicio.html", movs=movimientos.movimientos)    
    

@app .route ('/nuevo')
def nuevo ():
    return 'creación de movimiento'

@app .route ('/modificar')
def actualizar():
    return 'actualizar movimiento'

@app .route ('/borrar')
def borrar ():
    return 'borrar movimiento'