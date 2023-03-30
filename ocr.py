import easyocr
import matplotlib as plt
import cv2
import numpy as np
from pytesseract import pytesseract

#pytesseract.tesseract_cmd=

reader=easyocr.Reader(['en'],gpu=False)

img=cv2.imread("C:/Users/Admin/Desktop/Cars0.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
result = reader.readtext(img_gray)
cv2.imshow("output",img_gray)
print(result)
cv2.waitKey(0)
