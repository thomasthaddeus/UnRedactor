# file: char_tester.py
import cv2
import numpy as np
from styler import Styler

class CharTester:
    def __init__(self, image_processor, styler):
        self.image_processor = image_processor
        self.styler = styler

    def test_characters(self, character_set):
        for char in character_set:
            styled_char_image = self.styler.style_char(char)
            score = self.compare(styled_char_image, self.image_processor.image)
            print(f'Character: {char}, Score: {score}')

    def compare(self, styled_char_image, original_image):
        # Implement comparison logic, e.g., using OpenCV template matching
        result = cv2.matchTemplate(np.array(original_image), np.array(styled_char_image), cv2.TM_CCOEFF_NORMED)
        _, score, _, _ = cv2.minMaxLoc(result)
        return score
