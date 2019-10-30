from imageai.Detection.Custom import DetectionModelTrainer

# Choose path where data and model is stored
DATA_DIR = r"C:\Users\judit\Downloads\drive-download-20191024T074253Z-001\planetproof"
PRETRAINED_MODEL = r"C:\Users\judit\Downloads\drive-download-20191024T074253Z-001\planetproof\models\detection_model-ex-020--loss-0006.402.h5"


def keurmerk_train(data, model):
    """Trains YOLOv3 model from pretrained model.

    Arguments:
        data {string} -- Directory where the image and annotation data is
        stored according to the specified structure.

        model {string} -- Directory where the chosen model is stored.
    """

    # Set model type
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()

    labels = ['planetproof']

    # Data folder
    trainer.setDataDirectory(data_directory=DATA_DIR)

    # Training configuration
    trainer.setTrainConfig(object_names_array=labels,
                           batch_size=4,
                           num_experiments=100,
                           train_from_pretrained_model=PRETRAINED_MODEL)

    trainer.trainModel()


if __name__ == "__main__":
    keurmerk_train(DATA_DIR, PRETRAINED_MODEL)
