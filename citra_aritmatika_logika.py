import cv2
import numpy as np

class AritmatikaLogika:
    def __init__(self, app):
        self.app = app

    def arithmetic_addition(self):
        if self.app._check_image():
            added = cv2.add(self.app.image, np.full(self.app.image.shape, 50, dtype=np.uint8))
            self.app.show_image(added)

    def logic_not(self):
        if self.app._check_image():
            logic = cv2.bitwise_not(self.app.image)
            self.app.show_image(logic)
