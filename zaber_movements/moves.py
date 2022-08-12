from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
import constants

serialPortName = constants.ZABER_SERIAL_PORT_NAME

def relativeMovement(direction, value):
    with Connection.open_serial_port(serialPortName) as connection:
        device_list = connection.detect_devices()

        rotationDevice = device_list[0]
        verticalDevice = device_list[1]

        rotationAxis = rotationDevice.get_axis(1)
        # rotationAxis.home()
        verticalAxis = verticalDevice.get_axis(1)
        # verticalAxis.home()

        if direction == 'up':
            verticalAxis.move_relative(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()
        elif direction == 'down':
            verticalAxis.move_relative(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()
        elif direction == 'left':
            rotationAxis.move_relative(value, Units.ANGLE_DEGREES)
            rotationAxis.stop()
        elif direction == 'right':
            rotationAxis.move_relative(value, Units.ANGLE_DEGREES)
            rotationAxis.stop()

def absoluteMovement(direction, value):
    with Connection.open_serial_port(serialPortName) as connection:
        device_list = connection.detect_devices()

        rotationDevice = device_list[0]
        verticalDevice = device_list[1]

        rotationAxis = rotationDevice.get_axis(1)
        # rotationAxis.home()
        verticalAxis = verticalDevice.get_axis(1)
        # verticalAxis.home()

        if direction == 'up':
            verticalAxis.move_absolute(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()
        elif direction == 'down':
            verticalAxis.move_absolute(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()
        elif direction == 'left':
            rotationAxis.move_absolute(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()
        elif direction == 'right':
            rotationAxis.move_absolute(value, Units.ANGLE_DEGREES)
            verticalAxis.stop()

def home():
    with Connection.open_serial_port(serialPortName) as connection:
        device_list = connection.detect_devices()

        rotationDevice = device_list[0]
        verticalDevice = device_list[1]

        rotationAxis = rotationDevice.get_axis(1)
        verticalAxis = verticalDevice.get_axis(1)

        rotationAxis.home()
        verticalAxis.home()