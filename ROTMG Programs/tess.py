import pytesseract
from PIL import Image
import cv2
import numpy as np

file_path = "test.png"
img = Image.open(file_path)
img.save("ocr.png", dpi=(300, 300))

image = cv2.imread("ocr.png")
image = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
retval, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
text = pytesseract.image_to_string(threshold)

print (text)
