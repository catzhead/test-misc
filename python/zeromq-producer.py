# producer.py
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    message = f"Hello {time.time()}"
    socket.send_string(message)
    time.sleep(1)
