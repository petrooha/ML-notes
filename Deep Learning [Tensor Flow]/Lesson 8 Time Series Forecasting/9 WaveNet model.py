model = keras.models.Sequential()
model.add(keras.layers.InputLayer(input_shape=[None, 1]))
for dilation_rate in (1,2,4,8,16,32):
    model.add(keras.layers.Conv1D(filters=32, kernel_size=3, strides=1,
                                  dilation_rate=dilation_rate,
                                  padding="casual",
                                  activation="relu")
              )
    model.add(keras.layers.Conv1D(filters=1, kernel_size=1))# basically a dense layer
    
