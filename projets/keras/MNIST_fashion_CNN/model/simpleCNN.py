
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dropout, Dense
from keras import backend as K


## Visualization
from keras.utils import plot_model

def simplecnn():
  model=Sequential()
  model.add(
    Conv2D(
      filters=32,
      kernel_size=(5, 5),
      padding="same",
      input_shape=(28, 28, 1)  # Iput size because it's the first layer
    )

  )
  #model.add(Activation("relu"))
  model.add(
    Conv2D(
      filters=32,
      kernel_size=(5, 5),
      padding='same',
      activation='relu'
    )
  )
  model.add(
    MaxPooling2D(
      pool_size=(2, 2),
      strides=(2, 2)
    )
  )
  model.add(Dropout(0.2))
  model.add(
    Conv2D(
      filters=64,
      kernel_size=(5, 5),
      padding='same',
      activation='relu'
    )
  )
  model.add(
    Conv2D(
      filters=64,
      kernel_size=(5, 5),
      padding='same',
      activation='relu'
    )
  )
  model.add(
    MaxPooling2D(
      pool_size=(2, 2),
      strides=(2, 2)
    )
  )
  model.add(
    Dropout(0.2)
  )
  ## Link between convolution and neural network
  model.add(Flatten())

  ## Neural Network
  model.add(
    Dense(
      120,
      activation='relu'
    )
  )
  model.add(
    Dense(
      84,
      activation='relu'
    )
  )
  model.add(
    Dense(
      10,
      activation='softmax'
    )
  )
  return model

def generate_dot_graph(model, file):
  plot_model(model, to_file=file)

if __name__ == "__main__":
  model=simplecnn()
  model.summary()

  #generate_dot_graph(model, file="./graph.png")

