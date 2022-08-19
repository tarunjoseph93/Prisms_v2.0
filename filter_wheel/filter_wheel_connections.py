import serial
from filter_wheel import filter_conversion as conv
from filter_wheel import filters_and_speeds as fns
import constants as con

def resetWheel():
	with serial.Serial(con.FILTER_WHEEL_PORT_NAME, timeout=1) as filterSerial:
		response = conv.resetWheelWithStruct()
		filterSerial.write(response)
		s = filterSerial.readline()
		msg = bytes.hex(s, ' ')
		print(msg)
		# msg = conv.resetWheelResponse(s)
		return str(msg)

def setFilterWheel(filter, speed):
	with serial.Serial(con.FILTER_WHEEL_PORT_NAME, timeout=1) as filterSerial:
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
		filterSerial.write(filterWheelResponse)
		s = filterSerial.readline()
		msg = bytes.hex(s, ' ')
		print(msg)
		# msg = conv.resetWheelResponse(s)
		return str(msg)