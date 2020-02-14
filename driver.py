import usb.core
import usb.util
import time
import signal

def clear():
	for i in range(0,99):
		print()
def byeeeee(a,b):
	clear()
	print("""

   ad8888              
  d8"   ""              
  88                    
MM88MMM 88 8b,dPPYba,   
  88    88 88P'   `"8a  
  88    88 88       88  
  88    88 88       88  
  88    88 88       88  
                        
		                                                
		""")
	device.reset()
	exit(0)

def map_dis(output):
	keys = ''
	if output[4] == 72:
		keys = keys + 'B '
	elif output[4] == 40:
		keys = keys + 'A '
	elif output[4] == 136:
		keys = keys + 'Y '
	elif output[4] == 24:
		keys = keys + 'X '
	elif output[4] == 0:
		keys = keys + '↑ '
	elif output[4] == 4:
		keys = keys + '↓ '
	elif output[4] == 2:
		keys = keys + '→ '
	elif output[4] == 6:
		keys = keys + '← '	
	else:
		pass
	if output[5] == 1:
		keys = keys + 'L1 '
	elif output[5] == 4:
		keys = keys + 'L2 '
	elif output[5] == 2:
		keys = keys + 'R1 '
	elif output[5] == 8:
		keys = keys + 'R2 '
	elif output[5] == 16:
		keys = keys + 'BACK'
	elif output[5] == 32:
		keys = keys + 'START'
	elif output[5] == 128:
		byeeeee(6,9)	
	else:
		pass
	keys = keys + '    ||         	RIGHT : ({},{})   LEFT :({},{})'.format(output[0],output[1],output[2],output[3])
	return keys

signal.signal(signal.SIGINT,byeeeee)	
device = usb.core.find(idVendor=0x046d,idProduct=0xc218)

if device is None:
	raise ValueError("No device connected.")

if device.is_kernel_driver_active(0):
	print("Disabling kernel control")
	device.detach_kernel_driver(0)

device.set_configuration()
print("success")

while True:
	output = None
	try:
		output = device.read(0x81,8)
	except:
		pass
	if output is not None:
		print(map_dis(output))
	time.sleep(0.01)
