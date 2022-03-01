from curses import baudrate
import serial
import time

ACCELEROMETER_STRING = "A"*11
EXT_TEMP_STRING = "E"*11
EXT_HUMIDITY_STRING = "H"*11
INT_TEMP_STRING = "T"*11
INT_HUMIDITY_STRING = "I"*11

accel_val = 0
ext_temp_val = 0
ext_humidity_val = 0
int_temp_val = 0
int_humidity_val = 0

s = serial.Serial('COM3', baudrate=9600)

while True:
	# accel value
	s.write(ACCELEROMETER_STRING)
	time.sleep(0.1)
	accel_val = s.readline().decode("UTF-8")

	# ext temp value
	s.write(EXT_TEMP_STRING)
	time.sleep(0.1)
	ext_temp_val = s.readline().decode("UTF-8")

	# ext humidity value
	s.write(EXT_HUMIDITY_STRING)
	time.sleep(0.1)
	ext_humidity_val = s.readline().decode("UTF-8")

	# int temp value
	s.write(INT_TEMP_STRING)
	time.sleep(0.1)
	int_temp_val = s.readline().decode("UTF-8")

	# int humidity
	s.write(INT_HUMIDITY_STRING)
	time.sleep(0.1)
	int_humidity_val = s.readline().decode("UTF-8")

	print(accel_val, ext_temp_val, ext_humidity_val, int_temp_val, int_humidity_val)