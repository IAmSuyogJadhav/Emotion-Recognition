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

# ----- Loading the image and converting to grayscale
path = sys.argv[1]
image = cv2.imread(path)
if image is None:
    print(0)  # Correponds to "Unable to load image."
    sys.stdout.flush()
    sys.exit(1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ----- Detecting and Cropping the face
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detected = cascade.detectMultiScale(image)
faces = []
for (x, y, w, h) in detected:
    faces.append(image[y:y+h, x:x+w])

# ----- Resizing the image
for i in range(len(faces)):
    faces[i] = cv2.resize(faces[i], (img_size, img_size))

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

if faces:
    pred = emotion[np.argmax(
                model.predict(faces.pop(0)[np.newaxis, :, :, np.newaxis]))]

    # Predicting for the rest of faces, if there are more than one.
    for i in range(len(faces)):
        pred = pred + ' ' + emotion[np.argmax(
                model.predict(faces[i][np.newaxis, :, :, np.newaxis]))]

    print(pred)
else:
    print(1)  # Corresponds to "Unable to detect face in the image."
    sys.stdout.flush()
    sys.exit(1)
