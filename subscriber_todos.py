import zmq

context = zmq.Context()
sub = context.socket(zmq.SUB)

sub.setsockopt_string(zmq.SUBSCRIBE, "HORA")
sub.setsockopt_string(zmq.SUBSCRIBE, "DADO")

sub.connect("tcp://proxy:5556")

while True:
    message = sub.recv_string()
    print("Mensagem:", message, flush=True)

sub.close()
context.close()