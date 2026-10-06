import sqlite3
from flask import Flask, render_template

def get_db_connection():
    """Conecta a la base de datos de telemetría del auto."""
    conn = sqlite3.connect('registro_auto.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal: Muestra el historial de pruebas del auto Car Racing."""
    conn = get_db_connection()
    pruebas = conn.execute('SELECT * FROM pruebas_auto').fetchall()
    conn.close()
    return render_template('index.html', pruebas=pruebas)

@app.route('/frenado_ir')
def frenado_ir():
    """Muestra solo las pruebas donde el sistema IR funcionó correctamente."""
    conn = get_db_connection()
    frenado = conn.execute(
        "SELECT * FROM pruebas_auto WHERE estado_sensores = 'OK'"
    ).fetchall()
    conn.close()
    return render_template('frenado.html', frenado=frenado)

@app.route('/telemetria')
def telemetria():
    """Muestra la telemetría ordenada por velocidad máxima."""
    conn = get_db_connection()
    telemetria_data = conn.execute(
        "SELECT conductor, velocidad_max, vueltas_completadas, tiempo_segundos "
        "FROM pruebas_auto ORDER BY velocidad_max DESC"
    ).fetchall()
    conn.close()
    return render_template('telemetria.html', telemetria=telemetria_data)

if __name__ == '__main__':
    app.run(debug=False)