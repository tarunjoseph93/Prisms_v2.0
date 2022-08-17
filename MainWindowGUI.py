# Form implementation generated from reading ui file 'MainWindowGUI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal, pyqtSlot,QThread, Qt
import sys
import zaber_movements
import constants as con
import serial
import pyqtgraph as pg

from datetime import datetime
from matplotlib import pyplot as plt
from PIL import Image
from filter_wheel import filters_and_speeds as fns
from filter_wheel import filter_wheel_connections as cfw

from zaber_movements.movement_main import MovementMain
from zyla_camera import camera_thread as ct


class Ui_PrismsMainWindow(object):
    def setupUi(self, PrismsMainWindow):
        PrismsMainWindow.setObjectName("PrismsMainWindow")
        PrismsMainWindow.resize(1280, 768)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        PrismsMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PrismsMainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Zyla Camera Vertical Layout
        self.CameraVerticalLayout = QtWidgets.QVBoxLayout()
        self.CameraVerticalLayout.setObjectName("CameraVerticalLayout")
        self.verticalLayout_4.addLayout(self.CameraVerticalLayout)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.StartVideoPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartVideoPushButton.setObjectName("StartVideoPushButton")
        self.horizontalLayout_7.addWidget(self.StartVideoPushButton)
        self.SavePicturePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SavePicturePushButton.setObjectName("SavePicturePushButton")
        self.horizontalLayout_7.addWidget(self.SavePicturePushButton)
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setObjectName("HomePushButton")
        self.horizontalLayout_7.addWidget(self.HomePushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LogPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LogPlainTextEdit.setObjectName("LogPlainTextEdit")
        self.verticalLayout_3.addWidget(self.LogPlainTextEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SelectFilterWheelLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectFilterWheelLabel.setObjectName("SelectFilterWheelLabel")
        self.horizontalLayout_6.addWidget(self.SelectFilterWheelLabel)
        self.FilterWheelComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.FilterWheelComboBox.setObjectName("FilterWheelComboBox")
        self.horizontalLayout_6.addWidget(self.FilterWheelComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ResetFilterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetFilterPushButton.setObjectName("ResetFilterPushButton")
        self.horizontalLayout_5.addWidget(self.ResetFilterPushButton)
        self.SetFilterPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetFilterPushButton.setObjectName("SetFilterPushButton")
        self.horizontalLayout_5.addWidget(self.SetFilterPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.UpLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UpLineEdit.setInputMask("")
        self.UpLineEdit.setText("")
        self.UpLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.UpLineEdit.setPlaceholderText("Enter Up Value")
        self.UpLineEdit.setObjectName("UpLineEdit")
        self.horizontalLayout.addWidget(self.UpLineEdit)
        self.UpPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpPushButton.setObjectName("UpPushButton")
        self.horizontalLayout.addWidget(self.UpPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DownLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DownLineEdit.setInputMask("")
        self.DownLineEdit.setText("")
        self.DownLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DownLineEdit.setPlaceholderText("Enter Down Value")
        self.DownLineEdit.setObjectName("DownLineEdit")
        self.horizontalLayout_2.addWidget(self.DownLineEdit)
        self.DownPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownPushButton.setObjectName("DownPushButton")
        self.horizontalLayout_2.addWidget(self.DownPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RightLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RightLineEdit.setInputMask("")
        self.RightLineEdit.setText("")
        self.RightLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RightLineEdit.setPlaceholderText("Enter Right Value")
        self.RightLineEdit.setObjectName("RightLineEdit")
        self.horizontalLayout_3.addWidget(self.RightLineEdit)
        self.RightPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightPushButton.setObjectName("RightPushButton")
        self.horizontalLayout_3.addWidget(self.RightPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LeftLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LeftLineEdit.setInputMask("")
        self.LeftLineEdit.setText("")
        self.LeftLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LeftLineEdit.setPlaceholderText("Enter Left Value")
        self.LeftLineEdit.setObjectName("LeftLineEdit")
        self.horizontalLayout_4.addWidget(self.LeftLineEdit)
        self.LeftPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftPushButton.setObjectName("LeftPushButton")
        self.horizontalLayout_4.addWidget(self.LeftPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.ResetZaberPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetZaberPushButton.setObjectName("ResetZaberPushButton")
        self.verticalLayout.addWidget(self.ResetZaberPushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        PrismsMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrismsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PrismsMainWindow)

        # Zyla Camera GUI Connection code
        self.glw = pg.GraphicsLayoutWidget()
        self.CameraVerticalLayout.addWidget(self.glw)

        # Create the ploting axes in the GraphicsLayoutWidget
        self.plot = self.glw.addPlot()
        self.plot.setLabels(left="Pixel Height", bottom="Pixel Width")
        # Create the image item and add it to the plot
        self.image = pg.ImageItem()
        self.plot.addItem(self.image)

        # Adding stretch values to GUI elements and layouts
        self.horizontalLayout_8.setStretch(0, 1)

        # Create object of Camera Thread class
        self.camThread = ct.CameraThread()
        # Connect the image acquired Signal to a handler
        self.camThread.image_acquired.connect(self.update_image)

        # Starting Camera Thread
        self.startVideoAction()

        # Initialisation of image save property
        self.last_image = None

        # Connection Home button to home action
        self.HomePushButton.clicked.connect(self.homeAction)

        # Connection to Start Video Button to start video Action
        self.StartVideoPushButton.clicked.connect(self.startVideoAction)

        # Connection to save image button to save image action
        self.SavePicturePushButton.clicked.connect(self.savePictureAction)

        # Filter Wheel GUI Connection code
        self.filterWheelCheck()

        # Setting lists from filters_and_speeds.py
        self.FilterWheelComboBox.addItems(fns.filterList)

        # Setting default values for the list
        self.FilterWheelComboBox.setCurrentIndex(fns.filterList.index("5"))

        # Reset Filter Wheel
        self.ResetFilterPushButton.clicked.connect(self.resetFilterAction)

        # Set Filter Wheel
        self.SetFilterPushButton.clicked.connect(self.setFilterAction)

        # Zaber Motion GUI connection code
        self.zaberSerialCheck()

        self.ResetZaberPushButton.clicked.connect(self.resetZaberMotion)
        self.UpPushButton.clicked.connect(self.upClick)
        self.DownPushButton.clicked.connect(self.downClick)
        self.RightPushButton.clicked.connect(self.rightClick)
        self.LeftPushButton.clicked.connect(self.leftClick)

    # Zyla Camera Functions
    # Slot for video feed data acquisition from Camera Thread
    def update_image(self, data):
        """
        Update the plot with new image data.

        This should only be called from within the Qt event loop thread, such as when the
        appropriate Signal is emitted.
        """
        # Store reference to data in image storage property
        self.last_image = data

        self.image.setImage(data)

    # Save Picture from update_image()
    def savePicture(self):
        print(f"Data from last image: {self.last_image}")
        print(f"Dimensions from last image: {self.last_image.ndim}")
        print(f"Shape from last image: {self.last_image.shape}")
        print(f"Size of last image: {self.last_image.size}")

        self.dt = datetime.now()
        self.ts = datetime.timestamp(self.dt)
        self.date_time = datetime.fromtimestamp(self.ts)
        self.str_date_time = self.date_time.strftime("%d_%m_%Y_%H_%M_%S")

        print(self.str_date_time)

        self.new_file = open(f'{con.PATH_TO_SAVE_IMAGE}\\{self.str_date_time}.bin', 'w')
        self.last_image.astype('int16').tofile(self.new_file)
        self.new_file.close()

        # plt.imshow(data, cmap="gray")
        # plt.show()
        # im = Image.fromarray(data)
        # im.save(f"my_image.jpeg")

    # Start Video function
    def startVideoAction(self):
        self.StartVideoPushButton.setEnabled(False)

        # if self.pictureThread.isRunning():
        #     self.pictureThread.stop()

        self.SavePicturePushButton.setEnabled(True)
        self.camThread.start()

    # Save Image Function
    def savePictureAction(self):
        self.SavePicturePushButton.setEnabled(False)
        self.camThread.stop()
        self.savePicture()
        self.StartVideoPushButton.setEnabled(True)
        # self.pictureThread.start()

    def homeAction(self):
        msg = "Home set. Reset complete."
        self.resetZaberMotion()
        self.resetFilterAction()
        self.logSend(msg)

    # Filter Wheel Functions
    def resetFilterAction(self):
        reset = cfw.resetWheel()
        self.logSend(reset)

    def setFilterAction(self):
        currentFilter = int(self.FilterWheelComboBox.currentText())
        currentSpeed = 7
        msg = cfw.setFilterWheel(currentFilter, currentSpeed)
        self.logSend(msg)
        # self.filterLog.setPlainText("Filter: {0}; Speed: {1}".format(currentFilter, currentSpeed))

    def filterWheelCheck(self):
        try:
            filterWheelSerialPortObj = serial.Serial(con.FILTER_WHEEL_PORT_NAME)

            if filterWheelSerialPortObj.isOpen():
                print('\nPort Open! \nStatus -> ', filterWheelSerialPortObj)
        except:
            self.filterPopupFalse()

    def filterPopupFalse(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(f"Filter Wheel {con.FILTER_WHEEL_PORT_NAME} Port not found!")
        msg.setText(
            f"Could not find {con.FILTER_WHEEL_PORT_NAME} port for Filter Wheel. Check the port again and the connection!")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        x = msg.exec()


    # Zaber Motion Functions
    def zaberSerialCheck(self):
        try:
            serialPortObj = serial.Serial(con.ZABER_SERIAL_PORT_NAME)

            if serialPortObj.isOpen():
                print('\nPort Open! \nStatus -> ', serialPortObj)

        except:
            self.zaberPopupFalse()

    def zaberPopupFalse(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(f"Zaber {con.ZABER_SERIAL_PORT_NAME} Port not found!")
        msg.setText(
            f"Could not find {con.ZABER_SERIAL_PORT_NAME} port for Zaber Motion. Check the port again and the connection!")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        x = msg.exec()

        # Zaber Motion GUI functions

    def resetZaberMotion(self):
        msg = "You've clicked the Reset Zaber Motion Button."
        self.logSend(msg)

        zaber_movements.moves.home()

    def upClick(self):
        msg = "You've clicked the Up Button."
        self.logSend(msg)

        direction = 'up'

        if self.UpLineEdit.text() == '':
            value = 1
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        else:
            value = int(self.UpLineEdit.text())
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        self.UpLineEdit.clear()

    def downClick(self):
        msg = "You've clicked the Down Button."
        self.logSend(msg)

        direction = 'down'

        if self.DownLineEdit.text() == '':
            value = -1
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        else:
            value = -abs(int(self.DownLineEdit.text()))
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        self.DownLineEdit.clear()

    def rightClick(self):
        msg = "You've clicked the Right Button."
        self.logSend(msg)

        direction = 'right'

        if self.RightLineEdit.text() == '':
            value = 1
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        else:
            value = int(self.RightLineEdit.text())
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        self.RightLineEdit.clear()

    def leftClick(self):
        msg = "You've clicked the Left Button."
        self.logSend(msg)

        direction = 'left'

        if self.LeftLineEdit.text() == '':
            value = -1
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        else:
            value = -abs(int(self.LeftLineEdit.text()))
            self.move = zaber_movements.movement_main.MovementMain(direction, value)
            self.move.start()
            msg = f"Moved {direction} with value {value}"
            self.logSend(msg)
        self.LeftLineEdit.clear()

        # Send to Plain Text Log on the GUI

    def logSend(self, msg):
        self.LogPlainTextEdit.appendPlainText(msg)

    def closeEvent(self, event):
        self.camThread.stop()
        event.accept()

    def retranslateUi(self, PrismsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PrismsMainWindow.setWindowTitle(_translate("PrismsMainWindow", "PRISMS v2.0"))
        self.StartVideoPushButton.setText(_translate("PrismsMainWindow", "Start Video"))
        self.SavePicturePushButton.setText(_translate("PrismsMainWindow", "Save"))
        self.HomePushButton.setText(_translate("PrismsMainWindow", "Home"))
        self.SelectFilterWheelLabel.setText(_translate("PrismsMainWindow", "Select Filter Wheel:"))
        self.ResetFilterPushButton.setText(_translate("PrismsMainWindow", "Reset Filter"))
        self.SetFilterPushButton.setText(_translate("PrismsMainWindow", "Set Filter"))
        self.UpPushButton.setText(_translate("PrismsMainWindow", "UP"))
        self.DownPushButton.setText(_translate("PrismsMainWindow", "DOWN"))
        self.RightPushButton.setText(_translate("PrismsMainWindow", "RIGHT"))
        self.LeftPushButton.setText(_translate("PrismsMainWindow", "LEFT"))
        self.ResetZaberPushButton.setText(_translate("PrismsMainWindow", "Reset Zaber Motion"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    PrismsMainWindow = QtWidgets.QMainWindow()
    ui = Ui_PrismsMainWindow()
    ui.setupUi(PrismsMainWindow)
    PrismsMainWindow.show()
    sys.exit(app.exec())
