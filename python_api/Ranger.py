#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Модуль для работы с датчиком расстояния Promobot по шине Modbus RTU."""

__author__ = "Promobot"
__license__ = "Apache License, Version 2.0"
__status__ = "Production"
__url__ = "https://git.promo-bot.ru"
__version__ = "0.1.0"


import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


#Ranger registers
_TRIG_REGISTER      = 20
_RESULT_REGISTER    = 21
_COMMAND_REGISTER   = 19

_MIN_DIST_REGISTER  = 5


#Allowed commands
_PASS_COMMANDS      = [0xDEAD]

#Allowed distance for                       
_MAX_LED_DIST       = 2000
_MIN_LED_DIST       = 0

class Sensor():

    """Класс для работы с датчиком расстояния

    Args:
        * port (str): Имя последовательног порта шины данных, например ``/dev/RS485``.
        * address (int): Адрес устройства. 1-250
        * baudrate (int): Скорость соединения. По умолчанию 460800 Бод
        
    """

    def __init__(self,addr,master):

        self.master = master
        self.addr = addr
        self.logger = modbus_tk.utils.create_logger("console")

    #######PRIVATE FUNCTIONS#######

    def except_decorator(fn):
        def wrapped(self,*args):
            try:
                return fn(self,*args)
            except Exception as e:
                self.logger.error("%s", e)
                return False
        return wrapped

    ############################ 

    @except_decorator
    def trig_sensor(self):
        """Старт измерения.

        Args:
            None
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            None

        """
        
        return self.master.execute(self.addr, cst.WRITE_SINGLE_REGISTER, _TRIG_REGISTER, output_value=1)


    @except_decorator
    def read_sensor(self):
        """Чтение данных (измеренная дистанция) с датчика

        Args:
            None
        Returns:
            Словарь c ключами: 
                | "IR_distance" 
                | "US_distance"
        Raises:
            None

        """           
        data = {}

        values = self.master.execute(1, cst.READ_HOLDING_REGISTERS, _RESULT_REGISTER, 2)
        
        data["IR_distance"] = values[0] / 10
        data["US_distance"] = values[1]

        data["IR_distance"] = 255 if data["IR_distance"] == 819 else data["IR_distance"] 
        data["US_distance"] = 255 if data["US_distance"] == 8100 else data["US_distance"]   

        return data
        


    #@except_decorator
    def set_min_dist(self,dist):
        """Выставление порога измеренного расстояния, ниже которого загорается светодиод

        Args:
            * dist - дистанция в мм.
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            None

        """          
        if dist > _MIN_LED_DIST and dist <= _MAX_LED_DIST:
            return self.master.execute(self.addr, cst.WRITE_SINGLE_REGISTER, _TRIG_REGISTER, output_value=dist)
        else:
            raise ValueError("Wrong value for min dist!")     