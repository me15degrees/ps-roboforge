from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

"""
Para fazer um quadrado, existem dois movimentos básicos: andar para frente e virar.
Separei esses movimentos em duas funções e usei como parâmetro para a função a velocidade e o tempo de espera para cada um deles de acordo com o código fonte.
"""

def mover_frente(velocidade, tempo):
    motor_esquerdo.run(speed=velocidade)
    motor_direito.run(speed=velocidade)
    wait(tempo)

def virar_direita(velocidade, tempo):
    motor_esquerdo.run(speed=velocidade)
    motor_direito.run(speed=-velocidade)
    wait(tempo)

if __name__ == "__main__":
    ev3 = EV3Brick()

    motor_esquerdo = Motor(Port.B)
    motor_direito = Motor(Port.C)

    for _ in range(4):
        mover_frente(200, 2000)  
        virar_direita(200, 1000)  

    motor_esquerdo.stop()
    motor_direito.stop()
