import zmq
from time import sleep
from datetime import datetime

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    hora = datetime.now().strftime("%H:%M:%S")
    mensagem = f"HORA {hora}"
    print(mensagem, flush=True)
    pub.send_string(mensagem)
    sleep(1)

pub.close()
context.close()