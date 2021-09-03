import tensorflow as tf

# Sequence 2 Sequence Stateless

def seq2seq_window_dataset(series, window_size, batch_size=32,
                           shuffle_buffer=1000):
    series = tf.expand_dims(series, axis=-1)
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[1:]))
    return ds.batch(batch_size).prefetch(1)

for X_batch, Y_batch in seq2seq_window_dataset(tf.range(10), 3, batch_size=1):
    print("X:", X_batch.numpy())
    print("Y:", Y_batch.numpy())


# vs Stateful

def stateful_window_dataset(series, window_size):# no Shuffle
    series = tf.expand_dims(series, axis=-1)
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=window_size,# shift by a window_size
                   drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-1], w[1:]))
    return ds.batch(1).(batch_size).prefetch(1)# batches containing single window

for X_batch, Y_batch in seq2seq_window_dataset(tf.range(10), 3, batch_size=1):
    print("X:", X_batch.numpy())
    print("Y:", Y_batch.numpy())



###################


# Models

# Sequence 2 Sequence RNN

window_size = 30
train_set = seq2seq_window_dataset(x_train, window_size,
                                   batch_size=128)
valid_set = seq2seq_window_dataset(x_valid, window_size,
                                   batch_size=128)

model = keras.models.Sequential([
  keras.layers.SimpleRNN(100, return_sequences=True,
                         input_shape=[None, 1]),
  keras.layers.SimpleRNN(100, return_sequences=True),
  keras.layers.Dense(1),
  keras.layers.Lambda(lambda x: x * 200.0)
])

# vs Stateful


window_size = 30
train_set = stateful_window_dataset(x_train, window_size)#
valid_set = stateful_window_dataset(x_valid, window_size)# batch_size is 1

model = keras.models.Sequential([
  keras.layers.SimpleRNN(100, return_sequences=True,
                         stateful=True###
                         batch_input_shape=[1, None, 1]),# 
  keras.layers.SimpleRNN(100, return_sequences=True, stateful=True),#
  keras.layers.Dense(1),
  keras.layers.Lambda(lambda x: x * 200.0)
])

# ALSO
# need to reset states at each epoch:
class ResetStatesCallback(keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs):
        self.model.reset_states()

reset_states = ResetStatesCallback()

model.fit(train_set, epochs=500, validation_data=valid_set,
          callbacks=[early_stopping, model_checkpoint,
                     reset_states])#
