# Analisi dell'importanza delle features con Random Forest
In questo laboratorio utilizzerai una Random Forest per valutare l’importanza relativa delle features del set di addestramento. Questa tecnica viene spesso utilizzata per eliminare le features irrilevanti prima dell’addestramento.

Utilizzerai un dataset contenente traffico benigno e vari tipi di attacchi DDoS, estratto dal dataset CIC-DDoS2019 (https://www.unb.ca/cic/datasets/ddos-2019.html).
Il traffico di rete è stato precedentemente pre-elaborato in modo che i pacchetti siano raggruppati in flussi di traffico bidirezionali utilizzando il 5-tuple (IP sorgente, IP destinazione, Porta sorgente, Porta destinazione, protocollo).
Ogni flusso è rappresentato da 21 features dell’header dei pacchetti, calcolate su un massimo di 1000 pacchetti.

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