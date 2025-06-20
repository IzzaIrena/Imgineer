import cv2
import numpy as np

class EdgeAndErosi:
    def __init__(self, app):
        self.app = app

    def edge_detection(self):
        if self.app._check_image():
            gray = cv2.cvtColor(self.app.image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            self.app.show_image(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

    def erosion(self):
        if self.app._check_image():
            # Structuring Element 1: Baris Tengah
            se1 = np.array([[0,0,0],
                            [1,1,1],
                            [0,0,0]], dtype=np.uint8)
            eroded1 = cv2.erode(self.app.image, se1, iterations=1)

            # Structuring Element 2: Diagonal Cross
            se2 = np.array([[1,0,1],
                            [0,1,0],
                            [1,0,1]], dtype=np.uint8)
            eroded2 = cv2.erode(self.app.image, se2, iterations=1)

            # Labeling visuals
            label_height = 80
            width1, width2 = eroded1.shape[1], eroded2.shape[1]
            label1 = np.full((label_height, width1, 3), 255, dtype=np.uint8)
            label2 = np.full((label_height, width2, 3), 255, dtype=np.uint8)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(label1, "SE: Tengah Horizontal", (10, 50), font, 1.2, (0,0,0), 3, cv2.LINE_AA)
            cv2.putText(label2, "SE: Diagonal Cross", (10, 50), font, 1.2, (0,0,0), 3, cv2.LINE_AA)

            # Gap visual
            gap = 30
            gap_image = np.full((label_height + eroded1.shape[0], gap, 3), 255, dtype=np.uint8)

            # Combine
            combined = np.hstack((
                np.vstack((label1, eroded1)),
                gap_image,
                np.vstack((label2, eroded2))
            ))

            self.app.show_image(combined)
