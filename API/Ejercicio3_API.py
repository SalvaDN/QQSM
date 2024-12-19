import requests

api_key = "31c5543c1734d25c7206f5fd"
url = "https://leakcheck.io/api/public"

correo = input("Introduce la dirección de correo electrónico: ")

url_api = f"{url}?key={api_key}&check={correo}"
respuesta= requests.get(url_api)
datos = respuesta.json()

print(datos)
