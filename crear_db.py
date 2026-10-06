import sqlite3

# Conectar/crear la base de datos en la misma carpeta
conn = sqlite3.connect('registro_auto.db')
cursor = conn.cursor()

# Crear la tabla pruebas_auto si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS pruebas_auto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conductor TEXT NOT NULL,
    velocidad_max REAL NOT NULL,
    vueltas_completadas INTEGER NOT NULL,
    tiempo_segundos REAL NOT NULL,
    estado_sensores TEXT NOT NULL
)
''')

# Insertar datos de prueba del proyecto Car Racing
datos_iniciales = [
    ('Dylan Almaras', 45.5, 10, 120.4, 'OK'),
    ('Nicolás Herrera', 48.2, 12, 115.0, 'OK'),
    ('Thiago Gómez', 42.0, 8, 130.2, 'Calibrar')
]

cursor.executemany('''
INSERT INTO pruebas_auto (conductor, velocidad_max, vueltas_completadas, tiempo_segundos, estado_sensores)
VALUES (?, ?, ?, ?, ?)
''', datos_iniciales)

conn.commit()
conn.close()
print("Base de datos registro_auto.db creada exitosamente con datos de prueba.")