The goal of this project is to detect quality marks on food products. In order to use the code in this repository, some steps have to be taken.
First of all, data is needed where quality marks (or any kind of other objects you would want to detect) are present. This data needs to be labelled in .xml format. The LabelImg tool (https://github.com/tzutalin/labelImg) can be used to do so. Make sure to save the annotations as .xml files.
To train and validate your model a training and validation set is needed, both containing a folder with the images and the belonging annotations. Your data structure should look like this:

Data

-	Train

    o	Images

        	Image 1.png
        	Image 2.png
        	….
        
    o	Annotations

        	Image1.xml
        	Image2.xml
        	….

-	Validation

     o	Images

        	Image5.png
        	Image6.png
        	….
        
     o	Annotations
     
        	Image5.xml
        	Image6.xml
        	….
        
        
Besides the training and validation, you need a pretrained network. We used yolov3 (stored in .h5 format) to train the model. This model can be downloaded by cloning the following github repo: 
https://github.com/qqwweee/keras-yolo3
By running the following command the weights are transformed into a .h5 file, which will be used for training. 
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5


In order to train your model, transfer learning will be used from the pretrained yolo network. This github repo contains a requirements.txt which should be installed in an empty environment (to avoid wrong dependencies) before training. 
As a last step you should change the following in the code:

In keurmerken_training.py:
DATA_DIR =  path to your data folder containing train and validation set
MODEL_PATH =  path to your pretrained model (i.e. yolov3.h5) stored in .h5 format
labels = list with the labels of your annotations


In keurmerken_predicting.py:
MODEL_PATH =  path to your model after training
JSON_PATH = path to the .json file created while training
IMAGE_DIR =  directory where the images you want to predict the label on are stored
RESULTS_DIR =  directory where the images after they are annotated and labelled should be stored
While training the model will automatically create new folders in your data map (cache, json, logs, models). The models folder contains the models made while training. 

If you want to change something, for instance the labels, you should delete the cache, logs and the json folder in order to retrain your model. 

Steps for adding new labels:
1. Remove cache, json and logs folder from your data directory
2. Label new data and store in the training and validation folder
3. Add the new label to the list of labels in the keurmerken_training.py file
4. Retrain your model.

