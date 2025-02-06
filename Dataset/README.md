# Datasets
Le tracce di traffico in formato ```pcap``` ed files ```hdf5``` in questa cartella sono stati ottenuti dal dataset CIC-DDoS2019 fornito dal Canadian Institute for Cybersecurity dell’Università del New Brunswick (UNB).
I files ```pcap``` sono divisi per classi di traffico. Un file contiene solo traffico *benigno*, mentre gli altri files contengono un tipo di attacco DDoS diverso ognuno.

I files con estensione ```hdf5``` contengono dei campioni di traffico ottenuti dalle tracce di traffico ```pcap```. Questi campioni sono delle rappresentazioni dei flussi di traffico presenti nei files ```pcap```. Ogni flusso e' rappresentato tramite 21 caratteristiche (ad esempio, dimensione media dei suoi pacchetti in bytes) ed un'etichetta (label) rappresentata con un numero intero da ```0``` a ```4``` con il seguente significato:
- ```0``` indica che il flusso e' di tipo benigno 
- ```1``` flusso di attacco DDoS basato su traffico DNS 
- ```2``` flusso di attacco DDoS di tipo Syn Flood
- ```3``` flusso di attacco DDoS di tipo UDP lag
- ```4``` flusso di attacco DDoS su protocollo HTTP (WebDDoS)

Come descritto sopra, i files ```hdf5``` sono ottenuti dalle tracce di traffico ```pcap``` ri-elaborate in modo che i pacchetti siano raggruppati in flussi di traffico bidirezionali utilizzando il 5-tuple (IP sorgente, IP destinazione, Porta sorgente, Porta destinazione, protocollo). Ogni flusso è rappresentato da 21 caratteristiche (dette *Features*) del header dei pacchetti, calcolate usando un massimo di 1000 pacchetti per flusso:

| Feature nr.         | Nome Feature |
|---------------------|---------------------|
| 00 | timestamp (media IAT) | 
| 01 | packet_length (media)| 
| 02 | IP_flags_df (somma) |
| 03 | IP_flags_mf (somma) |
| 04 | IP_flags_rb (somma) | 
| 05 | IP_frag_off (somma) |
| 06 | protocols (media) |
| 07 | TCP_length (media) |
| 08 | TCP_flags_ack (somma) |
| 09 | TCP_flags_cwr (somma) |
| 10 | TCP_flags_ece (somma) |
| 11 | TCP_flags_fin (somma) |
| 12 | TCP_flags_push (somma) |
| 13 | TCP_flags_res (somma) |
| 14 | TCP_flags_reset (somma) |
| 15 | TCP_flags_syn (somma) |
| 16 | TCP_flags_urg (somma) |
| 17 | TCP_window_size (media) |
| 18 | UDP_length (media) |
| 19 | ICMP_type (media) |
| 20 | Packets (contatore)|

## Acknowlegments
The traffic traces and the pre-processed samples in this folder were obtained from the CIC-DDoS2019 dataset provided by the Canadian Institute for Cybersecurity of the University of New Brunswick (UNB). CIC-DDoS2019 and other datasets are publicly available on the [UNB website](https://www.unb.ca/cic/datasets/index.html). 

More details about the [CIC-DDoS2019](https://www.unb.ca/cic/datasets/ddos-2019.html) dataset can be found in the following scientific paper:

*Iman Sharafaldin, Arash Habibi Lashkari, Saqib Hakak, and Ali A. Ghorbani, "Developing Realistic Distributed Denial of Service (DDoS) Attack Dataset and Taxonomy", IEEE 53rd International Carnahan Conference on Security Technology, Chennai, India, 2019.*