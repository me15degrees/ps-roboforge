from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

"""
Para fazer um quadrado, existem dois movimentos básicos: andar para frente e virar.
Separei esses movimentos em duas funções e usei como parâmetro para a função a velocidade e o tempo de espera para cada um deles de acordo com o código fonte.
Como é interessante modularizar o código, pensei em fazer uma classe disso.
"""

class Robot:
    def __init__(self):
        self.ev3 = EV3Brick()
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)

    def move_forward(self, speed, time):
        self.left_motor.run(speed=speed)
        self.right_motor.run(speed=speed)
        wait(time)

    def turn_right(self, speed, time):
        self.left_motor.run_time(speed=speed, time=time)
        self.right_motor(speed=0)

    def execute_square(self):
        for _ in range(4):
            self.move_forward(200, 3000)
            self.turn_right(400, 2000)  
        self.left_motor.stop()
        self.right_motor.stop()
        self.left_motor.brake()
        self.right_motor.brake()

def main():
    robot = Robot()
    robot.execute_square()

if __name__ == "__main__":
    main()
