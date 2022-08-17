from PyQt6.QtCore import QThread
import zaber_movements.moves as mv

class MovementMain():
    def __init__(self, direction, value, parent=None):
        self.MovementActive = None
        self.direction = direction
        self.value = value

    def start(self):
        self.MovementActive = True
        while self.MovementActive:
            if self.direction == "up":
                if self.value == 1:
                    mv.relativeMovement(self.direction, self.value)
                else:
                    mv.absoluteMovement(self.direction, self.value)
            self.stop()

            if self.direction == "down":
                if self.value == -1:
                    mv.relativeMovement(self.direction, self.value)
                else:
                    mv.absoluteMovement(self.direction, self.value)
            self.stop()

            if self.direction == "left":
                if self.value == -1:
                    mv.relativeMovement(self.direction, self.value)
                else:
                    mv.absoluteMovement(self.direction, self.value)
            self.stop()

            if self.direction == "right":
                if self.value == 1:
                    mv.relativeMovement(self.direction, self.value)
                else:
                    mv.absoluteMovement(self.direction, self.value)
            self.stop()

    def stop(self):
        self.MovementActive = False