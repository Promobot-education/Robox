#!/bin/bash

apt update

apt install -y setserial udev autoconf nano libceres-dev liblua5.2-dev

cp 10-usb.rules /etc/udev/rules.d
udevadm control --reload-rules
udevadm trigger

git clone --single-branch --branch v3.1.6 https://github.com/stephane/libmodbus.git

cd libmodbus && ./autogen.sh && ./configure && make install && cd .. && rm -r libmodbus 

apt install --no-install-recommends -y \
    python3-pip \
    python3-tk \
    python3-serial \
    python3-matplotlib \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

apt install build-essential


cd python_api && sudo python3 setup.py install && cd ..


cd c_api && make && cd ..




