import admindata
import numpy as np
from keras.layers import *
from keras.models import *


model = Sequential()
max_features = 500
model.add(Embedding(max_features, 32))
model.add(LSTM(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
    loss='binary_crossentropy',
    metrics=['acc'])

precios = admindata.consultarPrecios("Bitcoin")
precios_a = precios[2]
for precio in precios_a:
    print(precio)
#fechas = admindata.consultarPrecios("Bitcoin")['Datetime']
#input_train = np.array()
#for fecha in fechas:
#    np.append(input_train, precio)
#fechas = admindata.consultarPrecios("Bitcoin")['Datetime']

#history = model.fit(input_train, y_train,
#epochs=10,
#batch_size=128,
#validation_split=0.2)