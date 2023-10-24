# file: image_processor.py
from PIL import Image

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def crop_image(self, crop_area):
        self.image = self.image.crop(crop_area)

    def get_block_size(self):
        # Assuming each block is square and the image is evenly pixelated
        for y in range(self.image.height):
            if self.image.getpixel((0, y)) != self.image.getpixel((0, y+1)):
                return y + 1  # Block size is the y-coordinate at which color changes

    def save_image(self, path):
        self.image.save(path)
