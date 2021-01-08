#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Модуль для работы с датчиком расстояния Promobot по шине Modbus RTU."""

__author__ = "Promobot"
__license__ = "Apache License, Version 2.0"
__status__ = "Production"
__url__ = "https://git.promo-bot.ru"
__version__ = "0.1.0"

import modbus_io

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
        * debug (bool): включение отладочного режима.
        
    """

    def __init__(self,port,address,baudrate = 460800,debug = False):
        modbus_io.CLOSE_PORT_AFTER_EACH_CALL = True
        modbus_io.BAUDRATE = baudrate
        modbus_io.TIMEOUT = 0.1
        try:
            self.client = modbus_io.Instrument(port, address)
            self.client.debug = debug
        except Exception as e:   
            print('Cant init port:{0}  {1}'.format(port, e))                    
            exit()  

    #######PRIVATE FUNCTIONS#######      

    def _write_register(self,
                        registeraddress,
                        value,
                        numberOfDecimals=0,
                        functioncode=6,
                        signed=True):
        try:
            self.client.write_register(registeraddress, value, numberOfDecimals, 6, signed)
            return True
        except Exception as e:
            print('ERROR! Sensor:{0}  {1}'.format(self.client.address, e))
        return False




    def _write_registers(self,
                        registeraddress,
                        values):
        try:
            self.client.write_registers(registeraddress, values)
            return True
        except Exception as e:
            print('ERROR! Sensor:{0}  {1}'.format(self.client.address, e))
        return False


    def _read_registers(self,
                        registeraddress,
                        numberOfRegisters,
                        functioncode=3):
        try:
            return self.client.read_registers(registeraddress, numberOfRegisters, functioncode)
        except Exception as e:
            print('ERROR! Sensor:{0}  {1}'.format(self.client.address, e))
        return False   

    ############################ 


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
        return self._write_register(_TRIG_REGISTER,1)



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
        values = self._read_registers(_RESULT_REGISTER, 2)
        if values is not False:

            data["IR_distance"] = values[0] / 10
            data["US_distance"] = values[1]

            data["IR_distance"] = 255 if data["IR_distance"] == 819 else data["IR_distance"] 
            data["US_distance"] = 255 if data["US_distance"] == 8100 else data["US_distance"]
        return data



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
            return self._write_register(_MIN_DIST_REGISTER,dist) 