FROM python:3.10-slim

WORKDIR /app

COPY bot.py .

# Aseguramos que el script tenga permisos de ejecución
RUN chmod +x bot.py

ENTRYPOINT ["python", "bot.py"]