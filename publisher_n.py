import zmq
from time import sleep
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    numero = random.randint(1,6)
    mensagem = f"DADO {numero}"
    print(mensagem, flush=True)
    pub.send_string(mensagem)
    sleep(1)

pub.close()
context.close()