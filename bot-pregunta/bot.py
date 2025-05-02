import sys
import os
import datetime

def main():
    if len(sys.argv) != 3:
        print("Se necesitan 2 parámetros: python bot.py <usuario> <pregunta>")
        return
    
    usuario = sys.argv[1]
    pregunta = sys.argv[2]
    
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Usuario: {usuario}")
    print(f"Pregunta: {pregunta}")
    print(f"Fecha y hora: {fecha_hora}")
    
    output_path = "/data/historial.txt"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "a") as f:
        f.write(f"[{fecha_hora}] Usuario: {usuario} | Pregunta: {pregunta}\n")
    
    print("Pregunta registrada en el historial correctamente.")

if __name__ == "__main__":
    main()