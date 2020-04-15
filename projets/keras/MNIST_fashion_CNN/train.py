from keras.utils import np_utils
from keras import backend as K

from keras.optimizers import Adam
from model import simpleCNN

from keras.datasets import fashion_mnist

# Display hist
from matplotlib import pyplot as plt

# Save model
from keras.models import load_model

## Correct Issue : "Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR"
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)


# Use GPU
K.tensorflow_backend._get_available_gpus()

if __name__ == "__main__":
  model = simpleCNN.simplecnn()
  model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
      metrics=["accuracy"]
  )

  data_label =["T_shirt", "pantalon", "pull-over", "robe", "manteau", "sandale", "chemise", "basket", "sac", "bottine"]

  ((trainX, trainY), (testX, testY)) = fashion_mnist.load_data()

  print(type(trainX))
  print(trainX.shape[0])
  print(testX.shape[0])
  print(testX.shape[0])
  print(testX.shape[0])
  print(K.image_data_format())
  if K.image_data_format() == "channels_first":
      trainX = trainX.reshape((trainX.shape[0], 1, 28, 28))
      testX = testX.reshape((testX.shape[0], 1, 28, 28))
  else:
      trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
      testX = testX.reshape((testX.shape[0], 28, 28, 1))

  trainX = trainX.astype("float32") / 255.0
  testX = testX.astype("float32") / 255.0

  trainY= np_utils.to_categorical(trainY, 10)
  testY= np_utils.to_categorical(testY, 10)

  Hist = model.fit(trainX, trainY, validation_data=(testX, testY), batch_size=32, epochs=15)

  plt.plot(Hist.history['accuracy'])
  plt.plot(Hist.history['val_accuracy'])
  plt.title('Precision du modèle')
  plt.ylabel('Precision')
  plt.xlabel('Iteration')
  plt.legend(['Apprentissage', 'Test'], loc='upper left')
  plt.savefig("Hist.png")
  plt.show()

  # Save model
  model.save('model.h5')