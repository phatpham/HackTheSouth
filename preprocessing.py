import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt

def binarizeAndInvert(img):
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),0)
    _,out = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    out = cv.bitwise_not(out)
    return out
