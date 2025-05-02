# Docker Cases and practices

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