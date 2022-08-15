import struct

def resetWheelWithStruct():
	response = int("11111011", 2)
	writtenResponse = struct.pack(">B", response)
	return writtenResponse

def resetWheelResponse(msg):
	unpackMsg = struct.unpack(">B", msg)
	unpackHexMsg = bytes.hex(unpackMsg)
	return str(unpackHexMsg)

def convertFilterWheelValues(msg):
	wheelA = "0"
	response = wheelA + msg
	print(response)
	print(type(response))
	intResponseFilterWheel = int(response, 2)
	writtenResponse = struct.pack(">B", intResponseFilterWheel)
	print(writtenResponse)
	return writtenResponse

