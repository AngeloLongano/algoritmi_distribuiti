# Schema Macroscopico - Algoritmi Distribuiti

## 0. Ripasso sugli algoritmi [qui](0_ripasso_complessità.md)

## 1. Teoria della Complessità [qui](1_teoria_della_complessita.md)

- Classificazione dei problemi (decisionali, ricerca, ottimizzazione)
- Classi di complessità: **P**, **NP**, **NP-completo**, **NP-hard** [qui](schema_classi_problemi.md)
- Riduzioni polinomiali (Riduzione di Karp)
- Notazione asintotica (O-grande, Omega, Theta)
- Problemi trattabili, intrattabili, irrisolvibili

***

## 2. Problema TSP e Algoritmi di Approssimazione

- Problema del Commesso Viaggiatore (TSP)
- Algoritmo MST-based (2-approssimazione)
- Algoritmo di Christofides (3/2-approssimazione)
- Branch and Bound applicato al TSP

***

## 3. Vertex Cover Problem

- Algoritmo greedy (2-approssimazione)
- Programmazione lineare intera (ILP) e rilassamento
- Tight approximation analysis

***

## 4. Fondamenti dei Sistemi Distribuiti

- Modello dei sistemi distribuiti
  - Entità, stato, eventi, azioni, comportamento
  - Rappresentazione a grafo
- Assiomi e restrizioni
  - Restrizioni su comunicazione, affidabilità, topologia, tempo
- Misure di efficienza: tempo, spazio, comunicazione

***

## 5. Problemi Base nei Sistemi Distribuiti

### 5.1 Broadcast e Wake-Up

- Flooding protocol
- Broadcast su grafi completi
- Wake-up problem con iniziatori multipli

### 5.2 Spanning Tree Construction

- Protocollo SHOUT (BFS)
- Depth-First Spanning Tree (DFS) con token
- Spanning Tree con iniziatori multipli

### 5.3 Computation on Trees

- Saturation (convergenza verso radice)
- Minimum Finding su alberi
- Rooted vs Unrooted Trees

***

## 6. Leader Election

- Teorema di Angluin (impossibilità senza ID univoci)
- Leader Election su Ring
  - All-the-way (Le Lann)
  - As-far-as-it-can (LCR)
  - Controlled Distance (fasi successive)
- Leader Election su alberi
- Leader Election su grafi generici (Flood Algorithm)

***

## 7. Routing Distribuito

- Shortest Path Routing
  - MapGossip
  - Iterating (Distance Vector)
  - Dijkstra distribuito (SPST)
- Min-Hop Routing (BFST)

***

## 8. Sistemi Sincroni

- Modello sincrono e comunicazione locale
- Upper bound alla comunicazione
- Leader Election sincrona
  - Speeding Algorithm
  - Waiting Protocol
- Randomized Leader Election (senza ID univoci)
- Misurare il silenzio

***

## 9. Tolleranza ai Guasti

### 9.1 Modelli di Fallimento

- Link failures
- Crash failures
- Byzantine failures

### 9.2 Broadcast Fault-Tolerant

- Problema dei due generali (impossibilità)
- TwoSteps Protocol (link failures)
- Broadcast con crash ed entity faults

### 9.3 Consensus Problem

- Impossibilità FLP (consensus asincrono)
- Consensus in sistemi sincroni (TellAll-Crash)
- Randomized Consensus (Ben-Or)
- Byzantine Consensus (sincrono e asincrono)

***

## 10. Distributed Hash Tables (DHT)

- Evoluzione dei sistemi P2P
  - Napster (centralizzato)
  - Gnutella (decentralizzato)
  - KaZaA (ibrido)
- Chord Protocol
  - Consistent Hashing
  - Finger Table
  - Node Join e Stabilization Protocol
  - Look-up operations
