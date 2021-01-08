#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Servo
import time
"""
servo_read.py

Пример подключения к сервоприводу и чтения с него данных.

"""

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес сервопривода. По умолчанию 10
servo_id    = 10

#Инициализация сервопривода
servo = Servo.Servo(port,servo_id,debug = True)

if __name__ == '__main__':

    while(True):

        #Чтение данных с сервопривода
        vals = servo.get_data()

        #Вывод полученных данных
        print('Data from servo: {0}'.format(servo_id))
        print('------------')
        for i in vals:
            print('{0} : {1}'.format(i, vals[i]))
        time.sleep(0.1)
        print('\n' * 3)


