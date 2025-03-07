# Intrusion Detection with Logistic Regression
In questo notebook utilizzeremo Logistic Regression per classificare i flussi di traffico di rete come benigni o dannosi. Il modello di Logistic Regression restituisce un valore compreso tra 0 e 1, che rappresenta la probabilità che il flusso in ingresso sia dannoso. Usiamo una soglia fissata a 0,5 per determinare se il flusso di rete è dannoso o meno.
Addestreremo un modello di Logistic Regression con traffico di rete benigno e quattro classi di attacchi DDoS dal dataset CIC-DDoS2019 dell’Università del New Brunswick. Il traffico di rete è stato precedentemente pre-elaborato in modo che i pacchetti siano raggruppati in flussi di traffico bidirezionali utilizzando la 5-tupla (IP sorgente, IP destinazione, porta sorgente, porta destinazione, protocollo). Ogni flusso è rappresentato da 21 features (attributi) dell’header dei pacchetti calcolate da un massimo di 1000 pacchetti:

| Features           | Logistic Regression model           |
|---------------------|--------------------|
| timestamp (mean IAT)  <br> packet_length (mean) <br> IP_flags_df (sum) <br> IP_flags_mf (sum) <br> IP_flags_rb (sum) <br> IP_frag_off (sum) <br> protocols (mean) <br> TCP_length (mean) <br> TCP_flags_ack (sum) <br> TCP_flags_cwr (sum) <br> TCP_flags_ece (sum) <br> TCP_flags_fin (sum) <br> TCP_flags_push (sum) <br> TCP_flags_res (sum) <br> TCP_flags_reset (sum) <br> TCP_flags_syn (sum) <br> TCP_flags_urg (sum) <br> TCP_window_size (mean) <br> UDP_length (mean) <br> ICMP_type (mean) <br> Packets (counter) <br>| <img src="./logistic_regression_CIC2019.png" width="100%">  |


Questa cartella contiene due notebook che mostrano le proprietà della Logistic Regression in problemi di classificazione.

Il notebook [LogisticRegressionTwoFeatures.ipynb](./LogisticRegressionTwoFeatures.ipynb) mostra le diverse prestazioni della Logistic Regression e della Logistic Regression polinomiale su dati sintetici, sia linearmente separabili che non linearmente separabili.
Il notebook [LogisticRegression.ipynb ](./LogisticRegression.ipynb)implementa un classificatore binario per il traffico di rete, che distingue i flussi di traffico tra benigni e dannosi. 