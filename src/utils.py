import const
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image

from tkinter import filedialog
from datetime import datetime

def select_file(title):
    print(title)
    path = input("Enter the path of the image: ")
    return path
    # filepath = filedialog.askopenfilename(
    #     title=title,
    #     filetypes=(('JPEG files', '*.jpg'), ('PNG files', '*.png'), ('All files', '*.*')),
    # )
    # return filepath


def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    scale = const.MAX_DIM / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]

    return img

def tensor_to_pil_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)

def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)

    plt.imshow(image)
    if title:
        plt.title(title)

def save_pil_image(image, filename):
    image.save(filename)

def log(message):
    date_format = '%Y-%m-%d %H:%M:%S'
    print(f'[{datetime.now().strftime(date_format)}] {message}')