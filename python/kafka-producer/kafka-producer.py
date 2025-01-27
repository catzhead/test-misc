from kafka import KafkaProducer
from datetime import datetime
import time
import json

producer = KafkaProducer(
    bootstrap_servers=['10.105.47.192:9092'],
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username='user1',
    sasl_plain_password='39H7SfCuPQ',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    producer.send('time_topic', {'timestamp': current_time})
    producer.flush()
    time.sleep(1)
