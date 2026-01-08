import cv2
import numpy as np

def grayscale(img):
    # Converts a color image into grayscale to simplify processing.
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img):
    # Applies Gaussian blur to reduce noise in the image.
    return cv2.GaussianBlur(img, (3, 3), 0)

def sobel_edge(img):
    # Detects edges by computing intensity gradients in both x and y directions.
    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    return cv2.convertScaleAbs(grad_x + grad_y)

def sharpen(img):
    # Sharpens the image by enhancing edges using a convolution kernel.
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def adjust_brightness(img, value=30):
    # Adjusts the image brightness by adding a constant intensity value.
    return cv2.convertScaleAbs(img, alpha=1, beta=value)
