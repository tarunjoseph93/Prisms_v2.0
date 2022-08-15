from PyQt6.QtCore import pyqtSignal, pyqtSlot,QThread, Qt
import numpy as np
import andor3
import logging

class Thread(QThread):
    image_acquired = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        try:
            # Initialise the camera and start acquiring frames using the FrameServer helper
            self.cam = andor3.Andor3()
            # Do whatever camera configuration desired here...
            self.cam.SensorCooling = True
            self.cam.FanSpeed = 1
            self.cam.TriggerMode = 0
            self.cam.ExposureTime = 0.001
            # Always keep at 30fps, otherwise video will freeze due to USB 3.0's high bandwidth.
            self.cam.FrameRate = 30
            self.cam.ElectronicShutteringMode = 0
            self.cam.PixelReadoutRate = 3
            self.cam.PixelEncoding = 2
            self.cam.SpuriousNoiseFilter = True
            self.cam.StaticBlemishCorrection = False
            self.cam.MetadataEnable = False
            self.cam.FastAOIFrameRateEnable = True
            self.cam.AOIHeight = self.cam.max("AOIHeight")
            self.cam.VerticallyCentreAOI = True
            self.cam.AOILeft = 1
            self.cam.AOIWidth = self.cam.max("AOIWidth")

            # Create the FrameServer helper and start it serving frames in a background thread
            # It will call the frame_callback method when new image data is available
            self.fsvr = andor3.FrameServer(self.cam, self.frame_callback)
            self.fsvr.start(frame_rate_max=60)
        except:
            logging.exception("Unable to initialise Andor3 camera!")

    def stop(self):
        self.fsvr.stop()
        self._run_flag = False
        self.wait()

    def frame_callback(self, n, data, timestamp):
        """
        Handle image data streamed by the Andor FrameServer.

        This just emits the Qt Signal so that the UI can then be updated within the Qt event loop.
        Any changes to the Qt UI elements should only be performed within the Qt event loop thread,
        otherwise bad things will happen...
        """
        self.image_acquired.emit(data)

