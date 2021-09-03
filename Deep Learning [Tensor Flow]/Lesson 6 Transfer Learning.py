import tensorflow as tf

import matplotlib.pylab as plt

# importing HUB
import tensorflow_hub as hub
import tensorflow_datasets as tfds

from tensorflow.keras import layers

import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)



# The model that we'll use is MobileNet v2 (but any model from tf2
# compatible image classifier URL from tfhub.dev would work)

# Download the MobileNet model and create a Keras model from it.
# MobileNet is expecting images of 224  ×  224 pixels, in 3 color channels (RGB)

CLASSIFIER_URL ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/2"
IMAGE_RES = 224

model = tf.keras.Sequential([
    hub.KerasLayer(CLASSIFIER_URL, input_shape=(IMAGE_RES, IMAGE_RES, 3))
])


# Run it on a single image
"""
MobileNet has been trained on the ImageNet dataset. ImageNet has 1000 different output classes,
and one of them is military uniforms. Let's get an image containing a military uniform that is
not part of ImageNet, and see if our model can predict that it is a military uniform.
"""
import numpy as np
import PIL.Image as Image

grace_hopper = tf.keras.utils.get_file('image.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg')
grace_hopper = Image.open(grace_hopper).resize((IMAGE_RES, IMAGE_RES))
grace_hopper

# make sure its in proper format
grace_hopper = np.array(grace_hopper)/255.0
grace_hopper.shape

# Remember, models always want a batch of images to process. So here, we add
# a batch dimension, and pass the image to the model for prediction.
result = model.predict(grace_hopper[np.newaxis, ...])
result.shape

# The result is a 1001 element vector of logits, rating the probability of each class for the image.

# So the top class ID can be found with argmax.
predicted_class = np.argmax(result[0], axis=-1)
predicted_class


# To see what our predicted_class is in the ImageNet dataset,
# download the ImageNet labels and fetch the row that the model predicted
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

plt.imshow(grace_hopper)
plt.axis('off')
predicted_class_name = imagenet_labels[predicted_class]
_ = plt.title("Prediction: " + predicted_class_name.title())




##################################################################################3



# Use a TensorFlow Hub models for the Cats vs. Dogs dataset





# We can use TensorFlow Datasets to load the Dogs vs Cats dataset.
(train_examples, validation_examples), info = tfds.load(
    'cats_vs_dogs', 
    with_info=True, 
    as_supervised=True, 
    split=['train[:80%]', 'train[80%:]'],
)

num_examples = info.splits['train'].num_examples
num_classes = info.features['label'].num_classes
num_validations = 0
for example in validation_examples:
    num_validations+=1

print('Total Number of Classes: {}'.format(num_classes))
print('Total Number of Training Images: {}'.format(num_examples))
print('Total Number of Validation Images: {} \n'.format(num_validations))



# The images in the Dogs vs. Cats dataset are not all the same size
for i, example_image in enumerate(train_examples.take(3)):
  print("Image {} shape: {}".format(i+1, example_image[0].shape))

# So we need to reformat all images to the resolution expected by MobileNet (224, 224).

# The .repeat() and steps_per_epoch here is not required, but saves ~15s per epoch,
# since the shuffle-buffer only has to cold-start once.
def format_image(image, label):
  image = tf.image.resize(image, (IMAGE_RES, IMAGE_RES))/255.0
  return image, label

BATCH_SIZE = 32
# create training and validation batches of size 32
train_batches      = train_examples.shuffle(num_examples//4).map(format_image).batch(BATCH_SIZE).prefetch(1)
validation_batches = validation_examples.map(format_image).batch(BATCH_SIZE).prefetch(1)


# Remember our model object is still the full MobileNet model trained on ImageNet, so it has 1000 possible output classes.
# ImageNet has a lot of dogs and cats in it, so let's see if it can predict the images in our Dogs vs. Cats dataset.
image_batch, label_batch = next(iter(train_batches.take(1)))
image_batch = image_batch.numpy()
label_batch = label_batch.numpy()

result_batch = model.predict(image_batch)

predicted_class_names = imagenet_labels[np.argmax(result_batch, axis=-1)]
predicted_class_names

plt.figure(figsize=(10,9))
for n in range(30):
  plt.subplot(6,5,n+1)
  plt.subplots_adjust(hspace = 0.3)
  plt.imshow(image_batch[n])
  plt.title(predicted_class_names[n])
  plt.axis('off')
_ = plt.suptitle("ImageNet predictions")





# Let's now use TensorFlow Hub to do Transfer Learning
# Note that we're calling the partial model from TensorFlow Hub (without the final classification layer) a feature_extractor

URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/2"
feature_extractor = hub.KerasLayer(URL,
                                   input_shape=(IMAGE_RES, IMAGE_RES,3))

# Let's run a batch of images through this, and see the final shape
feature_batch = feature_extractor(image_batch)
print(feature_batch.shape)
# 32 is the number of images, and 1280 is the number of neurons in the last layer of the partial model from TensorFlow Hub.


# Freeze the variables in the feature extractor layer, so that the training only modifies the final classifier layer.
feature_extractor.trainable = False


# Now wrap the hub layer in a tf.keras.Sequential model, and add a new classification layer.
model = tf.keras.Sequential([
  feature_extractor,
  layers.Dense(2)
])

model.summary()




# Train the model

model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

EPOCHS = 6
history = model.fit(train_batches,
                    epochs=EPOCHS,
                    validation_data=validation_batches)



# Check the predictions
# To redo the plot from before, first get the ordered list of class names
class_names = np.array(info.features['label'].names)
class_names

# Run the image batch through the model and convert the indices to class names
predicted_batch = model.predict(image_batch)
predicted_batch = tf.squeeze(predicted_batch).numpy()
predicted_ids = np.argmax(predicted_batch, axis=-1)
predicted_class_names = class_names[predicted_ids]
predicted_class_names

print("Labels: ", label_batch)
print("Predicted labels: ", predicted_ids)


plt.figure(figsize=(10,9))
for n in range(30):
  plt.subplot(6,5,n+1)
  plt.subplots_adjust(hspace = 0.3)
  plt.imshow(image_batch[n])
  color = "blue" if predicted_ids[n] == label_batch[n] else "red"
  plt.title(predicted_class_names[n].title(), color=color)
  plt.axis('off')
_ = plt.suptitle("Model predictions (blue: correct, red: incorrect)")

