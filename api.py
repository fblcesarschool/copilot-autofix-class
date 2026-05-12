import sqlite3
import os
import subprocess
import ipaddress
from flask import Flask, request, make_response, escape

app = Flask(__name__)

# Injeção de SQL (SQL Injection)
def autenticar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Command Injection
@app.route("/ping")
def ping():
    ip = request.args.get("ip", "")
    try:
        validated_ip = str(ipaddress.ip_address(ip))
    except ValueError:
        return make_response("Invalid IP address", 400)

    result = subprocess.run(
        ["ping", "-c", "1", validated_ip],
        capture_output=True,
        text=True,
        check=False
    )
    output = result.stdout if result.stdout else result.stderr
    return f"<pre>{output}</pre>"

# Exposição de variáveis sensíveis 

@app.route("/debug")
def debug():
    return f"SECRET_KEY={os.environ.get('SECRET_KEY')}"

# Cross-Site Scripting (XSS)
@app.route("/comente")
def comente():
    comentario = request.args.get("comentario", "")
    comentario_escapado = escape(comentario)
    return f"<h1>Comentário recebido:</h1><p>{comentario_escapado}</p>"


if __name__ == '__main__':
    app.run(debug=False)
