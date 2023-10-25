# We'll translate the utility functions step by step. Let's start with getBlueMargin.

def get_blue_margin(image):
    rowsize = image.width * 4
    margin = 0
    center = 0
    found = False

    # Scan a single row, in the middle to detect the blue box
    for x in range(image.width):
        y = image.height // 2
        red, green, blue = image.getpixel((x, y))
        if not found and blue == 255 and green != 255 and red != 255:
            found = True
            margin = x
            break

    # Find the vertical center point of the blue box
    found = False
    top_blue = 0
    bot_blue = 0
    for y in range(image.height):
        x = margin + 5
        red, green, blue = image.getpixel((x, y))
        if not found and blue == 255 and green != 255 and red != 255:
            found = True
            top_blue = y
        elif found and blue == 255 and green == 255 and red == 255:
            found = False
            bot_blue = y

    center = (top_blue + bot_blue) // 2
    return margin, center

# We'll translate the other utility functions step by step. Next is getMargins.

def get_margins(image):
    rowsize = image.width * 4
    hit_red = False
    left_edge = 0

    # Scan a single row, in the middle
    for x in range(image.width):
        y = image.height // 2
        red, green, blue = image.getpixel((x, y))

        # Detecting left edge
        if not hit_red and green != 255 and red == 255 and blue != 255:
            hit_red = True
            left_edge = x
            break

    return left_edge

# Next, we'll translate the getLeftEdge function.

def get_left_edge(image):
    rowsize = image.width * 4
    left_edge = image.width

    for x in range(image.width):
        for y in range(image.height):
            red, green, blue = image.getpixel((x, y))
            if x < left_edge and green != 255 and red != 255 and blue != 255:
                left_edge = x

    return 0 if left_edge == image.width else left_edge

# Placeholder for the image class to be used in testing the functions.
class ImagePlaceholder:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(255, 255, 255
