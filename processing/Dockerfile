FROM python:3.10-slim-buster

WORKDIR /app

COPY processing/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY processing /app/processing
COPY config /app/config
COPY logs /app/logs
COPY utils /app/utils



CMD ["python","-m", "processing.processing_manager"]


