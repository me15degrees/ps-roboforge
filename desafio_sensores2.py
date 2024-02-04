from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

"""
Para fazer um quadrado, existem dois movimentos básicos: andar para frente e virar.
Separei esses movimentos em duas funções e usei como parâmetro para a função a velocidade e o tempo de espera para cada um deles de acordo com o código fonte.
"""

def mover_frente(velocidade, tempo):
    motor_esquerdo.run(speed=velocidade)
    motor_direito.run(speed=velocidade)
    wait(tempo)

def virar_direita(velocidade, tempo):
    motor_esquerdo.run(speed=velocidade, time=tempo)
    motor_direito.run(speed=0)
    
def main():
    for _ in range(4):
        mover_frente(200, 3000)  
        virar_direita(400, 2000)  

    motor_esquerdo.stop()
    motor_direito.stop()
    motor_esquerdo.brake()
    motor_direito.brake()
    
if __name__ == "__main__":
    main()
