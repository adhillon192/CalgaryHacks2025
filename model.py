import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
import kagglehub


# Download latest version
path = kagglehub.dataset_download("anshulmehtakaggl/wildlife-animals-images")


# print("Path to dataset files:", path)

IMG_SIZE = (224,224)
BATCH_SIZE = 32

data = ImageDataGenerator(
    rescale=1./255,
    # validation_split=0.2,
    rotation_range=20,  # Data augmentation
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


# Load training data
train_generator = data.flow_from_directory(
    path,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

# # Load validation data
# validation_generator = data.flow_from_directory(
#     path,
#     target_size= IMG_SIZE,
#     batch_size= BATCH_SIZE,
#     class_mode='categorical',
#     subset='validation'
# )

# Check class labels
print(train_generator.class_indices)

base_model = MobileNetV2(
    input_shape = (224, 224, 3),
    weights="imagenet"
)

model = models.sequential(
    base_model
)


# #Preprocessing the images to a fixed size
# def preprocessImages(picture):
#     image = tf.image.resize(picture["image"], IMG_SIZE)/255.0
#     label = picture["label"]
#     return image, label

# #Applying the preprocessing 
# dataset = dataset.map(preprocessImages).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

# print(dataset)