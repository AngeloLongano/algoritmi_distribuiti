#### Modulo A: Teoria della Complessità (Focus: Algoritmi di Approssimazione)

1. **Analisi Asintotica e Ricorrenze:**
    
    - Ripasso veloce $O, \Omega, \Theta$.
        
    - **Master Theorem**: Saperlo applicare istantaneamente.
        
2. **Classi P, NP, NP-Hard:**
    
    - Definizione formale di riduzione polinomiale.
        
    - Capire perché i problemi seguenti sono difficili.
        
3. **Approssimazione Vertex Cover (VC):**
    
    - Algoritmo Greedy (Matching Massimale) $\to$ 2-approx.
        
    - Dimostrazione del fattore di approssimazione.
        
    - Rilassamento Lineare (LP) e arrotondamento (Rounding).
        
4. **Approssimazione TSP (Metric TSP):**
    
    - Algoritmo basato su MST (2-approx) _[Facoltativo ma utile]_.
        
    - **Algoritmo di Christofides** (1.5-approx): **Cruciale**. Devi saper costruire il grafo euleriano unendo MST e Matching Perfetto di peso minimo.
        

#### Modulo B: Il Modello e Algoritmi Base

1. **Il Modello Distribuito:**
    
    - Definizione di Entità, Link, Assiomi (topologia finita, connessa, ecc.).
        
    - Metriche: Message Complexity vs Time Complexity (ideale).
        
2. **Broadcast e Traversal:**
    
    - **Flooding:** Semplice, ma quanto costa? ($\Omega(m)$).
        
    - **Spanning Tree Broadcast:** Se abbiamo già l'albero.
        
3. **Spanning Tree Construction:**
    
    - **Algoritmo Shout:** Funzionamento e perché serve per costruire lo spanning tree.
        
    - **Shout+:** Ottimizzazione per grafi sparsi.
        
    - Analisi esatta dei messaggi scambiati.
        

#### Modulo C: Elezione del Leader (Il cuore del corso)

1. **Impossibilità:**
    
    - Simmetria e Anonymity: Perché non possiamo eleggere un leader se tutti sono uguali senza ID?
        
2. **Ring Networks (Anello):**
    
    - **All-the-way:** $O(n^2)$ messaggi. Caso peggiore vs caso medio.
        
    - **As-Far-As-It-Can (LCR):** Introduzione del filtraggio.
        
    - **Hirschberg (Distance Constraint):** Algoritmo a fasi $O(n \log n)$. Questo è complesso, richiede tempo per capire la logica dei $2^k$ passi.
        
    - Lower Bound: Dimostrazione intuitiva del perché $\Omega(n \log n)$ è il limite inferiore.
        
3. **Grafi Generici:**
    
    - Elezione su grafi arbitrari (basata su Spanning Tree/Extrema Finding).
        

#### Modulo D: Sistemi Sincroni, Routing & Faults

1. **Sincronia:**
    
    - Differenza tra "Round" e "Tempo asincrono".
        
    - Algoritmo Min-Finding in sistemi sincroni.
        
2. **Routing:**
    
    - Routing Tables e efficienza spaziale.
        
    - Shortest Path distribuito (rilassamento distribuito).
        
3. **Fault Tolerance (Guasti):**
    
    - Modelli: Crash vs Byzantine.
        
    - **Consenso:** Problema dei due generali (Impossibilità su canali inaffidabili).
        
    - **Generali Bizantini:** $3f+1$. Capire l'algoritmo orale per $f=1$ (o capire perché con 3 nodi e 1 traditore non funziona).
        

#### Modulo E: Distributed Hash Tables (DHT)

1. **P2P & Overlay Networks:** Concetto base.
    
2. **CHORD:**
    
    - Consistent Hashing (l'anello degli ID).
        
    - Finger Table: struttura logaritmica.
        
    - Lookup: come funziona la ricerca della chiave $O(\log n)$.
        
    - Join/Leave: cenni sulla stabilizzazione.