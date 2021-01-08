#!/bin/bash

apt-get install setserial
sudo cp 10-usb.rules /etc/udev/rules.d
sudo udevadm control --reload-rules
sudo udevadm trigger