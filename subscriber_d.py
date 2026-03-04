import zmq

context = zmq.Context()
sub = context.socket(zmq.SUB)

sub.setsockopt_string(zmq.SUBSCRIBE, "DADO")
sub.connect("tcp://proxy:5556")

while True:
    message = sub.recv_string()
    print("Dado recebido:", message, flush=True)

sub.close()
context.close()