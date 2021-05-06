#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ranger_read.py

Пример подключения к датчику расстояния и чтения с него данных.

"""
import Ranger
import time
import bus_handler

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес датчика расстояния. По умолчанию 1
sensor_id   = 1


#Инициализация шины передачи данных
master = bus_handler.Bus(port = port, baudrate = 460800, debug = False, timeout = 1.0)

#Инициализация датчика
sensor = Ranger.Sensor(sensor_id ,master.bus)

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


