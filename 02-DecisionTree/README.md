# Alberi decisionali

In questo laboratorio, analizzeremo le proprietà dei Decision Trees (DT), o Alberi Decisionali, attraverso un problema di classificazione del traffico di rete.

In particolare, utilizzeremo un dataset composto da traffico benigno e quattro tipi di attacchi DDoS: SYN Flood, UDP Lag, WebDDoS e un attacco DDoS basato su riflessione DNS. Questi attacchi fanno parte del dataset CIC-DDoS2019 (https://www.unb.ca/cic/datasets/ddos-2019.html).

L’Albero Decisionale classifica il traffico in cinque classi (traffico benigno o uno dei tipi di attacco) e i risultati vengono visualizzati utilizzando metriche di accuratezza come Accuratezza, Falsi Positivi/Negativi, etc.

Il codice di questa dimostrazione è disponibile nel seguente Jupyter notebook: [decision-tree-dos2019.ipynb](./decision-tree-dos2019.ipynb).

Inoltre, considereremo un problema di regressione (previsione di un numero reale) con un dataset sintetico: [decision-tree-regression.ipynb](./decision-tree-regression.ipynb). In questo caso, useremo un albero decisionale per rilevare anomalie di rete.