# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
servo_plot.py

Пример отправки в сервопривод команд для перемещения в требуемую позицию и построения графика перемещения.

"""

import matplotlib.pyplot as plt
import Servo
import time
import bus_handler
from threading import Timer

# Порт шины данных. По умолчпнию /dev/RS_485
port        = '/dev/RS_485'

# Адрес сервопривода. По умолчанию 10
servo_id    = 10

# Инициализация шины передачи данных
master = bus_handler.Bus(port = port, baudrate = 460800, debug = False, timeout = 1.0)

# Инициализация сервопривода
servo = Servo.Servo(servo_id, master.bus)

# Желаемая позиция сервопривода
set_point   = 4000

# Интервал(сек.) между чтением данных с сервопривода
t_step      = 0.01

# Общее время (сек) построения графика
plot_time = 2.0

# Время (сек) от начала построения графика для перемещения сервопривода в желаемую позицию
move_start_time = 0.3

# Переменные для графика
x = []
y_position = []
y_setpoint = []

# Инициализация графика
fig = plt.figure()
data = fig.add_subplot(111)
data.set_xlabel('Time')
data.set_ylabel('Servo_value')
data.set_title('Servo step response')
data.autoscale(enable=True, axis='both', tight=None)

#  Включим сервопривод, выставим вал в начальное положение
servo.set_torque(1)
servo.set_point(0)

# Дождемся выставления вала в ноль с некоторой погрешностью +- 15 тиков
while not (-15 <= servo.get_data()["Position"] <= 15):
    time.sleep(0.01)

# Запуск таймера 
start = time.time()

# Список точек, точка состоит из 2х чисел, время и желаемое положение
points = [
    (0.3,   4000),
    (0.75,  4500),
    (1,     3500),
    (1.15,  4000),
    (1.30,  3500),
    (1.5,   4000),
]

# Запускает выставление положения через заданный промежуток времени
for t, p in points:
    Timer(t, servo.set_point, (p,), kwargs=None).start()
    
while (time.time() - start) < plot_time:
    # Чтение данных с сервопривода
    vals = servo.get_data()

    # Запишем время итерации на график    
    x.append(time.time() - start)

    # Отображение двух данных от сервопривода: текущей позиции вала двигателя и желаемой позиции
    y_position.append(vals["Position"])
    y_setpoint.append(vals["Setpoint"])    
    time.sleep(t_step)

# Выключим сервопривод
servo.set_torque(0)

# Вывод графика на экран
data.plot(x, y_position,color="blue",label="Position")
data.plot(x, y_setpoint,color="red",label="Setpoint")
data.legend()
plt.show()