import tensorflow as tf

# Difference is only in a model itself
# vs Stateful

model = keras.models.Sequential([
  keras.layers.SimpleRNN(100, return_sequences=True,
                         stateful=True
                         batch_input_shape=[1, None, 1]),
  keras.layers.SimpleRNN(100, return_sequences=True, stateful=True),
  keras.layers.Dense(1),
  keras.layers.Lambda(lambda x: x * 200.0)
])

# ALSO
# need to reset states in both and use sequentional window dataset

class ResetStatesCallback(keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs):
        self.model.reset_states()

reset_states = ResetStatesCallback()

model.fit(train_set, epochs=500, validation_data=valid_set,
          callbacks=[early_stopping, model_checkpoint,
                     reset_states])


# vs LSTM

model = keras.models.Sequential([
  keras.layers.LSTM(100, return_sequences=True,
                         stateful=True
                         batch_input_shape=[1, None, 1]),
  keras.layers.LSTM(100, return_sequences=True, stateful=True),
  keras.layers.Dense(1),
  keras.layers.Lambda(lambda x: x * 200.0)
])
