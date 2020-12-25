# ROBOX

Решение для простого взаимодействия с сервоприводом и датчиком расстояния Promobot

## Содержание
1. [Общие сведения](#Общие-сведения)
2. [Интерфейсная плата](#Интерфейсная-плата)
3. [Сервопривод](#Сервопривод)
4. [Датчик расстояния](#Датчик-расстояния)
5. [Начало работы](#Начало-работы)



## Общие сведения

Для работыс с устройствами Promobot используются бибилотеки на **Python** и **С**.

Протокол взаимодействия c устройствами - **MODBUS RTU**.

Бибилотеки основаны на существующих решениях для работы с шиной MODBUS:
* [minimalmodbus](https://github.com/pyhys/minimalmodbus) ( Python )
* [libmodbus](https://github.com/stephane/libmodbus)( C )

Интерфейс работы с устройствами по шине - **RS485**.

Для удобства и безопасности вся работа с устройсвами Promobot осуществляется в **Docker** контейнере.

**Структура работы с устройствами Promobot:**

![device_image](https://github.com/Promobot-education/robox/blob/main/docs/res/Edu.png "Struct") 


## Интерфейсная плата

Интерфейcная плата (ROBOX) предназначена для преобразования интерфейсов USB-RS485, а также для обеспечения питанием подключенных устройств Promobot.

![device_image](https://github.com/Promobot-education/robox/blob/main/docs/res/robox.png "Robox") 

:information_source: Более подробную информацию об интерфейсной плате можно найти в [Руководстве пользователя](https://github.com/Promobot-education/robox/blob/main/docs/Robox_manual.pdf)




## Сервопривод

Сервопривод является высокопроизводительным исполнительным механизмом, разработанным специально для нужд робототехники. Данный сервопривод может использоваться для создания подвижных механизмов повышенной сложности, например, роботов-манипуляторов, pan-tilt модулей и т.п.

**Структура типового взаимодействия с сервоприводом:**

![device_image](https://github.com/Promobot-education/robox/blob/main/docs/res/motor_struct.png "Motor_struct") 

 
:information_source: [Описание библиотеки сервопривода на Python](https://github.com/Promobot-education/robox/blob/main/docs/servo_py.md)

:information_source: [Описание библиотеки сервопривода на C](https://github.com/Promobot-education/robox/blob/main/docs/servo_c.md)



## Датчик расстояния

Ranger_Sensor предназначен для детектирования препятствий и последующего определения расстояния до них. В данном устройстве используются как ультразвуковые (УЗ) сигналы измерения, так и инфракрасные (ИК)

**Структура типового взаимодействия с датчиком расстояния:**

![device_image](https://github.com/Promobot-education/robox/blob/main/docs/res/Range_struct.png "Range_struct") 

:information_source: [Описание библиотеки датчика расстояния на Python](https://github.com/Promobot-education/robox/blob/main/docs/ranger_py.md)

:information_source: [Описание библиотеки датчика расстояния на C](https://github.com/Promobot-education/robox/blob/main/docs/ranger_c.md)



## Начало работы

:warning: Перед проведением работ необходимо ознакомиться с [Руководством пользователя](https://github.com/Promobot-education/robox/blob/main/docs/Robox_manual.pdf)

#### Подготовка

Установка Docker:
```sh
$ apt-get install docker.io
```

Установка репозитория:
```sh
$ git clone https://github.com/Promobot-education/robox.git
$ cd robox
```

Для корректной работы интерфейсной платы необходимо:
```sh
$ apt-get install setserial
$ sudo cp 10-usb.rules /etc/udev/rules.d
$ sudo udevadm control --reload-rules
$ sudo udevadm trigger
```

Сборка Docker образа:
```sh
$ cd docker
$ sudo ./build.sh
```

#### Создание контейнера

Если при работе используется интерфейсная плата:
```sh
$ sudo docker run -it --device=/dev/RS_485 --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -v /$HOME/Edu_env:/home/student/Edu_env promobot_edu
```

Если при работе **НЕ используется** интерфейсная плата:
```sh
$ sudo docker run -it --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -v /$HOME/Edu_env:/home/student/Edu_env promobot_edu
```
:key: логин:пароль - student:student

#### Работа с примерами библиотек

Примеры работы с устройствами Promobot расположены:

**Python** - /python/examples

**C**      - /c/examples_build

Для сборки (установки) библиотек и примеров:

**Python**:
```sh
$ cd python/
$ sudo python setup.py install
```

**C**:
```sh
$ cd c/
$ make
```
