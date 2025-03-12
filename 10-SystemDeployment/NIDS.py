# Author: Roberto Doriguzzi-Corin
# Project: Corso di Algoritmi di Machine Learning per la rilevazione di attacchi informatici
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import argparse
import pyshark
import numpy as np
import pprint
from scipy.stats import uniform, randint
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import RandomizedSearchCV
from tensorflow.keras.models import Sequential,load_model, save_model
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Conv2D, GlobalMaxPooling2D, Flatten, Dropout
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.utils import set_random_seed
from lucid_dataset_parser import *
from util_functions import *

import nest_asyncio
nest_asyncio.apply()  

EPOCHS = 100
TEST_ITERATIONS=100

# disable GPUs for test reproducibility
tf.config.set_visible_devices([], 'GPU')

SEED = 0
np.random.seed(SEED)
set_random_seed(SEED)


parser = argparse.ArgumentParser(description="A DL-based NIDS for DDoS attack detection")
args = parser.parse_args(args=[])
parser.add_argument('-t', '--train', nargs='?', type=str,  default=None, help="Start the training process")
parser.add_argument('-p', '--predict', nargs='?', type=str,  default=None, help="Perform a prediction on pre-preprocessed data")
parser.add_argument('-pl', '--predict_live', nargs='?', type=str, default=None, help='Perform a prediction on live traffic or on a pre-recorded traffic trace in pcap format')
parser.add_argument('-m', '--model', type=str, default = None, help='File containing the model in h5 format')

args, unknown = parser.parse_known_args()
print("see all args:", args)



def report_results(Y_true, Y_pred, model_name, data_source, prediction_time):
    ddos_rate = '{:04.3f}'.format(sum(Y_pred) / Y_pred.shape[0])
    row = {}

    if Y_true is not None and len(Y_true.shape) > 0:  # if we have the labels, we can compute the classification accuracy
        Y_true = Y_true.reshape((Y_true.shape[0], 1))
        accuracy = accuracy_score(Y_true, Y_pred)

        f1 = f1_score(Y_true, Y_pred)
        tn, fp, fn, tp = confusion_matrix(Y_true, Y_pred, labels=[0, 1]).ravel()
        tnr = tn / (tn + fp)
        fpr = fp / (fp + tn)
        fnr = fn / (fn + tp)
        tpr = tp / (tp + fn)

        row = {'Model': model_name, 'Time': '{:04.3f}'.format(prediction_time),
               'Samples': Y_pred.shape[0], 'DDOS%': ddos_rate, 'Accuracy': '{:05.4f}'.format(accuracy), 'F1Score': '{:05.4f}'.format(f1),
               'TPR': '{:05.4f}'.format(tpr), 'FPR': '{:05.4f}'.format(fpr), 'TNR': '{:05.4f}'.format(tnr), 'FNR': '{:05.4f}'.format(fnr), 'Source': data_source}

    pprint.pprint(row, sort_dicts=False)


def create_model(optimizer=SGD, dense_layers=4, hidden_units=2, learning_rate = 0.001):
    model = Sequential(name  = "mlp")
    ### Add YOUR CODE HERE ###
    model.add(Dense(hidden_units, input_shape=(21,), activation='relu'))
    for layer in range(dense_layers):
        model.add(Dense(hidden_units, activation='relu', name='hidden-fc' + str(layer)))
    model.add(Dense(1, activation='sigmoid', name='fc2'))
    model.compile(optimizer=optimizer(learning_rate=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])
    ##########################
    model.summary()
    return model


def predict(dataset_path, model_path):
    if dataset_path is not None:
        X_test, y_test = load_dataset(dataset_path + "/*" + '-test.hdf5')

        if model_path == None or model_path.endswith('.h5') == False:
                print ("No valid model specified!")
                exit(-1)

        if model_path is not None:
            model = load_model(model_path)
        else:
            print ("Invalid model path: ", model_path) 
            return

        pt0 = time.time()
        for i in range(TEST_ITERATIONS):
            Y_pred = np.squeeze(model.predict(X_test, batch_size=16) > 0.5,axis=1)
        pt1 = time.time()
        prediction_time = pt1 - pt0

        report_results(np.squeeze(y_test), Y_pred,  model.name, '', prediction_time/TEST_ITERATIONS)


def predict_live(source,model_path):
    if source is not None:
        if source.endswith('.pcap'):
            pcap_file = source
            cap = pyshark.FileCapture(pcap_file)
            data_source = pcap_file.split('/')[-1].strip()
        else:
            cap =  pyshark.LiveCapture(interface=source)
            data_source = args.predict_live

        print ("Prediction on network traffic from: ", source)

        if model_path is not None:
            model = load_model(model_path)
        else:
            print ("Invalid model path: ", model_path) 
            return

        # load the labels, if available
        labels = parse_labels('DOS2019')

        mins, maxs = static_min_max(flatten=True,time_window=10,max_flow_len=1000)

        while (True):
            samples = process_live_traffic(cap, 'DOS2019', labels, max_flow_len=1000, traffic_type="all")
            if len(samples) > 0:
                X,Y_true,flow_ids = dataset_to_list_of_fragments(samples)
                X_flatten = flatten_samples(X)
                X = np.array(normalize(X_flatten, mins, maxs))
                if labels is not None:
                    Y_true = np.array(Y_true)
                else:
                    Y_true = None
                
                pt0 = time.time()
                Y_pred = np.squeeze(model.predict(X, batch_size=2048) > 0.5,axis=1)
                pt1 = time.time()
                prediction_time = pt1 - pt0

                report_results(np.squeeze(Y_true), Y_pred,  model.name, '', prediction_time)

                ### ADD YOUR CODE HERE ###
                for index in range(len(flow_ids)):
                    if Y_pred[index] == True:
                        print("DDoS Flow: ", flow_ids[index])
                ##########################


predict_live(args.predict_live,args.model)


