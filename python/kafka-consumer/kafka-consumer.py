from kafka import KafkaConsumer
from flask import Flask, render_template_string
import json
from threading import Thread
import queue

app = Flask(__name__)
messages = queue.Queue()

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Kafka Messages</title>
    <meta http-equiv="refresh" content="1">
</head>
<body>
    <h1>Messages from Kafka</h1>
    <div>
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    </div>
</body>
</html>
'''

def kafka_consumer():
    consumer = KafkaConsumer(
        'time_topic',
        bootstrap_servers='10.105.47.192:9092',
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        sasl_plain_username='user1',
        sasl_plain_password='39H7SfCuPQ',
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        messages.put(message.value)

@app.route('/')
def home():
    message_list = list(messages.queue)
    return render_template_string(HTML_TEMPLATE, messages=message_list)

if __name__ == '__main__':
    kafka_thread = Thread(target=kafka_consumer)
    kafka_thread.daemon = True
    kafka_thread.start()
    app.run(host='0.0.0.0', port=8080)
