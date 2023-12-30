# Challenge Back-End

A continuación se indicarán los pasos para correr correctamente el servidor y probar los endpoints desde Postman.

## Correr servidor

1. Lo primero que se debe realizar es instalar docker y docker-compose (en mi caso realicé la instalación de Docker Desktop en Windows que ya los incluye).
2. Se debe clonar este repositorio.

3. Se debe registrar un servidor en postgres con las siguientes propiedades:

HOST = localhost
PASSWORD = admin1234 
PORT = 5433
USER = postgres

4. Se debe de crear una base de datos en este servidor con el nombre de 'prueba'

5. se debe crear un archivo .env en la raiz del proyecto, el contenido de este archivo se comparte en el correo junto al link del repositorio.

6. Se debe ejecutar el siguiente comando dentro del directorio raíz del proyecto para crear los contenedores y correrlos.

```bash
docker-compose up --build
```
7. Después de esto ya debería estar corriendo todo correctamente.

8. Para detener los contenedores se ejecuta el siguiente comando o con ctrl + C.

```bash
docker-compose down
```

## Probar los endpoints

1. Se debe importar la colección en Postman, la colección de postman se puede obtener del siguiente link :https://api.postman.com/collections/27003563-8ead4552-9a80-4bae-ad17-b3fc4cdffeab?access_key=PMAT-01HJX8M1WKAMB6WQYQNH5VTMB9  se debe dar en el botón import y pegar el link enviado, o se puede descargar directamente en el correo enviado con las respuestas de la prueba técnina, en este correo se encuentra el archivo de la colección (Se encuentra como respuesta del correo enviado)
2. Después, se debe crear un cliente (usuario), el endpoint se encuentra en la colección en la carpeta llamada 'Clients', se llama register el endpoint, esto se debe de hacer para realizar la autenticación y poder consumir los servicios.
3. Ya con el usuario creado, se debe proceder a la autenticación, para lo cual se consumirá el endpoint del Login (se encuentra en la carpeta 'Client'). Este retornará un response como el siguiente, del cual se tomará el access token:
```json
{
    "message": "Inicio de sesión exitosa",
    "data": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTE2MTQ0MiwiaWF0IjoxNjgxMDc1MDQyLCJqdGkiOiIyZWU3ZWNjYzc4YTk0N2UxOTkzMWI1M2JhMjYxZWIwZSIsInVzZXJfaWQiOjF9.02gBmjyZ_P7T00gqhfjZoO3gs0NJFrydBozuZ50qX2E",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMTYxNDQyLCJpYXQiOjE2ODEwNzUwNDIsImp0aSI6ImYyZDM1ZTU2MWU4ZTQ1MThhNjg0MDc4M2FkNDdlNzA3IiwidXNlcl9pZCI6MX0.i6niY9lqMd8ofg8-rh3w5ZW2CW4boJQwyt1Rx4iQ3jA"
    }
}
```
4. Finalmente, se usa este token en la cabecera de las peticiones.


* Se agrego la documentación técnica con swagger, se puede observar en el siguiente link:  http://127.0.0.1:8000/swagger/

* El archivo .env en este caso se va a subir al repositorio para su correcta revisión.

El asunto del correo enviado es: Prueba Técnica - Dev Python - Juan Camilo Arias
