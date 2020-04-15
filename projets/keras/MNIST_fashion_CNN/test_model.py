from keras.models import load_model


import numpy as np
from keras.datasets import fashion_mnist

from keras import backend as K
from keras.utils import np_utils

from matplotlib import pyplot as plt
import cv2


## Correct Issue : "Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR"
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


# Use GPU
K.tensorflow_backend._get_available_gpus()


model = load_model('model.h5')


# Définition des labels
data_label = ["T_shirt", "pantalon", "pull-over", "robe", "manteau", "sacandale", "chemise", "basket", "sac", "bottine"]

# Chargement du jeu de données
((trainX, trainY), (testX, testY)) = fashion_mnist.load_data()

# Vérification du format de TensorFlow
if K.image_data_format() == "channels_first":
    testX = testX.reshape((testX.shape[0], 1, 28, 28))
else:
    testX = testX.reshape((testX.shape[0], 28, 28, 1))

# Conditionnement des données
testX = testX.astype("float32") / 255.0
testY = np_utils.to_categorical(testY, 10)

# Liste pour ensemble d'image est à afficher
tabimages=[]


# Extraction aléatoire et test du modèle
for i in np.random.choice(np.arange(0, len(testY)), size=(16,)):
    results = model.predict(testX[np.newaxis, i])
    prediction = results.argmax(axis=1)
    label = data_label[prediction[0]]

    # Extraction de l'image testX en niveaux de gris suivant la configuration TensorFlow
    if K.image_data_format() == "channels_first":
        image = (testX[i][0]*255).astype("uint8")
    else:
        image = (testX[i]*255).astype("uint8")

    # Si prédiction bonne
    if prediction[0] == np.argmax(testY[i]):
        couleurTXT = (0, 255, 0)
    else:
        couleurTXT = (255, 0, 0)

    image = cv2.merge([image] * 3)
    cv2.putText(image, label, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.20, couleurTXT, 1)
    tabimages.append(image)

plt.figure(figsize=(7, 7))
for i in range(0, len(tabimages)):
    plt.subplot(4, 4, i+1)
    plt.imshow(tabimages[i])
plt.show()