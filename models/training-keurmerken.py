import os
import imageai
from imageai.Detection.Custom import DetectionModelTrainer


# Copy and paste the root of your folder from the side menu
ROOT_DIR = r"C:\Users\judit\Downloads\drive-download-20191024T074253Z-001"

"""## Model type"""

# Set model type
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()

"""## Training settings"""

# Detect and set class labels
#labels = ['planetproof', 'asc', 'msc', 'eko', 'ebio', 'fairtrade', 'beterleven', 'utz']
labels =  ['planetproof']



# Data folder
trainer.setDataDirectory(data_directory = r"C:\Users\judit\Downloads\drive-download-20191024T074253Z-001\planetproof")

"""To resume training, copy the directory of your most recent model in `train_from_pretrained_model`."""

# Training configuration
trainer.setTrainConfig(object_names_array = labels,
                       batch_size = 4,
                       num_experiments = 100,
                       train_from_pretrained_model= r"C:\Users\judit\Downloads\drive-download-20191024T074253Z-001\planetproof\models\detection_model-ex-002--loss-0009.663.h5")

trainer.trainModel()