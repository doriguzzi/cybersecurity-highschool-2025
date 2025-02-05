# Addestramento, test ed installazione di un algoritmo di Machine Learning per l'individuazione degli attacchi di rete

In questo laboratorio, addestreremo e testeremo una rete neurale per l'individuazione di attacchi di rete di tipo Distributed Denial of Service (DDoS).

## Training and testing
The training methods are implemented in the Jupyter notebook [training-binary.py](./training-binary.ipynb). After 100 epochs, the script produces a trained CNN in *h5* format saved in the ```output``` folder.

The training process is performed by using the training and validation set available in the ```sample-dataset``` folder. Some relevant hyperparameters of the model (number of convolutional kernels and their height) and of the training process (batch size, learning rate and max epochs) can be changed to improve the performance of the CNN.

One trained, the model can be tested on the test set through the Jupyter notebook [classify.ipynp](./classify.ipynb)

## Simulated deployment
Once trained, the CNN can perform inference on live network traffic or on pre-recorded traffic traces saved in ```pcap``` format. This operational mode is implemented in the ```lucid_cnn.py``` script and leverages on ```pyshark``` and ```tshark``` tools to extract the packets from a ```pcap``` file. The script simulates an online deployment, where the traffic is collected for a predefined amount of time (```time_window```) and then sent to the neural network for classification.

Inference on a pre-recorded traffic trace can be started with command:

```
python3 lucid_cnn.py --predict_live ./sample-dataset/CIC-DDoS-2019-UDPLag.pcap --model ./output/10t-10n-DOS2019-LUCID.h5 --dataset_type DOS2019
```

The script parses the pcap file with the pre-recorded network traffic from the beginning to the end, printing the classification results every 10 seconds (default time window).