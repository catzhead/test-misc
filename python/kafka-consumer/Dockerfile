FROM python:3.9-slim

WORKDIR /app

COPY kafka-consumer.py .

RUN pip install kafka-python-ng flask

CMD ["python", "kafka-consumer.py"]
