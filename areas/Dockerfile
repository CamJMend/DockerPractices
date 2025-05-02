FROM python:3.9

WORKDIR /app

COPY requirements_areas.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app_areas.py ./app.py

EXPOSE 5000

CMD ["python", "app.py"]