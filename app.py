from flask import Flask, request, render_template_string
import sqlite3
import hashlib
import os

app = Flask(__name__)

# Crear DB si no existe
DB_NAME = 'usuarios.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def agregar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)', (nombre, hash_password(password)))
    conn.commit()
    conn.close()

def validar_usuario(nombre, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM usuarios WHERE nombre = ?', (nombre,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0] == hash_password(password)
    return False

#Plantilla simple HTML
html_form = '''
    <h2>Iniciar sesión</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre"><br>
        Contraseña: <input type="password" name="password"><br>
        <input type="submit" value="Ingresar">
    </form>
    {% if mensaje %}
    <p><strong>{{ mensaje }}</strong></p>
    {% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if validar_usuario(nombre, password):
            mensaje = f"✅ Acceso permitido: {nombre}"
        else:
            mensaje = "❌ Usuario o contraseña incorrectos"
    return render_template_string(html_form, mensaje=mensaje)

if __name__ == '__main__':
    init_db()

    # Agrega los integrantes del grupo (puedes cambiar esto)
    usuarios = [
        ('Fabian', 'password'),
        ('Jose', 'cisco123')
    ]

    for nombre, clave in usuarios:
        agregar_usuario(nombre, clave)

    app.run(port=7500)
