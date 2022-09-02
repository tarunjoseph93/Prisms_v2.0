USER MANUAL FOR PRISMS II PYTHON APPLICATION

1. Minimum Hardware Requirements
The minimum hardware requirements to run the PRISMS II Python Application are as follows:
1.	Operating system: Windows 7/10/11 (x64, x86)
2.	RAM: minimum 2 GB
3.	Memory: minimum 1 GB
4.	USB ports: 3 minimum required, 1 being USB 3.0

2. Devices Used
The devices that connect via USB are as follows: 
1.	Zaber Motion mount (USB 2.0)
2.	Filter Wheel (USB 2.0)
3.	Andor Zyla 4.2 Camera (USB 3.0)
4.	Laptop/Computer/Raspberry Pi

3. Software Requirements
The minimum software requirements are as follows: 
1.	Andor SDK 3 (This is proprietary software. If you have purchased this product, please look up the download link here: https://andor.oxinst.com/products/software-development-kit/)
2.	Python 3.10 with Pip 3 version 22.1 minimum (For Python 3.10 download and installation, go to the download link here: https://www.python.org/downloads/)
3.	PyCharm Community Edition (Download PyCharm via this download link: https://www.jetbrains.com/pycharm/download/#section=windows)
4.	Important Python packages such as: 
a.	Andor 3 PyPi package - https://pypi.org/project/andor3/
b.	Zaber Motion Python package - https://www.zaber.com/software/docs/motion-library/ascii/
c.	PyQt6
d.	PySerial
e.	Struct
f.	PyQtGraph
g.	Numba (optional)
Dependencies on these library packages such as NumPy will be installed through packages like Andor 3. 

4. PRISMS II Working
1.	Open PyCharm Community edition and open the folder containing the source code.
2.	Before running the application, make sure all Python packages are installed. Import all relevant packages for Python 3.10 and make sure the Python interpreter is set to Python 3.10 as well. Install all packages with the help of Project Settings and Python Interpreter by adding it through the “+” symbol or simply import all packages via the import statements at the head of the code in the root directory.
3.	Check the constants.py file for configuration settings. COM ports relevant to Zaber Motion and Filter Wheel will need to be modified according to their respective COM port numbers described in system settings once connected. 
4.	Set the local file path in the constants.py file. 
5.	Do not change the framerate of the camera. The default framerate is 30 frames per second. 
6.	The options for the camera are as follows: 
a.	SensorCooling: Boolean (rw)
value=False
b.	FanSpeed: Enumerated (rw)
value = 1
c.	TriggerMode: Enumerated (rw)
-> 0: Internal
     2: External Start
     3: External Exposure
     4: Software
     6: External
d.	ExposureTime: Floating Point (rw)
value=9.6e-06 min=9.6e-06 max=30
e.	Framerate: Integer (rw)
value = 30
f.	ElectronicShutteringMode: Enumerated (rw)
-> 0: Rolling
g.	PixelReadoutRate: Enumerated (rw)
    1: 100 MHz
-> 3: 270 MHz
h.	PixelEncoding: Enumerated (rw)
-> 0: Mono12
1: Mono12Packed
2: Mono16
9: Mono32
i.	SpuriousNoiseFilter: Boolean (rw)
value=True
j.	StaticBlemishCorrection: Boolean (rw)
value=True
k.	MetadataEnable: Boolean (rw)
value=False
l.	FastAOIFrameRateEnable: Boolean (rw)
value=False
m.	VerticallyCentreAOI: Boolean (rw)
value=False
The complete constants.py file is given in the figure below:
 
Figure 1: Constants.py
7.	Save the constants.py file.
8.	Make sure all the serial ports are connected to their respective devices. Also, be sure to check if each device is powered on and if the Andor Zyla 4.2 Camera is connected to a USB 3.0 port or not. 
9.	Run the application from the MainWindowGUI.py file. 
10.	COM checks should pass provided the correct COM ports are given in the constants.py file and the serial ports are connected. 
11.	The application should be ready to go. The PyGraph’s Graphical Widget should display a black and white video feed from the camera. 
12.	When saving a picture, make sure the file path specified in the constants.py file has write permissions.

The overall GUI should look like this: 
 
Figure 2: PRISMS II GUI
The figure above has a blank screen when it comes to the video feed. This was a sample GUI taken without the camera connected. Log messages should appear to the right of the screen in the plain text field. 
Below that is the filter wheel controls where the dropdown has filters from 0-9. Once selected, the set filter button is clicked, and the filter should change its position on the device. The reset filter button is used to reset the filter back to its default value, which is 0. 
Below the filter wheel controls are the Zaber motion controls. There are 4 text fields, that can take integer values for their corresponding direction, signified by the direction button next to it. If the text field is empty and the direction button is clicked, a relative motion of 1 degree in the direction specified is triggered. If the text field is populated with an integer and the corresponding direction button is clicked, the Zaber motion device moves in the absolute direction of the given value. The reset Zaber motion button calls the home function and resets the Zaber motion device to 0, both horizontally and vertically. 
The Start Video button, on the bottom-left corner of the main window, is initially invisible as the video should start of the application. The save button next to it, if clicked, stops the video thread and saves the last image gathered from the Zyla Camera as a binary file with a timestamp as its name. This file is saved to the file path specified in the constants.py folder. The start video button becomes visible once this action is complete and the save button becomes invisible, until the video starts again. 
