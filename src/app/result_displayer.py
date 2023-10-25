# file: result_displayer.py
import tkinter as tk
from PIL import ImageTk, Image

class ResultDisplayer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root)
        self.canvas.pack()

    def display(self, result_image_path):
        result_image = Image.open(result_image_path)
        result_image_tk = ImageTk.PhotoImage(result_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=result_image_tk)
        self.root.mainloop()
