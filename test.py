import cv2
import sys

path = sys.argv[1]
image = cv2.imread(path)
cv2.imwrite("output.jpg", image)
try:
    _ = len(image)
    print(1)
except TypeError:
    print(0)

sys.stdout.flush()
