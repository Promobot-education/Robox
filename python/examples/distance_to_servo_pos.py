#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
servo_mode_to.py

Пример отправки в сервопривод команд для перемещения в требуемую позицию.

"""
import Servo
import Ranger
import time

#Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

#Адрес сервопривода. По умолчанию 10
servo_id    = 10

#Адрес датчика расстояния. По умолчанию 1
sensor_id   = 1

#Соотношение изменения расстояния к измененюи перемещения сервопривода
distance_to_pos_scale = 100

#Инициализация сервопривода
servo = Servo.Servo(port,servo_id,debug = False)

#Инициализация датчика расстояния
sensor = Ranger.Sensor(port,sensor_id,debug = False)

#Включение питания обмоток мотора
servo.set_torque(1)

if __name__ == '__main__':

    while(True):
        
        #Отправка команды для измерения раастояния
        sensor.trig_sensor()

        time.sleep(0.05)

        #Чтение полученных данных о расстоянии
        sensor_data = sensor.read_sensor()

        #Чтение данных с сервопривода
        vals = servo.get_data()

        #Вывод полученных данных
        print('Data from servo: {0}'.format(servo_id))
        print('------------')
        for i in vals:
            print('{0} : {1}'.format(i, vals[i]))    

        #Движение на позицию       
        servo.set_point(sensor_data["US_distance"] * distance_to_pos_scale) 


