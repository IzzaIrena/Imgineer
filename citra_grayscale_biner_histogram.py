import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class GrayscaleBinerHistogram:
    def __init__(self, app):
        self.app = app

    def to_grayscale(self):
        if self.app._check_image():
            gray = cv2.cvtColor(self.app.image, cv2.COLOR_BGR2GRAY)
            self.app.show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

    def to_binary(self):
        if self.app._check_image():
            gray = cv2.cvtColor(self.app.image, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            self.app.show_image(cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR))

    def show_histogram(self):
        if self.app._check_image():
            color = ('b', 'g', 'r')
            plt.figure("Histogram RGB")
            for i, col in enumerate(color):
                hist = cv2.calcHist([self.app.image], [i], None, [256], [0, 256])
                plt.plot(hist, color=col)
                plt.xlim([0, 256])
            plt.title("Histogram Warna")
            plt.xlabel("Intensitas")
            plt.ylabel("Jumlah Piksel")
            plt.grid(True)
            plt.show()
