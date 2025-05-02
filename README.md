# Docker Cases and practices

## Bot

### Archivos Implementados:
- bot.py: Este script de Python recibe dos parámetros a través de la línea de comandos: el primer parámetro es el nombre del usuario y el segundo parámetro es la pregunta que hace el usuario. El script registra estos datos junto con la fecha y hora actual en un archivo llamado historial.txt dentro de un directorio /data, que será donde montaremos nuestro volumen.
- Dockerfile: Define cómo se construirá nuestra imagen Docker

### Ejecutar el código
1. Abrir el código fuente y entrar a la carpeta correspondiente:
```bash
cd bot-pregunta
```
2. Abrir Docker
3. Construir la imagen Docker con
```bash
docker build -t bot-app .
```
4. Crear el volumen Docker para almacenar el historial con 
```bash
docker volume create bot-historial
```
5. Ejecutar el contenedor con el volumen con
```bash
docker run --rm -v bot-historial:/data bot-app "Juan" "¿Cómo funciona Docker?"
```
- Para registrar mas preguntas:
```bash
docker run --rm -v bot-historial:/data bot-app "Maria" "¿Qué son los volúmenes en Docker?"
docker run --rm -v bot-historial:/data bot-app "Pedro" "¿Cómo instalo Python?"
```
6. Ver el contenido del historial con:
```bash
docker run --rm -v bot-historial:/data alpine cat /data/historial.txt
```


## Microservices Flask

### Archivos Implementados:

- app.py: Contiene el código Flask que implementa cuatro microservicios matemáticos (suma, resta, multiplicación y división)
- Dockerfile: Define cómo construir el contenedor Docker para nuestra aplicación
- requirements.txt: Especifica las dependencias necesarias (Flask)

### Microservicios REST:

- Suma: Endpoint que acepta dos parámetros y devuelve su suma
- Resta: Endpoint que acepta dos parámetros y devuelve su diferencia
- Multiplicación: Endpoint que acepta dos parámetros y devuelve su producto
- División: Endpoint que acepta dos parámetros y devuelve su cociente, con validación para división por cero

### Ejecutar el código
1. Abrir el código fuente y entrar a la carpeta correspondiente:
```bash
cd microservices-flask
```
2. Abrir Docker
3. Construir la imagen Docker con 
```bash
docker build -t micro .
```
4. Ejecutar el contenedor con 
```bash
docker run -p 5000:5000 micro
```
5. Probar los endpoints mediante solicitudes HTTP a localhost:5000


## Calculo de Áreas

### Archivos Implementados:
- app_areas.py
- Dockerfile
- requirements_areas.txt

### Microservicios REST:
- Área de un Triángulo: Calcula el área de un triángulo usando base y altura.
- Área de un Cuadrado: Calcula el área de un cuadrado usando la longitud del lado.
- Área de un Círculo: Calcula el área de un círculo usando el radio.

### Ejecutar el código
1. Abrir el código fuente y entrar a la carpeta correspondiente:
```bash
cd areas
```
2. Abrir Docker
3. Construir la imagen Docker con 
```bash
docker build -t areas-microservicios -f Dockerfile .
```
4. Ejecutar el contenedor con 
```bash
docker run -p 5000:5000 areas-microservicios
```
5. Probar los endpoints mediante solicitudes HTTP a localhost:5000

- Página principal: http://localhost:5000/
- Área de un triángulo: http://localhost:5000/area/triangulo?base=5&altura=3
- Área de un cuadrado: http://localhost:5000/area/cuadrado?lado=4
- Área de un círculo: http://localhost:5000/area/circulo?radio=5