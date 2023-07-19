import numpy as np 
from keras.models import Sequential 
from keras.layers import Dense

class MLmodelClass: # This class is used to create and train the model
    def __init__(self, inputLen, outputLen): # inputLen is the length of the input vector, outputLen is the length of the output vector
        self.model = Sequential() # create a sequential model
        self.model.add(Dense(50, activation='relu', input_dim=inputLen)) # add a dense layer with 50 neurons, relu activation and input dimension of inputLen
        self.model.add(Dense(20, activation='relu')) # add a dense layer with 20 neurons and relu activation
        self.model.add(Dense(30, activation='relu')) # add a dense layer with 30 neurons and relu activation
        self.model.add(Dense(outputLen, activation='softmax')) # add a dense layer with outputLen neurons and softmax activation

        self.model.compile(optimizer='adam', 
                           loss='categorical_crossentropy',
                           metrics=['accuracy']) # compile the model with adam optimizer, categorical_crossentropy loss and accuracy metrics

    def train(self, x, y, epochs=500, verbose=1):   # x is the input vector, y is the output vector, epochs is the number of epochs to train the model, verbose is the verbosity mode
        self.model.fit(x, y, epochs=epochs, verbose=verbose) # train the model

    def predict(self, x): # x is the input vector
        pred = self.model.predict(x) # predict the output vector
        return np.argmax(pred) # return the index of the maximum value in the output vector
