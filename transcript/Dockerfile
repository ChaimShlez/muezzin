FROM python:3.10-slim-buster

WORKDIR /app

COPY transcript/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY transcript /app/transcript
COPY config /app/config
COPY logs /app/logs




CMD ["python","-m", "transcript.transcript_manager"]


