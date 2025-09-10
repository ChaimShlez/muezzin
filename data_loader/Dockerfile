FROM python:3.10-slim-buster

WORKDIR /app

COPY data_loader/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY data_loader /app/data_loader
COPY config /app/config
COPY logs /app/logs



CMD ["python","-m", "data_loader.manager"]


