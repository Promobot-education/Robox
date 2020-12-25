Servo.py
--------

### class Servo(port,address,baudrate = 460800,debug = False)
        Класс для работы с сервоприводом.
    
        Args:
            * port (str): Имя последовательног порта шины данных, например ``/dev/RS485``.
            * slaveaddress (int): Адрес устройства. 1-250
            * baudrate (int): Скорость соединения. По умолчанию 460800 Бод
            * debug (bool): включение отладочного режима.


### custom_command(function,payload):
        Отправка пользовательской команды Modbus RTU.
        Args:       
            * functioncode (int): код пользовательской функции. Например "запись в регистр" = 16.
            * payloadToSlave (bytearray): Данные для отправки (к этим данным автоматически будут добавлен адрес устройства и CRC)
        Returns:
            * ответ от устройства (string)
        Raises:
            ValueError
  
### set_torque(state):
        Включение(отключение) питания обмоток двигателя
        Args:       
            * state (int): 
                0 - отключение питания обмоток двигателя, обмотки замкнуты, двигатель в торможении. 
                1 -Включение питания обмоток двигателя. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_command(command):
        Write command to servo.
        Args:
            * command (int): one of available commands. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_point(value):
        Установка задачи. (Положение, скорость, ШИМ в зависимости от режима работы)
        Args:
            * value (int): Требуемое значение. от -32000 to 32000. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            None

### set_Pos_PID_P(value):
        Запись коэф. P в ПИД регулятор по положению.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_Pos_PID_I(value):
        Запись коэф. I в ПИД регулятор по положению.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_Pos_PID_D(value):
        Запись коэф. D в ПИД регулятор по положению.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError
  
### set_Speed_PID_P(value):
        Запись коэф. P в ПИД регулятор по скорости.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_Speed_PID_I(value):
        Запись коэф. I в ПИД регулятор по скорости.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_Speed_PID_D(value):
        Запись коэф. D в ПИД регулятор по скорости.
        Args:
            * value (int): Желаемое значение в диапазоне от 0.01 to 50.0. 
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError

### set_PID_Mode(value):
        Высталвение режима работы ПИД регуляторов сервопривода.
        Args:
            * value (str): Режим работы.
                "NORMAL" - каскадный режим ПИД ругялтора по скорости и положению.
                "PWM" - отключение всех ПИД регуляторов и прямое управление скважностью ШИМ.
                "SPEED" - включение только ПИД регулятора поп сокрости.                  
        Returns:
            * True если отправка команды прошла успешно
            * False если при отправке команды произошла ошибка
        Raises:
            ValueError
 
### get_data():
        Чтение данных с сервопривода
        Args:
            None
        Returns:
            * Словарь с ключами: 
                 "Torque", 
                 "Setpoint" 
                 "Position" 
                 "Speed" 
                 "Command" 
                 "Current" 
                 "Pos_PID_P" 
                 "Pos_PID_I" 
                 "Pos_PID_D" 
                 "Speed_PID_P" 
                 "Speed_PID_I" 
                 "Speed_PID_D" 
                 "Errors"
        Raises:
            None
