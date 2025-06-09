import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

from citra_grayscale_biner_histogram import GrayscaleBinerHistogram
from citra_edge_erosi import EdgeAndErosi
from citra_aritmatika_logika import AritmatikaLogika

class CitraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengolahan Citra Digital")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f5f7fa")
        self.image = None

        title = tk.Label(root, text="🖼️ Aplikasi Pengolahan Citra Digital", font=("Segoe UI", 20, "bold"), bg="#f5f7fa", fg="#2c3e50")
        title.pack(pady=10)

        main_frame = tk.Frame(root, bg="#f5f7fa")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.sidebar = tk.Frame(main_frame, width=250, bg="#ecf0f1", bd=2, relief="groove")
        self.sidebar.pack(side="left", fill="y", padx=(0, 20))

        self.image_frame = tk.Frame(main_frame, width=720, height=500, bg="white", relief="ridge", bd=2)
        self.image_frame.pack(side="right", fill="both", expand=True)
        self.panel = tk.Label(self.image_frame, bg="white")
        self.panel.pack(expand=True)

        self.style_button = {
            "font": ("Segoe UI", 10),
            "bg": "#3498db",
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "width": 22,
            "bd": 0,
            "padx": 8,
            "pady": 8,
            "anchor": "w",
            "justify": "left"
        }

        self.grayscale_ops = GrayscaleBinerHistogram(self)
        self.edge_ops = EdgeAndErosi(self)
        self.logic_ops = AritmatikaLogika(self)

        self._add_button("📁 Load Gambar", self.load_image)
        self._add_button("🌑 Grayscale", self.grayscale_ops.to_grayscale)
        self._add_button("⬛ Biner", self.grayscale_ops.to_binary)
        self._add_button("📊 Histogram", self.grayscale_ops.show_histogram)
        self._add_button("🪞 Edge Detection", self.edge_ops.edge_detection)
        self._add_button("🧱 Erosi", self.edge_ops.erosion)
        self._add_button("➕ Aritmatika (+)", self.logic_ops.arithmetic_addition)
        self._add_button("🔁 Logika NOT", self.logic_ops.logic_not)

        tk.Button(self.sidebar, text="❌ Keluar", command=self.root.quit,
                  font=("Segoe UI", 10, "bold"),
                  bg="#e74c3c", fg="white",
                  width=22, pady=10).pack(pady=10, side="bottom")

    def _add_button(self, label, command):
        tk.Button(self.sidebar, text=label, command=command, **self.style_button).pack(pady=5, padx=10, anchor="w")

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if path:
            image = cv2.imread(path)
            if image is None:
                messagebox.showerror("Error", "Gagal membuka gambar.")
                return
            self.image = image
            self.show_image(self.image)

    def show_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((720, 500))
        imgtk = ImageTk.PhotoImage(image=img_pil)
        self.panel.imgtk = imgtk
        self.panel.config(image=imgtk)

    def _check_image(self):
        if self.image is None:
            messagebox.showwarning("Peringatan", "Silakan load gambar terlebih dahulu!")
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = CitraApp(root)
    root.mainloop()
