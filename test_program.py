import zmq 
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:6666")


socket.send_string("lipps asvph")

ready = socket.recv()

socket.send_string("4")
time.sleep(0.6)

set = socket.recv()

time.sleep(0.6)

socket.send_string("d")
message = socket.recv()
message = message.decode()
print(message)
time.sleep(.5)

socket.send_string("Q") 
go = socket.recv()
socket.send_string("0") 
var = socket.recv()
socket.send_string("Q") 