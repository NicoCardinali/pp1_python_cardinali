import requests

from flask import Flask, render_template, request

app = Flask(__name__)

listado_producto=[
    dict(
        producto="Camiseta",
        tipo="Titular",
        precio="100"
    ),
    dict(
        producto="Camiseta",
        tipo="Suplente",
        precio="90"
    ),
    dict(
        producto="Pantalon",
        tipo="Titular",
        precio="80"
    ),
    dict(
        producto="Campera",
        tipo="Suplente",
        precio="120"
    )
]

@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/productos')
def productos():
    listado = listado_producto
    return render_template (
        'productos.html',
        listado=listado
    )

@app.route('/add_producto', methods=['POST','GET'])
def agregar_producto():
    if request.method == 'POST':
        producto = request.form['producto']
        tipo = request.form['tipo']
        precio = int(request.form['precio'])
        

        nuevo_producto = dict(
                producto=producto,
                tipo=tipo,
                precio=precio
    )

        listado_producto.append(nuevo_producto)

    return render_template('add_producto.html')     