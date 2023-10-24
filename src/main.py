# file: main.py
from image_processor import ImageProcessor
from styler import Styler
from char_tester import CharTester
from result_displayer import ResultDisplayer
import tkinter as tk

def main():
    root = tk.Tk()
    image_processor = ImageProcessor('image_path.png')
    styler = Styler(root)
    char_tester = CharTester(image_processor, styler)
    result_displayer = ResultDisplayer(root)

    # Assume character_set and result_image_path are defined
    char_tester.test_characters(character_set)
    result_displayer.display(result_image_path)

    root.mainloop()

if __name__ == "__main__":
    main()
