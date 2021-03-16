#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
servo_mode_to.py

Пример отправки в сервопривод команд для перемещения в требуемую позицию.

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

#Включение питания обмоток мотора
servo.set_torque(1)

if __name__ == '__main__':

    while(True):
        
        #Движение в позицию 4000        
        servo.set_point(4000)

        #Ожидание перемещения мотора до требуемой позиции
        time.sleep(4)

        servo.set_point(0)
        time.sleep(4)

        servo.set_point(-4000)
        time.sleep(4)

        servo.set_point(0)
        time.sleep(4)   


