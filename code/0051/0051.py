import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

SIZE = 128
NUM_RESULTS = 5

classes = np.array(open('ImageNetLabels.txt').read().splitlines())

image = tf.io.read_file('dog.jpg')
image = tf.image.decode_jpeg(image)
image = tf.image.resize(image, [SIZE, SIZE])
image = tf.expand_dims(image, 0) 
image = image/255.0

mobilenetv2 = "https://www.kaggle.com/models/google/mobilenet-v2/frameworks/TensorFlow2/variations/035-128-classification/versions/2"
model = tf.keras.Sequential([hub.KerasLayer(mobilenetv2)])
model.build([None, SIZE, SIZE, 3])

predictions = model.predict(image)
probabilities = tf.nn.softmax(predictions[0])
top_indices = np.argsort(probabilities)[::-1][:NUM_RESULTS]
top_classes = [classes[i] for i in top_indices]

for i, name in enumerate(top_classes):
    print(f"{i+1} - {name}")
