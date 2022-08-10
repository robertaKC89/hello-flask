"""
Un movimiento debe tener mínimo (para poder mostrar una tabla):
1. Fecha
2. Concepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""
import csv  #librería que me proporciona varios tipos de lectores
from datetime import date, datetime

from . import FICHERO
 
# creo class de tipo movimiento
class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.errores = []   # me guardaré los errores en una lista de errores vacío de inicio
        try:    # convierto fecha str en objeto fecha con iso format
            self.fecha = date.fromisoformat (fecha)
        except ValueError:
            self.errores.append ('fecha no válida, revisa por favor')

        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

class ListaMovimientos: # para mostrar lo anterior en lista
    def __init__(self):
        self.movimientos = []   # en constructor arranco con lista movimientos vacía

    def leer_archivo(self):
        #con with no debo pensar en cerrar el fichero, lo cierra solo al terminar bucle
        with open(FICHERO,"r") as fichero: #   lectura que hago gracias a importar librería csv
            reader = csv.DictReader(fichero)    # me mostrará lectura como dicc que podré convertir en objeto Python
            for linea in reader:    # cada linea que recorra el lector que me genere un movimiento
                mov = Movimiento (linea ['fecha'], linea ['concepto'], linea ['tipo'], linea ['cantidad'])
                self.movimientos.append(mov) 
