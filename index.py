# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:36:56 2020

@author: Juan Carlos Jerez

En este ejemplo se utiliza un framework llamado FLASK que permite el desarrollo
de aplcaciones web, similar a Django, pero con funcionalidades más limitadas.

La carpeta templates guarda las páginas (vistas) que se invocan en cada ruta.
Por defecto Flask busca estas paginas en la carpeta Templates.
"""

## Se importa el framework Flask
from flask import Flask, render_template

## Se inicializa el framework y se crea una app para gestioanr un servidor
app = Flask(__name__)

## Se define la ruta del Home
@app.route('/')
def home():
    return render_template('home.html')

## Por cada ruta se puede definir la página que responde
@app.route('/about')
def about():
    return render_template('about.html')

## Se se escribe app.run() sin ninguna opción, cada vez que se hace un cambio en la aplicacíon
## es necesario reiniciar el app.
## para hacer que se reinicie atuomáticamente cuando identifica un cambio se pone en modo DEBUG
## es decir, en modo de desarrollo
## app.run(debug = True)
if __name__ == '__main__':
    app.run(debug=True)
    
    
