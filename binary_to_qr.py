from PIL import Image
import re
import math

not_binary_pattern = re.compile("[^01?]")


def binary_to_qr(binary, width=None, height=None):
    """
    If no width or height is specified then it will make a square
    If either width or height is specified then the non specified will be calculated accordingly
    Result is saved to qr.png in the same folder
    """
    binary = not_binary_pattern.sub("", binary)
    binary = binary.replace("?","2")
    if width is None:
        if height is None:
            width = math.ceil(math.sqrt(len(binary)))
            height = width
        else:
            width = math.ceil(len(binary)/height)

    if height is None:
        height = math.ceil(len(binary)/width)

    binary += "0" * ((width * height) - len(binary))
    img = Image.new("L",(width, height))
    i = 0
    for y in range(height):
        for x in range(width):
            bit = int(binary[i])
            if bit == 0:
                color = 255
            elif bit == 1:
                color = 0
            else:
                color = 128

            img.putpixel((x,y), color)
            i += 1

    img.save("qr.png")

