FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade --no-cache-dir -r /tmp/requirements.txt

COPY . /app

EXPOSE 80

CMD uvicorn src.main:app --host 0.0.0.0 --port 80 --reload
