import cv2 as cv
from math import ceil
import numpy as np


def main() -> None:

    # Get input

    try:
        width = int(input('Enter Width: '))
        height = int(input('Enter Height: '))
    except:
        print('ERROR: invalid input, try again')
        return

    src_path = input('Enter image source file: ')
    if not src_path:
        print('ERROR: invalid filename, try again')
        return

    filename = input('Enter new image file name: ')
    if not filename:
        print('ERROR: invalid filename, try again')
        return

    color_channel = -1
    tok = filename.split('.')
    if len(tok) == 1:
        print('ERROR: invalid filename, try again')
        return

    if tok[-1] == 'png':
        color_channel = 1

    # Open source image

    src = cv.imread(src_path, color_channel)

    src_height = src.shape[0]
    src_width = src.shape[1]

    # Determine number of repetitions

    h_rep = ceil(height / src_height)
    w_rep = ceil(width / src_width)
    
    # Create new image

    img = np.zeros((height, width, 3), np.uint8)

    for i in range(h_rep):
        for j in range(w_rep):

            p1 = min(src_height, height-(i*src_height))
            p2 = min(src_width, width-(j*src_width))

            x1 = j*src_width
            x2 = min(width, (j+1)*src_width)

            y1 = i*src_height
            y2 = min(height, (i+1)*src_height)

            img[y1:y2, x1:x2] = src[:p1, :p2]

    # Save new image

    try:
        cv.imwrite(filename, img)
    except:
        print('ERROR: failed to create file')

main()
