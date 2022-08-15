import serial
from filter_wheel import filter_conversion as conv
from filter_wheel import filters_and_speeds as fns
import constants as con

ser = serial.Serial(con.FILTER_WHEEL_PORT_NAME, timeout=1)

def checkUSBConnection():
	msg1 = con.FILTER_WHEEL_PORT_NAME + ' is open'
	msg2 = con.FILTER_WHEEL_PORT_NAME + ' is closed'
	print(msg1) if ser.isOpen() else msg2
	return msg1 if ser.isOpen() else msg2

def resetWheel():
	response = conv.resetWheelWithStruct()
	ser.write(response)
	s = ser.readline()
	msg = bytes.hex(s, ' ')
	print(msg)
	# msg = conv.resetWheelResponse(s)
	return str(msg)

def setFilterWheel(filter, speed):
	filterValue = ''
	speedValue = ''
	for key, value in fns.filters.items():
		if key == filter:
			print("Found filter value: {}".format(value))
			filterValue = value
		# else:
		# 	msg = "Cannot find filter values"
		# 	return msg

	for key, value in fns.speeds.items():
		if key == speed:
			print("Found speed value: {}".format(value))
			speedValue = value
		# else:
		# 	msg = "Cannot find speed values"
		# 	return msg

	response = speedValue + filterValue
	print(response)
	filterWheelResponse = conv.convertFilterWheelValues(response)
	ser.write(filterWheelResponse)
	s = ser.readline()
	msg = bytes.hex(s, ' ')
	print(msg)
	# msg = conv.resetWheelResponse(s)
	return str(msg)