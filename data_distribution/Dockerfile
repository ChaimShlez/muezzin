FROM python:3.10-slim-buster

WORKDIR /app

COPY data_distribution/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY data_distribution /app/data_distribution
COPY config /app/config
COPY logs /app/logs



CMD ["python","-m", "data_distribution.distribution_manager"]

