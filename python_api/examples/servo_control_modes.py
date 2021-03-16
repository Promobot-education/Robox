#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
servo_mode_to.py

Пример работы сервопривода в разных режимах.

* С каскадом ПИД регуляторов по сокрости и положение.

* Только с ПИД регулятором по скорости.

* Без регуляторов отпрвка ШИМ сигнала напрямую.

"""


import Servo
import time

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес сервопривода. По умолчанию 10
servo_id    = 10

#Инициализация последовательного порта
master = modbus_rtu.RtuMaster(serial.Serial(port=port, baudrate=460800, bytesize=8, parity='N', stopbits=1, xonxoff=0))


#Инициализация сервопривода
servo = Servo.Servo(servo_id,master)


if __name__ == '__main__':

    #С каскадом ПИД регуляторов по сокрости и положение.
    print("NORMAL mode")

    servo.set_PID_Mode("NORMAL")

    #Включение питания обмоток мотора
    servo.set_torque(1)

    #Движение в позицию 4000        
    servo.set_point(4000)
     
    time.sleep(4)


    #Только с ПИД регулятором по скорости.
    print("SPEED mode")
    servo.set_torque(0)                

    servo.set_PID_Mode("SPEED")

    servo.set_torque(1)

    #Установка оборотво вала в минуту
    servo.set_point(10)

    time.sleep(4)

    servo.set_torque(0)    


    #Без регуляторов, отправка ШИМ сигнала напрямую.
    print("PWM mode")
    servo.set_torque(0)                

    servo.set_PID_Mode("PWM")

    servo.set_torque(1)

    #Установка скважности ШИМ сигнала. (0-1000)
    servo.set_point(750)

    time.sleep(4)

    servo.set_torque(0)      


    #Выставление обычного режима работы           
    servo.set_PID_Mode("NORMAL")   