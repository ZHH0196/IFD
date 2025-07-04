from keras.utils import plot_model
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense, Flatten

model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(100, 1)))
model.add(MaxPooling1D(2))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

plot_model(model, to_file='1D_CNN_structure.png', show_shapes=True)
