#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ranger_read.py

Пример подключения к датчику расстояния и чтения с него данных.

"""
import Ranger
import time

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес датчика расстояния. По умолчанию 1
sensor_id   = 1

#Инициализация датчика
sensor = Ranger.Sensor(port,sensor_id,debug = True)

#Установка значения измеренной дистанции (мм), ниже которого сработает световая индикация. ЗЕЛЕНЫЙ - ИК датчик, СИНИЙ - УЗ датчик
sensor.set_min_dist(800) 

if __name__ == '__main__':

    while(True):

        #Отправка команды для измерения раастояния
        sensor.trig_sensor()

        time.sleep(0.1)

        #Чтение полученных данных о расстоянии
        vals = sensor.read_sensor()
        print('Data from sensor: {0}'.format(sensor_id))
        print('------------')
        for i in vals:
            print('{0} : {1}'.format(i, vals[i]))
        print('\n' * 3)


