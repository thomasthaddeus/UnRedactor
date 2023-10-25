# utils.py
import PIL.Image as Image

def get_blue_margin(image):
    rowsize = image.width * 4
    margin = 0
    center = 0
    found = False

    for x in range(image.width):
        y = image.height // 2
        red, green, blue = image.getpixel((x, y))
        if not found and blue == 255 and green != 255 and red != 255:
            found = True
            margin = x
            break

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

def get_margins(image):
    rowsize = image.width * 4
    hit_red = False
    left_edge = 0

    for x in range(image.width):
        y = image.height // 2
        red, green, blue = image.getpixel((x, y))
        if not hit_red and green != 255 and red == 255 and blue != 255:
            hit_red = True
            left_edge = x
            break

    return left_edge

def get_left_edge(image):
    rowsize = image.width * 4
    left_edge = image.width

    for x in range(image.width):
        for y in range(image.height):
            red, green, blue = image.getpixel((x, y))
            if x < left_edge and green != 255 and red != 255 and blue != 255:
                left_edge = x

    return 0 if left_edge == image.width else left_edge
