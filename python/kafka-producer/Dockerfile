FROM python:3.9-slim

WORKDIR /app

COPY kafka-producer.py .

RUN pip install kafka-python

CMD ["python", "kafka-producer.py"]
