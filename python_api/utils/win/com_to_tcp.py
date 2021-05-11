#!/usr/bin/python

import socket
import sys
import serial
import serial.tools.list_ports
import threading

pid = "0403"
hid = "6001"
desc = "USB Serial Port"

port = ""

for dev in serial.tools.list_ports.comports():
    if pid and hid in dev.hwid:
        if desc in dev.description:
            port = dev.device

if port == "":
    print("Cant find available ports")
    exit()          

   
ser = serial.Serial(port, 460800, timeout=0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)


server_address = ('', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    try:
        connection, client_address = sock.accept()
        print('connection from', client_address)
        connection.settimeout(0.001)
        while True:
            try:
                data = connection.recv(16)
                if data == '': break
                ser.write(data)
            except KeyboardInterrupt:
                connection.close()
                sys.exit()
            except Exception as e:
                pass
            received_data = ser.read(ser.inWaiting())
            connection.sendall(received_data) 
    except Exception as e:
        print(e)

    finally:
        connection.close()