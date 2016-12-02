import serial
from time import gmtime, strftime, localtime
import time
from serial.tools import list_ports

ports = list(list_ports.comports())
print("There are %d COM port(s) found" % len(ports))
print("==============================")
for x in xrange(0,len(ports)):
	print("[%d] %s" % (x,ports[x][1]))
	pass
print("==============================")

x = raw_input(">>> Choose COM port(Enter number): ")
Serial = serial.Serial(ports[int(x)][0],57600)
time.sleep(3)

Serial.write("C\r")
print Serial.readline()
print Serial.readline()
time.sleep(1)
Serial.write("GO 0 0\r")
time.sleep(1)
while Serial.inWaiting()>0:
	print Serial.readline()
	pass
f = open("cradio.ihx","r")
time.sleep(3)


for line in f:
	Serial.write(line)
	print "Data>>%s" % line
	print Serial.readline()
	print Serial.readline()
	print Serial.readline()
	pass
