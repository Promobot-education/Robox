#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Servo
import time
"""
servo_custom_command.py

Пример отправки в сервопривод пользовательских команд.

"""

#Порт шины данных. По умолчпнию /dev/RS_485
port                = '/dev/RS_485'

#Адрес сервопривода. По умолчанию 10
servo_id            = 10

# Функция и команда для записи в сервоприво. Запись значения "0" в регистр "41"(0x29)
WRITE_FUNCTION      = 6

WRITE_COMMAND       = '\x00\x29\x00\x00'


# Функция и команда для чтения из сервоприво. Чтение 5 регистров начиная с 41 (0x29) регистра.
READ_FUNCTION       = 3

READ_COMMAND        = '\x00\x29\x00\x05'

servo = Servo.Servo(port,servo_id,debug = True)

if __name__ == '__main__':

    #Отправка команды на запись
    out = servo.custom_command(WRITE_FUNCTION,WRITE_COMMAND)

    print('Data from servo: {0}'.format(out))
    print('------------')
    print('\n' * 3)     

    #Отправка команды на чтение
    out = servo.custom_command(READ_FUNCTION,READ_COMMAND)  

    print('Data from servo: {0}'.format(out))
    print('------------')
    print('\n' * 3)     