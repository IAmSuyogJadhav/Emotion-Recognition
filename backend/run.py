import cv2
import sys
from keras.models import load_model
import numpy as np

# ----- Some parameters
accuracy = 94.12  # Available: [94.12]
img_size = 25

# ----- Loading the model
model = load_model(
    './models/model_{}.h5'.format(accuracy))

# ----- Loading the image
path = sys.argv[1]
image = cv2.imread(path)
if image is None:
    print(0)
    sys.stdout.flush()
    sys.exit(1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ----- Cropping the image (For now we simply resize the entire image)
image = cv2.resize(image, (img_size, img_size))

emotion = {
    0: 'anger',
    1: 'contempt',
    2: 'disgust',
    3: 'fear',
    4: 'happiness',
    5: 'neutral',
    6: 'sad',
    7: 'sadness',
    8: 'surprise'
    }

print(emotion[np.argmax(model.predict(image[np.newaxis, :, :, np.newaxis]))])
