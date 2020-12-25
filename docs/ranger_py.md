Ranger.py
---------

### class Sensor(port,address,baudrate = 460800,debug = False)
        Класс для работы с датчиком расстояния
        Args:
             port (str): Имя последовательного порта шины данных, например ``/dev/RS485``
             address (int): Адрес устройства. 1-250
             baudrate (int): Скорость соединения. По умолчанию 460800 Бод
             debug (bool): включение отладочного режима.



### trig_sensor()
        Старт измерения расстояния
        Args:
            None
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            None

    
### read_sensor():
        Чтение данных (измеренная дистанция) с датчика расстояния
        Args:
            None
        Returns:
            Словарь c ключами: 
                "IR_distance" 
                "US_distance"
        Raises:
            None
   
### set_min_dist(dist)
        Выставление порога измеренного расстояния, ниже которого загорается светодиод
        Args:
            * dist (int) - дистанция в мм.
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            None
