# Algoritmi di Machine Learning per la rilevazione di attacchi informatici

Questo corso introdurrà gli studenti agli aspetti teorici e pratici dell’implementazione di algoritmi di Machine Learning (ML) per il rilevamento attacchi di rete. Gli argomenti includono l’analisi del traffico di rete malevolo, la progettazione e l’ottimizzazione dei modelli di ML, e le sfide legate all’implementazione dei sistemi di rilevamento delle intrusioni di rete (NIDS) basati su ML in contesti reali.

Alla fine del corso, gli studenti avranno una comprensione delle basi tecniche dei NIDS basati su ML, oltre alle competenze pratiche necessarie per progettare, sviluppare, implementare e validare questi sistemi. Sessioni di laboratorio pratiche forniranno agli studenti esperienza nell’uso di dataset reali e strumenti di ML per rilevare attività malevole. Gli studenti acquisiranno inoltre le competenze necessarie per implementare con sicurezza NIDS basati su ML in scenari reali e proteggere le reti da intrusioni e attacchi informatici.

In questo repository viene messo a disposizione degli studenti il codice dei laboratori eseguiti durante il corso.
Il codice e' basato su Python e Jupyter Notebook (https://jupyter.org/) e si trovera' preinstallato nelle Macchine Virtuali (VM) configurate nel laboratorio dedicato al corso.


## Installazione dell'ambiente di sviluppo (opzionale)
Il codice puo' anche essere installato su un qualsiasi computer Linux, Mac o Windows seguendo le istruzioni riportate di seguito:


Il consiglio e' di usare ambienti Python virtuali conda (https://docs.conda.io/projects/conda/en/latest/) per evitare di inerferire con le librerie Python di sisrtema. 
In particolare, si consiglia di installare miniconda, una versione leggera di conda. Miniconda è disponibile per Windows, macOS e Linux e può essere installato seguendo le linee guida disponibili a questo link: https://docs.conda.io/en/latest/miniconda.html.

Per Windows, è richiesto Windows 10 versione 2004 o superiore (Build 19041 o superiore) oppure Windows 11. Su Windows, per prima cosa installa il sottosistema Windows per Linux (WSL) utilizzando il seguente comando da terminale:
```
wsl.exe --install
```
(consulta questo [link](https://learn.microsoft.com/en-us/windows/wsl/install) per ulteriori informazioni). 
Questo comando installerà un sistema operativo Ubuntu Linux sul tuo computer. Puoi accedere alla riga di comando di Linux eseguendo l’app WSL dal menu Start di Windows e successivamente seguire le istruzioni per il sistema operativo Linux.

Apri un terminale, esegui uno dei seguenti comandi (in base al tuo sistema operativo) e segui le istruzioni visualizzate:

```
bash Miniconda3-latest-Linux-x86_64.sh (on Linux operating systems)
bash Miniconda3-latest-MacOSX-x86_64.sh (on macOS)
```

Quindi crea un nuovo ambiente conda (chiamato ```python39```) basato su Python 3.9:

```
conda create -n python39 python=3.9
```

e configura l’ambiente con ```TensorFlow``` e alcuni altri pacchetti:

Su sistemi operativi Linux:

```
(python39)$ pip install tensorflow==2.7.1 numpy==1.26.4 protobuf==3.19.6
(python39)$ pip install scikit-learn h5py pyshark matplotlib jupyter graphviz
```

Per macOS (con CPU Apple M1, M2 and M3):

```
(python39)$ conda install -c conda-forge tensorflow=2.7.1 numpy=1.26.4
(python39)$ conda install -c conda-forge scikit-learn h5py pyshark matplotlib jupyter graphviz
```
