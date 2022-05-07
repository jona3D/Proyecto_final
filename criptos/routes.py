from criptos import app
from flask import render_template, jsonify, request
from criptos.models import Gestiona_Datos
import sqlite3

ruta_db = app.config['RUTA_BBDD']
data_manager = Gestiona_Datos(ruta_db)



@app.route("/")
def inicio():
    return render_template("index.html")



@app.route("/api/v01/movimientos")
def todos():
    datos = data_manager.todos_movimientos()
    return jsonify(datos)

"""@app.route("/api/v01/tipo_cambio/<divisa_from>/<divisa_to>/<cantidad>")
def muestra_cambio(divisa_from,divisa_to,cantidad):
    datos = request.json
    try:
        data_manager.update_datos((datos['fecha'], datos['hora'], datos['concepto'], datos ['cantidad'],
                                 datos['es_ingreso'], id))
        return jsonify({'status': 'success'})
    except sqlite3.Error as e:
        return jsonify({'status': 'error', 'msg': str(e)})"""


"""@app.route("/api/v01/movimiento",["POST"])
def intro_movimiento(divisa_from,divisa_to,cantidad):



@app.route("/api/v01/status")
def muestra_status():"""