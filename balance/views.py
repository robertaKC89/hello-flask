from balance import app

# a cada ruta Flask puede decorar una función con @ para especificarle cosas desde fuera
# estas rutas son para la estructura principal de mi app balance
@app .route ('/')
def home():
    return 'Página de inicio'

@app .route ('/nuevo')
def nuevo ():
    return 'creación de movimiento'

@app .route ('/modificar')
def actualizar():
    return 'actualizar movimiento'

@app .route ('/borrar')
def borrar ():
    return 'borrar movimiento'