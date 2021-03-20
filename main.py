import cv2 as cv
import math
import numpy as np

# User input required
# -------------------
# - filename
# - width
# - height
# - mirror?
# - scale?

# resize: img = cv.resize(frame, (0, 0), fx=Xscale, fy=Yscale)
# open img: img = cv.imread('filename', color channel)
# color channel: -1 color, 0 greyscale, 1 color with alpha

def main():

    width = int(input('Enter Width: '))
    height = int(input('Enter Height: '))
    filename = input('Enter image file: ')

    color_channel = -1
    file_extension = filename.split('.')[-1]
    if file_extension == 'png':
        color_channel = 1

    src = cv.imread(filename, color_channel)

    src_height = src.shape[0]
    src_width = src.shape[1]

    h_rep = math.ceil(height / src_height)
    w_rep = math.ceil(width / src_width)
    
    img = np.zeros((width, height, 3), np.uint8)

    print(width, height)
    print(src_width, src_height)

    for i in range(h_rep):
        for j in range(w_rep):

            print(i, j)

            p1 = min(src_height, height-(i*src_height))
            p2 = min(src_width, width-(j*src_width))
            print('p:', p1, p2)

            x1 = j*src_width
            x2 = min(width, (j+1)*src_width)
            print('x:', x1, x2)

            y1 = i*src_height
            y2 = min(height, (i+1)*src_height)
            print('y:', y1, y2)

            pattern = src[:p1, :p2]
            test = img[y1:y2, x1:x2]

            print(test.shape, pattern.shape)

            img[y1:y2, x1:x2] = pattern

    cv.imshow('Image', img)
    cv.waitKey(0);
    cv.destroyAllWindows()
    

main()
