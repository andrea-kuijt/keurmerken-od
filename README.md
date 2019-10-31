# keurmerken-od
Object Detection of sustainability labels on food

In order to train your model and predict labels, you should have a training- and validation set, both containing images and annotations. 
A folder including both a training a test set, should be stored in a folder called 'data'. You have to store this folder in the cloned github repository. 
In order to train the model, a pretrained network should be used. This could be yolov3 or another model that has been trained based on yolov3 (stored in .h5 format). 

The code should work when your data is stored in the data folder. 
The requirements.txt should be used to install all needed packages, it is recommended to install these in clean virtual environment to avoid wrong dependencies.
