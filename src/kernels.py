import numpy as np


class Kernel:
    blur = np.ones((3, 3), np.float32) / 9
    gaussian_blur_3x3 = np.array(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]
    ) / 16
    gaussian_blur_5x5 = np.array(
        [[1,  4,  6,  4, 1],
         [4, 16, 24, 16, 4],
         [6, 24, 36, 24, 6],
         [4, 16, 24, 16, 4],
         [1,  4,  6,  4, 1]]
    ) / 256
    gaussian_blur_5x5_2 = np.array(
        [[1,  4,  7,  4, 1],
         [4, 16, 26, 16, 4],
         [7, 26, 41, 26, 7],
         [4, 16, 26, 16, 4],
         [1,  4,  7,  4, 1]]
    ) / 273
    sharpening = np.array(
        [[ 0, -1,  0],
         [-1,  5, -1],
         [ 0, -1,  0]]
    )
    sharpening_2 = np.array(
        [[-1, -1, -1],
         [-1,  9, -1],
         [-1, -1, -1]]
    )
    sharpening_3 = np.array(
        [[ 0,  -4,  0],
         [-4,  17, -4],
         [ 0,  -4,  0]]
    )
    sobel_x = np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
    )
    sobel_x_inv = np.array(
        [[1, 0, -1],
         [2, 0, -2],
         [1, 0, -1]]
    )
    sobel_y = np.array(
        [[-1, -2, -1],
         [0,   0,  0],
         [1,   2,  1]]
    )
    sobel_y_inv = np.array(
        [[1,   2,  1],
         [0,   0,  0],
         [-1, -2, -1]]
    )
    embossed_3d = np.array(
        [[0, -3, -3],
         [3,  0, -3],
         [3,  3,  0]]
    )
