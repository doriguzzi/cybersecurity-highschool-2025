# K-Nearest Neighbors (KNN)
In questo notebook faremo degli esperimenti con l'algoritmo KNN.
Il primo, riguarda la classificazione di immagini di fiori "iris" in tre classi: Setosa, Versicolor, Virginica (notebook [KNN-Iris](./KNN-Iris.ipynb)).
Questo primo esperimento ci permette di capire come funziona KNN e come esso si comporta al variare di alcuni parametri.

| <img src="./Iris-Dataset.png" width="90%">  |
|--|

Nel secondo esperimento, vedremo come si puo' usare un algoritmo semplice come KNN per svolgere compiti complessi come la classificazione del traffico di rete (notebook [KNN-dos2019](./KNN-dos2019.ipynb)).
In questo caso, i campioni (flussi di rete) sono rappresentati con 21 features nel seguente modo:

| Feature nr.         | Feature Name |
|---------------------|---------------------|
| 00 | timestamp (mean IAT) | 
| 01 | packet_length (mean)| 
| 02 | IP_flags_df (sum) |
| 03 | IP_flags_mf (sum) |
| 04 | IP_flags_rb (sum) | 
| 05 | IP_frag_off (sum) |
| 06 | protocols (mean) |
| 07 | TCP_length (mean) |
| 08 | TCP_flags_ack (sum) |
| 09 | TCP_flags_cwr (sum) |
| 10 | TCP_flags_ece (sum) |
| 11 | TCP_flags_fin (sum) |
| 12 | TCP_flags_push (sum) |
| 13 | TCP_flags_res (sum) |
| 14 | TCP_flags_reset (sum) |
| 15 | TCP_flags_syn (sum) |
| 16 | TCP_flags_urg (sum) |
| 17 | TCP_window_size (mean) |
| 18 | UDP_length (mean) |
| 19 | ICMP_type (mean) |
| 20 | Packets (counter)|