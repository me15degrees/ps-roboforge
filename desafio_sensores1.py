#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (
    ColorSensor,
    Motor,
    UltrasonicSensor,
)
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

motorB = Motor(Port.B)
motorC = Motor(Port.C)
ultrasonic_sensor = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

DIAMETRO_RODA = 6.0
DIST_ENTRE_RODAS = 14
wall_distance = ultrasonic_sensor.distance()
tolerate_dist = 0.4

"""
O robô sempre deve andar paralelamente à parede, então eu guardo em uma variável essa distância e caso o sensor retorne algo diferente disso ele para de seguir os comandos.
Talvez eu acrescentaria uma variável de tolerância em relação à variação dessa distância, já que eu não sei como é a precisão do sensor e não tenho como testar.
Caso ele encontre a cor vermelha, é necessário girar 90 graus. Se encontrar amarelo ele espera o usuário apertar algum botão para sair do laço que segura o movimento.
Se o encontrar verde ele para.
"""

def curva(graus_reais):
    motorB.reset_angle(0)
    motorC.reset_angle(0)
    media_motor = 0
    graus_motor = graus_reais * (DIST_ENTRE_RODAS / DIAMETRO_RODA)
    while media_motor < graus_motor:
        motorB.run(200)
        motorC.run(-200)
        media_motor = (motorB.angle() - motorC.angle()) / 2
    motorB.hold()
    motorC.hold()

robot = DriveBase(motorB,motorC, wheel_diameter=55.5,axle_track=104)

while ultrasonic_sensor.distance() < wall_distance + tolerate_dist and ultrasonic_sensor.distance() > wall_distance - tolerate_dist:
    if color_sensor.color == Color.RED: 
        curva(90)
    if color_sensor.color == Color.YELLOW:
        button = Button()
        while not button.any():
            pass
    if color_sensor.color == Color.GREEN:
        robot.stop(Stop.BRAKE)
        break
    
    robot.drive(200, 0)
