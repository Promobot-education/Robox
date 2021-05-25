## Python

Взаимодействие с сервоприводом на примере [**servo_read.py**](https://github.com/Promobot-education/robox/blob/master/python/examples/servo_read.py)

Импорт необходимых модулей

Servo - модуль для работы с сервоприводом
bus-handler - модуль для работы с шиной передачи данных:
```python
import Servo
import bus_handler
```


Определение последовательного порта интерфейсного блока:
```python
port        = '/dev/RS_485'
```

Адрес сервопривода, по умолчанию адрес сервопривода в наборе - "10":
```python
servo_id   = 10
```

Инициализация шины передачи данных
```python
master = bus_handler.Bus(port = port, baudrate = 460800, debug = False, timeout = 1.0)
```

Создание объекта - сервопривода.:
```python
servo = Servo.Servo(servo_id, master.bus)
```


Чтение данных с сервопривода. Функция возвращает словарь c ключами: 

- "ID"
- "Torque", 
- "Setpoint" 
- "Position" 
- "Speed" 
- "Command" 
- "Current" 
- "Pos_PID_P" 
- "Pos_PID_I" 
- "Pos_PID_D" 
- "Speed_PID_P" 
- "Speed_PID_I" 
- "Speed_PID_D" 
- "Errors"

```python
vals = servo.get_data()
```

:information_source: [Описание библиотеки сервопривода на Python](https://github.com/Promobot-education/robox/blob/master/docs/python/servo_py.md)


## C

Взаимодействие с сервоприводом на примере  [**servo_control_modes.c**](https://github.com/Promobot-education/robox/blob/master/c/examples/servo_control_modes.c)

Включение библиотек:
Servo.h - библиотека для работы с сервоприводом

bus_handler.h - библиотека для взаимодействия с последовательным портом
```c
#include "Servo.h"
#include "bus_handler.h"
```

Выставление адреса сервопривода:
```c
int servo_addr = 10;
```

Инициализация последовательного порта для работы с сервоприводом. Вывод отладочной информации отключен.
```c
init_port("/dev/RS_485",false)
```

Стандартный режим работы сервопривода
```c
set_PID_mode(servo_addr,NORMAL);
```

Включение питания обмоток двигателя
```c
set_torque(servo_addr,true);
```

Перемещение на позицию 4000. Кол-во тиков. Один тик = 0,021 градуса.
```c
set_point(servo_addr,4000);
```

:information_source: [Описание библиотеки сервопривода на C](https://github.com/Promobot-education/robox/blob/master/docs/c/servo_c.md)