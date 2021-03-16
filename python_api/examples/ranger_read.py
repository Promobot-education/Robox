#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ranger_read.py

Пример подключения к датчику расстояния и чтения с него данных.

"""
import Ranger
import time

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес датчика расстояния. По умолчанию 1
sensor_id   = 1



master = modbus_rtu.RtuMaster(serial.Serial(port='/dev/RS_485', baudrate=460800, bytesize=8, parity='N', stopbits=1, xonxoff=0))
master.set_verbose(True)

#Инициализация датчика
sensor = Ranger.Sensor(sensor_id,master)

#Установка значения измеренной дистанции (мм), ниже которого сработает световая индикация. ЗЕЛЕНЫЙ - ИК датчик, СИНИЙ - УЗ датчик
sensor.set_min_dist(800) 

if __name__ == '__main__':

    while(True):

        #Отправка команды для измерения раастояния
        sensor.trig_sensor()

        time.sleep(0.05)

        #Чтение полученных данных о расстоянии
        vals = sensor.read_sensor()
        #Если есть данные, то делаим их вывод на экран
        if vals:
            print('Data from sensor: {0}'.format(sensor_id))
            print('------------')
            for i in vals:
                print('{0} : {1}'.format(i, vals[i]))
            print('\n' * 3)


