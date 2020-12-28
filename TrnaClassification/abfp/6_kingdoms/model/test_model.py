# -*- coding: utf-8 -*-
"""test_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o3ousuwDtB0_vGLm9s8JGEM6nlGayQXQ
"""

# Load the Drive helper and mount
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

cd drive/MyDrive/ML_task/

ls

!pip install texttable

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model,Sequential
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.preprocessing import image
from keras.layers import BatchNormalization
from keras.callbacks import CSVLogger
from keras.utils import plot_model
from keras.utils.vis_utils import model_to_dot

import pandas as pd
import csv

from keras import optimizers
from PIL import Image
import os
from keras.layers.advanced_activations import PReLU

import numpy as np
import tensorflow as tf
import random as rn
import struct
from texttable import Texttable

#Для одинакового результата при разных запусках.
os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
rn.seed(12345)
session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
tf.compat.v1.set_random_seed(1234)
sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(), config=session_conf)
tf.compat.v1.keras.backend.set_session(sess)

#specify data paths here
data = 'testBalancedHuge.csv'
db_file = 'dbBalancedHuge.csv'
weights = 'trainedWeightsHugeB32Down20LR5_300.h5'

img_size = 80
input_length = 220

model2 = Sequential()

model2.add(Dropout(0.05, input_shape=(input_length,)))

model2.add(Dense(512))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dense(1024))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dense(2048))
model2.add(BatchNormalization())
model2.add(Activation('relu'))


model2.add(Dense(30420))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dropout(0.3))

model2.add(Dense(1024))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dropout(0.9))

model2.add(Dense(512))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dropout(0.9))

model2.add(Dense(128))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dropout(0.75))

model2.add(Dense(64))
model2.add(BatchNormalization())
model2.add(Activation('relu'))

model2.add(Dropout(0.5))

model2.add(Dense(6))
model2.add(Activation('softmax'))

model2.load_weights(weights)

def generate_arrays(path):
    db = pd.read_csv(db_file)
    f = open(path)
    r = csv.reader(f)
    batch_x = []
    batch_y = []
    for line_index, ln in enumerate(r):
        if len(ln) > 0:
            for i in range(1,len(ln)):
                if ln[i] == "A": ln[i] = "2"
                elif ln[i] == "C": ln[i] = "3"
                elif ln[i] == "G": ln[i] = "5"
                elif ln[i] == "T": ln[i] = "7"
                else: ln[i] = "0"

            id = ln[0]
            if id[0] == '>':
              id = id[1:]

            X = np.array(ln[1:len(ln)],dtype=np.uint32)
            y = [1, 0, 0, 0, 0, 0]
            if db.loc[db['id'] == int(id)].values[0][2] == 'b':
                y = [0, 1, 0, 0, 0, 0]
            if db.loc[db['id'] == int(id)].values[0][2] == 'f':
                y = [0, 0, 1, 0, 0, 0]
            if db.loc[db['id'] == int(id)].values[0][2] == 'p':
                y = [0, 0, 0, 1, 0, 0]
            if db.loc[db['id'] == int(id)].values[0][2] == 'anim':
                y = [0, 0, 0, 0, 1, 0]
            if db.loc[db['id'] == int(id)].values[0][2] == 'prot':
                y = [0, 0, 0, 0, 0, 1]
            batch_x.append(np.array(X))
            batch_y.append(y)
    return np.array(batch_x), np.array(batch_y)

data = generate_arrays(data)

result = model2.predict_classes(data[0], verbose=0)

def precision(cl, row):
    return row[cl] / sum(row)

def recall(cl, col):
    return col[cl] / sum(col)

def accuracy(c1, data_matrix):
  tp_count = data_matrix[c1, c1]
  tn_count = 0
  for i in range(6):
    for j in range(6):
      if i != c1 and j != c1:
        tn_count += data_matrix[i, j]
  return (tp_count + tn_count) / np.sum(data_matrix)

def total_accuracy(data_matrix):
  true_sum = 0
  for i in range(6):
    true_sum += data_matrix[i, i]
  return true_sum / np.sum(data_matrix)

a = [0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0]
f = [0, 0, 0, 0, 0, 0]
p = [0, 0, 0, 0, 0, 0]
anim = [0, 0, 0, 0, 0, 0]
prot = [0, 0, 0, 0, 0, 0]

for i in range(len(result)):
    res = result[i]
    lbl = list(data[1][i]).index(1)
    if lbl == 0:
        a[res] += 1
    if lbl == 1:
        b[res] += 1
    if lbl == 2:
        f[res] += 1
    if lbl == 3:
        p[res] += 1
    if lbl == 4:
        anim[res] += 1
    if lbl == 5:
        prot[res] += 1        
        
res_data = np.array([a, b, f, p, anim, prot])

precision_data = [
    precision(0, [a[0], b[0], f[0], p[0], anim[0], prot[0]]),
    precision(1, [a[1], b[1], f[1], p[1], anim[1], prot[1]]),
    precision(2, [a[2], b[2], f[2], p[2], anim[2], prot[2]]),
    precision(3, [a[3], b[3], f[3], p[3], anim[3], prot[3]]),
    precision(4, [a[4], b[4], f[4], p[4], anim[4], prot[4]]),
    precision(5, [a[4], b[5], f[5], p[5], anim[5], prot[5]])
]

recall_data = [
  recall(0, a),
  recall(1, b),
  recall(2, f),
  recall(3, p),
  recall(4, anim),
  recall(5, prot)
]

accuracy_data = [
  accuracy(0, res_data),
  accuracy(1, res_data),
  accuracy(2, res_data),
  accuracy(3, res_data),
  accuracy(4, res_data),
  accuracy(5, res_data)
]

t = Texttable()
t.add_rows([
            ['Ground truth/Prediction', 'Arhea', 'Bacteria','Fungi', 'Plant', 'Animal', 'Protist'],
            ['Arhea', *a],
            ['Bacteria', *b],
            ['Fungi', *f],
            ['Plant', *p],
            ['Animal', *anim],
            ['Protist', *prot]
            ])
print(t.draw())

t = Texttable()
t.add_rows([
            ['Kingdom', 'Arhea', 'Bacteria','Fungi', 'Plant', 'Animal', 'Protist'],
            ['Recall', *precision_data],
            ['Precision', *recall_data],
            ['Accuracy', *accuracy_data]
            ])
print(t.draw())

t = Texttable()
t.add_rows([['Total accuracy', total_accuracy(res_data)]])
print(t.draw())