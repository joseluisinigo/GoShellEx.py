# GoShellEx.py
GoShellEx: Ejecución Remota Segura con Tokens JWT


## Descripción
`GoShellEx` es un script Python que genera tokens JWT con comandos y los envía a un servidor Go para su ejecución remota. Puedes personalizar la URL, el puerto y el secreto utilizado para firmar los tokens.

## Uso
```bash
python GoShellEx.py --url <URL_DEL_SERVIDOR_GO> --port <PUERTO_DEL_SERVIDOR_GO> --secret <CLAVE_SECRETA> <COMANDO>
```


Mis disculpas por el error. Aquí está el README con los bloques de código correctamente formateados:

markdown
Copy code
# GoShellEx

## Descripción
`GoShellEx` es un script Python que genera tokens JWT con comandos y los envía a un servidor Go para su ejecución remota. Puedes personalizar la URL, el puerto y el secreto utilizado para firmar los tokens.

## Uso
```bash
python GoShellEx.py --url <URL_DEL_SERVIDOR_GO> --port <PUERTO_DEL_SERVIDOR_GO> --secret <CLAVE_SECRETA> <COMANDO>
```
* <URL_DEL_SERVIDOR_GO>: La dirección IP o el nombre de dominio del servidor Go.
* <PUERTO_DEL_SERVIDOR_GO>: El puerto en el que el servidor Go está escuchando.
* <CLAVE_SECRETA> (opcional): La clave secreta para firmar el token JWT. Si no se proporciona, se usará la clave predeterminada.
* <COMANDO>: El comando que deseas ejecutar en el servidor Go.

## Ejemplos
Ejecutar ls -la en el servidor Go:
```bash
python GoShellEx.py --url 192.168.1.100 --port 3000 ls -la
```
Ejecutar whoami con una clave secreta personalizada:

```bash
python GoShellEx.py --url 192.168.1.100 --port 8080 --secret MiClaveSecreta whoami
```

## Requisitos
- Python 3.x
- Bibliotecas Python: jwt, datetime, subprocess, sys, requests, argparse

## Notas
Este script interactúa con un servidor Go que espera comandos en el formato /exec/{cmd}.
Asegúrate de que el servidor Go esté configurado correctamente y sea seguro.

1. Ejecutar el Script
2. Clona o descarga el repositorio.
3. Instala las bibliotecas requeridas con pip install -r requirements.txt.
4. Ejecuta el script con los argumentos necesarios.


## Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras problemas o mejoras, por favor, abre un problema o envía una solicitud de extracción.

## Licencia
Este proyecto está bajo la Licencia MIT.
