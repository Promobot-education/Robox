#!/bin/bash

sudo apt update &&
sudo apt install -y setserial udev autoconf nano libceres-dev liblua5.2-dev &&

sudo cp -f 10-usb.rules /etc/udev/rules.d &&
udevadm control --reload-rules &&
udevadm trigger

git clone --single-branch --branch v3.1.6 https://github.com/stephane/libmodbus.git

cd ./libmodbus && ./autogen.sh && ./configure && sudo make install && cd .. && rm -r libmodbus &&

sudo apt install --no-install-recommends -y \
     python3-pip \
     python3-tk \
     python3-serial \
     python3-matplotlib \
     python3-setuptools \
     && sudo rm -rf /var/lib/apt/lists/* &&

sudo apt install build-essential &&

cd ./python_api && sudo python3 setup.py install && cd .. &&

cd ./c_api && make && cd .. &&

echo "FINISH"
