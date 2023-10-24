# file: styler.py
import tkinter as tk
from tkinter import font

class Styler:
    def __init__(self, root):
        self.root = root
        self.font = font.Font(family="Helvetica", size=12)  # Set initial font properties

    def style_char(self, char):
        label = tk.Label(self.root, text=char, font=self.font)
        label.pack()
        self.root.update_idletasks()  # Update to ensure correct rendering
        return label  # Return label for further processing
