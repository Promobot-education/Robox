#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import Servo
import time
"""
servo_plot.py

Пример отправки в сервопривод команд для перемещения в требуемую позицию и построения графика перемещения.

"""

#Инициализация сервопривода
servo = Servo.Servo('/dev/RS_485',10,debug = False)

#Желаемая позиция сервопривода
set_point   = 4000

#Интервал(сек.) между чтением данных с сервопривода
t_step      = 0.01

#Общее время (сек) построения графика
plot_time = 2.0

#Время (сек) от начала построения графика для перемещения сервопривода в желаемую позицию
move_start_time = 0.3

#Переменные для графика
x = []
y_position = []
y_setpoint = []

#Инициализация графика
fig = plt.figure()
data = fig.add_subplot(111)
data.set_xlabel('Time')
data.set_ylabel('Servo_value')
data.set_title('Servo step response')
data.autoscale(enable=True, axis='both', tight=None)


#Запуск таймера 
start = time.time()

#Строим график пока не прошло выделенное для этого время
while (time.time() - start) < plot_time:

    #Чтение данных с сервопривода
    vals = servo.get_data()

    #Если прошло достаточно времени для старта сервопривода, то отправляем его в желаемую позицию
    if  (time.time() - start) > move_start_time:
        #Включение питания обмоток мотора
        servo.set_torque(1)
        #Движение в желаемую позицию
        servo.set_point(set_point)

    #Отображение полученных от сервопривода данных на графике    
    x.append(time.time() - start)
    #Отображение двух данных от сервопривода: текущей позиции вала двигателя и желаемой позиции
    y_position.append(vals["Position"])
    y_setpoint.append(vals["Setpoint"])    
    time.sleep(t_step)


#Вывод графика на экран
data.plot(x, y_position,color="blue",label="Position")
data.plot(x, y_setpoint,color="red",label="Setpoint")
data.legend()
plt.show()