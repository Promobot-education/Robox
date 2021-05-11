Работа с устройствами robox через проброс последовательного порта "COM <-> TCP". Windows + Linux(WSL2)

1. В Windows выполнить:

```bash
python com_to_tcp.py
```

2. В Linux выполнить команды:

```bash
export HOST_ADDR=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null)
sudo socat -d -d pty,link=/dev/RS_485,raw,echo=0,perm=0666 tcp:$HOST_ADDR:5000
```

3. При работе с устройствами через Python необходимо при инициалзиации шины выставить аргумент port_forward = True:

```python
master = bus_handler.Bus(port = port, baudrate = 460800, debug = False, timeout = 1.0, port_forward = True)
```

