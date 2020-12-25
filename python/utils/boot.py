#!/usr/bin/env python
import sys
import time
import argparse
import modbus_io
import struct
import Servo


packet = 128

parser = argparse.ArgumentParser(description='Set values for a servo, by id')
parser.add_argument('-p', '--port', type=str, help='port for flashing',default='None')


args = parser.parse_args()


#modbus_io.TIMEOUT = 0.03
#modbus_io.CLOSE_PORT_AFTER_EACH_CALL = True
#modbus_io.BAUDRATE = 460800

mod_port = str(args.port)

ping_devs = []

instr = None

def ping():
	print("Pinging devices...")
	for element in range(0, 50):
		time.sleep(0.1)
		try:
			temp = Servo.Servo(mod_port,element,debug = False,ping = True)
			#temp = modbus_io.Instrument(mod_port, element, mode=modbus_io.MODE_RTU)
			val = temp._ping(2, 1, 3)
			ping_devs.append(element)
		except Exception:
			pass
	print("Found device: " + str(ping_devs))


      
def reboot_device(device):
	print("Firmwaring device " + str(device) + " ...")
	data = bytearray([0x00,0x01])
	try:
		instr.custom_command(0xAA, str(data))
		#instr._performCommand(0xAA, str(data))
		print('REBOOT DEVICE:SUCCES') 
		return 1 
	except IOError:
		print("REBOOT DEVICE:FAILED: IOerror(No answer from device)")
		sys.exit(-1)
	except ValueError:
		print("REBOOT DEVICE:FAILED: ValueError")
		sys.exit(-1)



def send_parts(packet,parts):
	global instr
	packet_array = struct.pack(">H",int(packet))
	parts_array = struct.pack(">H",int(parts))
	data = bytearray([packet_array[0],packet_array[1],parts_array[0],parts_array[1]])

	bad_count = 0 
	while True:
		try:
			instr.custom_command(0xAB, str(data))
			#instr._performCommand(0xAB, str(data))
			print('SEND DATA SIZE:SUCCES') 
			return 1
		#except Exception as e:
		#	print(e)	
		except IOError:
			bad_count = bad_count + 1
		except ValueError:	
			bad_count = bad_count + 1
		if bad_count > 150:
			print("SEND_PARTS:FAILED")
			sys.exit(-1)


def send_data(packet,parts):
	global instr
	a = 0
	while a <= parts + 1:
		k = 0
		data = bytearray([])
		parts_temp = struct.pack(">H",int(a))
		data.append(parts_temp[0])
		data.append(parts_temp[1]) 
		while k < packet:
			if (k+packet*a) < len(b): 
				data.append(b[k+packet*a])
			else:
				data.append(b[k+7*a])
			k = k + 1   
		try:
			instr.custom_command(0xAC, str(data))
			#instr._performCommand(0xAC, str(data))
		except IOError:
			print("SEND_DATA:FAILED: IOerror(No answer from device)")
			sys.exit(-1)
		except ValueError:
			print("SEND_DATA:FAILED: ValueError")
			sys.exit(-1)
		a = a + 1 
	print('WRITING FIRMWARE:SUCCES')	


def set_params(id):
	version = instr._read_registers(2,1,3)
	print(version[0])
	instr._write_register(3,8198,signed=False)
	instr._write_register(4,34429,signed=False) 
	instr.set_Speed_PID_P(15)
	instr.set_Speed_PID_I(0.01)
	instr.set_Speed_PID_D(10)	 
	instr.set_Pos_PID_P(0.1)
	instr.set_Pos_PID_I(0)
	instr.set_Pos_PID_D(0.5)
	instr._write_register(0,10,signed=False)
	instr._write_register(40,0xACDC,signed=False)
	instr._write_register(28,1000,signed=False)		
	instr._write_register(40,0xDEAD,signed=False)

def boot(id):
	global mod_port
	global instr
	
	instr = Servo.Servo(mod_port,id)
	instr.debug = False
	reboot_device(id)
	send_parts(packet,parts)
	time.sleep(1)
	send_data(packet,parts)
	print("Rebooting device")
	time.sleep(8)
	set_params(id)
	print("FIRMWARING FINISHED!")


b = open('servo.bin', "rb").read()
parts = (len(b)/packet)


ping()
#boot(33)
boot(ping_devs[0])
