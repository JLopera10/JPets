Proceso para iniciar el proyecto:

Tener instalado Python, Docker y Docker Compose

Iniciar un ambiente virtual de python

Hacer docker compose build en la raiz del proyecto

Hacer docker compose up para correr el servidor

(Importante)
Si el sistema pide un .env, crear un archivo .env en la raiz del proyecto y darle el contenido:

DEBUG=True
SECRET_KEY=dakjhsda98dab89da79d8a
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
