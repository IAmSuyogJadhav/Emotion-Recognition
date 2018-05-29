# Emotion-Recognition

## Ultimate goal
The project aims to create a webapp that will recognise a person's emotions live in the browser. It can also be further developed to include some nice applications.
## Current status
Right now, the focus is on the backend. The model has been trained with keras, using TensorFlow backend. The model architecture is shown below. Addition of CNN was the main step in improving the accuracy of the model.
![alt text](https://github.com/IAmSuyogJadhav/Emotion-Recognition/blob/master/network.png)

## To-Do's
94% accuracy is fine for most purposes, yet it has a lot of room for improvement. Soon going to turn to data augmentation to increase the data avialable for training by performing various modifications on existing data like, rotation, zooming in/out, cropping etc. This prevents overfitting and gives a more reliable model.
The webapp is yet to be implemented. Will be implemented soon.

## Data description
* ```./backend```: Contains the backend part of the project. It contains a file named ```train.ipynb``` that has the code to train this model from scratch, if you wish to. It also contains the images used for training the model ([original source](https://github.com/muxspace/facial_expressions)). Just [clone](https://codeload.github.com/IAmSuyogJadhav/Emotion-Recognition/zip/master) this repository and uncompress the contents and you're ready to go!

* ```./frontend```: Contains the frontend part of the project. Currently it is implemented using HTML+CSS and it is not linked with the backend. The frontend is yet to be created using JS.

## Contributors
* Backend: [Suyog](https://github.com/IAmSuyogJadhav/)
* Frontend: [Ujjawal](https://github.com/ujjawaljaiswal2017)

