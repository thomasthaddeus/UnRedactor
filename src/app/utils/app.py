import PIL.Image as Image

# Constants
GUESSABLE_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz '
MAX_LENGTH = 20
BLOCKSIZE = 8
THRESHOLD = 0.25
REDACT_COMMAND = "redact-text"
GUESS_COMMAND = "guess-text"
REDACTED_IMAGE = "secret.png"

def get_blue_margin(image):
    for x in range(image.width):
        y = image.height // 2
        red, green, blue = image.getpixel((x, y))
        if blue == 255 and green != 255 and red != 255:
            margin = x
            break

    top_blue, bot_blue = 0, 0
    found = False
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

def make_guess(command, guess, previous_image, offset_x, offset_y):
    global redacted_image, max_length, guessable_characters
    request = {
        "command": command,
        "redacted_image": redacted_image,
        "totalLength": max_length,
        "text": guess,
        "previousimage": previous_image,
        "charset": guessable_characters,
        "offset_x": offset_x,
        "offset_y": offset_y
    }
    result = redact_placeholder(request)
    return result

def redact_placeholder(request):
    return {
        "status": "not_implemented",
        "message": f"Received request: {request}"
    }

def gather_results(guess, total_score, score, image_data, offset_x, offset_y):
    global best_guess, best_score
    if total_score < best_score:
        best_score = total_score
        best_guess = guess
    return best_guess, best_score

def start_guess():
    return "guess-text triggered"

def redact_text(text_to_redact, redacted_offset_x, redacted_offset_y):
    return f"redact-text triggered with text: {text_to_redact}, offsets: ({redacted_offset_x}, {redacted_offset_y})"

def preload_init():
    global redacted_image
    redacted_image = "base64_representation_of_secret.png"
    return "Initialization completed"

def guess_recursive(guess, score, offset_x, offset_y):
    global redacted_image, guessable_characters, max_length, threshold
    if len(guess) == max_length:
        return
    scores = []
    parent_guess_result = make_guess(guess_command, guess, "", offset_x, offset_y)
    if not parent_guess_result.get("tooBig", False):
        for char in guessable_characters:
            next_guess = guess + char
            result = make_guess(guess_command, next_guess, parent_guess_result.get("imageData", ""), offset_x, offset_y)
            used_threshold = threshold if char != " " else 0.5
            if result.get("score", 1) < used_threshold:
                scores.append([result["score"], next_guess])
        scores.sort()
        for score, new_guess in scores:
            guess_recursive(new_guess, score, offset_x, offset_y)

if __name__=='__main__':
    main()
