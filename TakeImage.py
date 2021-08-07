import cv2
import dropbox
import random

def take_snapshot():
  vid = cv2.VideoCapture(0)
  result = True

  while result:
    ret, frame = vid.read()
    cv2.imwrite("pic1.jpg", frame)
    result = False
    
  vid.release()
  cv2.destroyAllWindows()

take_snapshot()