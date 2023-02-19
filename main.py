# IMPORTS
import cv2 as cv 
import pyautogui
import time
import numpy as np

from direct_keys import PressKey, ReleaseKey, KEY_W, KEY_A, KEY_D, KEY_S


img = cv.imread("3x3.png")
print(img[0,0])
print(img[1,0])
print(img[2,0])


print(img[0,1])
print(img[1,1])
print(img[2,1])

time.sleep(3)

def move_forwards():
	PressKey(KEY_W)
	time.sleep(0.1)
	ReleaseKey(KEY_W)



