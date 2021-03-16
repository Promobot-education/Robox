#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
servo_read.py

Пример подключения к сервоприводу и чтения с него данных.

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

#Вывод отладочной информации по работе шины
master.set_verbose(True)

#Инициализация сервопривода
servo = Servo.Servo(servo_id,master)

time.sleep(2)

if __name__ == '__main__':

    while(True):

        #Чтение данных с сервопривода
        vals = servo.get_data()
        #Если есть данные, то делаим их вывод на экран
        if vals:
            #Вывод полученных данных
            print('Data from servo: {0}'.format(servo_id))
            print('------------')
            for i in vals:
                print('{0} : {1}'.format(i, vals[i]))
            time.sleep(0.05)
            print('\n' * 3)


