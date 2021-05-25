# Общие сведения

:information_source: Перед началом работы прочтите [руководстве пользователя Robox](https://github.com/Promobot-education/robox/blob/master/docs/Robox_manual.pdf)

Для работы с устройствами Robox используются библиотеки на **Python** и **С**.

Протокол взаимодействия c устройствами - **MODBUS RTU**.

Библиотеки основаны на существующих решениях для работы с протоколом MODBUS:
* [modbus-tk](https://github.com/ljean/modbus-tk) ( Python )
* [libmodbus](https://github.com/stephane/libmodbus)( C )

Интерфейс работы с устройствами на шине - **RS485**.

Структура работы с устройствами Robox:

![device_image](https://github.com/Promobot-education/robox/blob/master/docs/res/Edu.png "Struct") 

# Установка

Скачать репозиторий Robox:

```bash
git clone https://github.com/Promobot-education/robox.git
cd robox
```

### ОС Linux

:heavy_exclamation_mark: Рекомендуется использовать дистрибутив Ububntu версии **не ниже 16.04**. Версия Python **не ниже 3.5**.

Установить требуемые зависимости и компоненты:

```bash
./install.sh
```

### ОС Windows

Установить [Python](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)

Установить требуемые модули

```bash
cd /python
python setup.py install
```

# Запуск примеров:

### Python

```bash
cd /python/examples
python3 servo_read.py
```

### С

```bash
cd /с/build
./servo_read
```