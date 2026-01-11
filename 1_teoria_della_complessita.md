# Riassunto - Teoria della Complessità

La teoria della complessità classifica i problemi in base alla difficoltà di risolverli efficientemente. Si concentra sui **problemi decisionali** (output SI o NO), poiché la trattazione formale è più agevole e permette di trarre conclusioni applicabili anche ad altri tipi di problemi.

**Esempio**: Il problema **Shortest Path** può essere espresso sia come problema di ottimizzazione (qual è la lunghezza del cammino minimo?) che come problema decisionale (esiste un cammino di lunghezza $\leq k$?).

***
## Classificazione dei problemi
#### Classe P (Polynomial Time) - "I Facili"
Sono i problemi che un computer può **RISOLVERE** velocemente (in tempo polinomiale, $O(n^k)$).

- **Esempio:** Ordinare una lista (Sorting), trovare il cammino minimo (Dijkstra).
	
- **Nota:** Se un problema è in P, è automaticamente anche in NP.

#### Classe NP (Nondeterministic Polynomial Time) - "I Verificabili"
Sono i problemi per cui, se io ti do una soluzione ("il certificato"), tu puoi **VERIFICARE** velocemente se è corretta con un algoritmo deterministico in tempo polinomiale.

- _Definizioni utili_
	- **Certificato**: sequenza di caratteri di dimensione al massimo polinomiale che contiene l'evidenza che un'istanza $i$ sia positiva per il problema Π.
		
	- **Algoritmo verificatore**: algoritmo decisionale che prende in input un'istanza $i$ e un certificato $C_i$, restituendo SI se $i$ è positiva per Π, NO altrimenti.
	
- **Esempio:** Fare un Sudoku è difficile (ci metti tempo a risolverlo), ma se ti do un Sudoku già compilato, ci metti un attimo a controllare se le regole sono rispettate.
    
- **Relazione:** $P \subseteq NP$. (Se so risolvere un problema velocemente, so anche verificare la soluzione velocemente).

#### Classe NP-Hard - "I Più Cattivi di Tutti"
Qui usciamo dal recinto dei problemi "trattabili". Un problema è NP-Hard se è **almeno** difficile quanto il problema più difficile in NP.
	
- **La Chiave (Riduzione):** Un problema $H$ è NP-Hard se **ogni** problema in NP può essere ridotto (trasformato) in $H$ in tempo polinomiale.
    
- **Significato:** Se trovassi un modo veloce per risolvere un problema NP-Hard, avrei trovato un modo veloce per risolvere _tutti_ i problemi in NP (e quindi avrei dimostrato che P=NP).
    
- **Nota:** Un problema NP-Hard **non deve per forza essere in NP**. Potrebbe essere così difficile che non riesci nemmeno a verificare la soluzione velocemente (o potrebbe essere indecidibile, come l'Halting Problem).

#### Classe NP-Complete - "L'Intersezione Critica"
Questi sono i problemi "chiave". Sono sia in NP che NP-Hard.

- **Definizione:** Un problema $C$ è NP-Complete se soddisfa due condizioni:
    1. $C \in NP$ (è verificabile efficientemente).
        
    2. $C \in$ NP-Hard (tutti i problemi in NP si riducono a lui).
        
- **Concetto Chiave:** Rappresentano il "nucleo" della difficoltà di NP.
    
- **Esempi:** Vertex Cover, 3-SAT, TSP Decisionale.

#### Domanda: Il problema del commesso viaggiatore (TSP) è NP-Complete?
	
- **TSP Decisionale:** "Esiste un ciclo di costo minore di $k$?" $\rightarrow$ **NP-Complete**. (Posso verificare se un ciclo dato costa meno di $k$).
    
- **TSP di Ottimizzazione:** "Trovami il ciclo di costo minimo assoluto." $\rightarrow$ **NP-Hard**, ma **non** NP-Complete.
    
    - _Perché?_ Se ti do una soluzione e ti dico "Questa è la minima", tu non hai un modo veloce per verificare che non ne esista una ancora più piccola da qualche parte. Devi fidarti. Quindi non è in NP (come definito classicamente per i problemi decisionali).

### Come rappresentiamo queste classi di problemi mantenendo il dubbio che in futuro si possano trovare degli algoritmi polinomiali risolutori dei problemi NP?
A sinistra siamo nel caso in cui i problemi NP potrebbero essere risolti in tempo polinomiale, a destra nel caso sia stato dimostrato che non esiste un algoritmo polinomiale per i problemi NP.
![[Pasted image 20260111133929.png]]

| **Classe**      | **Trovare Soluzione (Tempo Polinomiale)** | **Verificare Soluzione (Tempo Polinomiale)** | **Relazione Insiemistica**                  |
| --------------- | ----------------------------------------- | -------------------------------------------- | ------------------------------------------- |
| **P**           | **SÌ**                                    | **SÌ**                                       | $P \subseteq NP$                            |
| **NP**          | **NO** (o non lo sappiamo)                | **SÌ**                                       | Contiene P e NP-Complete                    |
| **NP-Complete** | **NO**                                    | **SÌ**                                       | Intersezione tra NP e NP-Hard               |
| **NP-Hard**     | **NO**                                    | **NO** (non garantito)                       | Almeno difficile quanto ogni problema in NP |
***
TODO:
- [ ] Riduzione di karp
- [ ] esempio con tsp e ciclo hamiltoniano

***
## Confrontiamo la difficoltà di due algoritmi: **Riduzione di Karp**

**Definizione**: Un problema decisionale $A$ è **riducibile in tempo polinomiale** a $B$ ($A \leq_p B$) se:

- Ogni istanza di $A$ _può essere trasformata_ in tempo polinomiale in un'istanza di $B$
- Ogni istanza positiva di $A$ viene trasformata in un'istanza positiva di $B$
- Ogni istanza negativa di $A$ viene trasformata in un'istanza negativa di $B$

**Intuizione**: $A \leq_p B$ significa che:

- Il problema $B$ non è più facile di $A$ (un algoritmo per $B$ può risolvere $A$)
- Il problema $A$ non è più difficile di $B$

![[Pasted image 20260111173456.png]]

## **Conseguenze**

Se $A \leq_p B$ allora:

- $B \in P \Rightarrow A \in P$ 🚀 abbiamo un algoritmo polinomiale per $A$  🚀
- $A \notin P \Rightarrow B \notin P$  non abbiamo un algoritmo polinomiale per A 🥲, quindi neanche per B 🥲 
- $B \leq_p A \Rightarrow A \equiv B$ i problemi sono equivalentemente difficili

**Proprietà**: La riduzione polinomiale è **transitiva**: $A \leq_p B \land B \leq_p C \Rightarrow A \leq_p C$.

![[Pasted image 20260111174028.png|400]] ![[Pasted image 20260111174046.png|400]]
![[Pasted image 20260111174224.png|400]]

***
## **Classe NP (Non-deterministic Polynomial Time)**

## **Esempio: Ciclo Hamiltoniano**

- **INPUT**: Grafo $G = (V, E)$
- **OUTPUT**: Esiste un ciclo in $G$ che passa per tutti i nodi esattamente una volta?

![[Pasted image 20260111181443.png|500]]

Per questo problema:

- Non si conoscono algoritmi polinomiali
- Un algoritmo forza bruta richiede tempo **fattoriale**
- Possiamo **verificare** una soluzione in tempo polinomiale: data una permutazione dei nodi, possiamo verificare in tempo lineare se rappresenta un ciclo hamiltoniano

![[Pasted image 20260111181847.png|400]]

## **Classe NP-Completo**

**Definizione**: Un problema decisionale $A$ è **NP-completo** se:

1. $A \in NP$
2. $\forall B \in NP : B \leq_p A$

## **Come dimostrare che un Problema è NP-Completo**

Per dimostrare che $A$ è NP-completo, sfruttiamo la transitività della riduzione:

1. Dimostrare che $A \in NP$
2. Scegliere un problema $B$ già dimostrato NP-completo
3. Dimostrare che $B \leq_p A$

**Teoremi di Cook** (1971) **e Levin** (1973): Il primo problema dimostrato NP-completo è **SAT** (Satisfiability).

**SAT**: Data una formula in forma normale congiuntiva (FNC), esiste un assegnamento di verità che la renda vera?

- Esempio: $(a \lor b \lor c) \land (\neg b \lor c) \land (\neg a \lor \neg b \lor c)$

## **Teorema Fondamentale**

Se si dimostra che un problema NP-completo:

1. Ha un algoritmo polinomiale, allora $P = NP$
2. Non ha algoritmi polinomiali, allora $P \neq NP$

***

## **Classe NP-Hard**

**Definizione**: Un problema $A$ (non necessariamente decisionale) è **NP-hard** se:

- $\forall B \in NP : B \leq_p A$

**Differenza con NP-completo**: un problema NP-hard non è necessariamente in NP (ad esempio, problemi di ottimizzazione).

## **Come Dimostrare che un Problema è NP-Hard**

Per dimostrare che $A$ è NP-hard:

1. Scegliere un problema $B$ già dimostrato NP-completo
2. Dimostrare che $B \leq_p A$

![[Pasted image 20260111182131.png]]

_N.B.: Non è detto che A abbia un algoritmo verificatore polinomiale_

## **Soluzioni per Problemi NP-Hard**

Molti problemi NP-hard hanno importanti applicazioni e non possono essere ignorati. Possibili soluzioni:

- Risolvere efficientemente solo istanze piccole
- Utilizzare euristiche
- Utilizzare algoritmi paralleli/distribuiti
- Utilizzare **algoritmi di approssimazione**: restituiscono in tempo polinomiale una soluzione ammissibile con garanzie sul discostamento dal costo ottimo

***
### **Teorema: Il problema del Commesso Viaggiatore (TSP) è NP-Hard**

Obiettivo: Dimostrare che $HC \leq_p TSP$ (Optimization).

Poiché il problema del Ciclo Hamiltoniano ($HC$) è noto essere NP-Completo, se dimostriamo che esso è riducibile polinomialmente al TSP di ottimizzazione, allora il TSP è almeno tanto difficile quanto un problema NP-Completo, dunque è NP-Hard.

#### **1. Definizione della Riduzione**

Dobbiamo costruire un algoritmo di trasformazione $f$ che operi in tempo polinomiale.

- **Input (Istanza HC)**: Un grafo orientato o non orientato $G = (V, E)$.
	
- **Output (Istanza TSP)**: Un grafo completo ponderato $G' = (V, E')$ con una funzione di costo $c: E' \rightarrow \mathbb{N}$.

**Costruzione di $G'$:**

1. L'insieme dei vertici $V$ rimane lo stesso.
    
2. L'insieme degli archi $E'$ include tutti i possibili archi tra i vertici di $V$ (ovvero, $G'$ è un grafo completo $K_{|V|}$).
    
3. Definiamo la funzione di costo $c(u, v)$ per ogni arco $(u, v) \in E'$ come:
    $$c(u, v) = \begin{cases} 0 & \text{se } (u, v) \in E \quad (\text{l'arco esisteva nel grafo originale}) \\ 1 & \text{se } (u, v) \notin E \quad (\text{l'arco non esisteva}) \end{cases}$$

_Nota: La costruzione di $G'$ richiede di iterare su tutte le coppie di nodi, impiegando un tempo $O(|V|^2)$, che è polinomiale._

#### **2. Dimostrazione di Correttezza**

Sia $C_{min}$ il costo del ciclo hamiltoniano di costo minimo in $G'$ trovato risolvendo il TSP.

**Caso A: $G$ ha un Ciclo Hamiltoniano $\implies C_{min} = 0$**

- **Ipotesi**: Esiste un ciclo hamiltoniano in $G$.
    
- **Tesi**: Il TSP su $G'$ ha costo 0.
    
- **Dimostrazione**: Se esiste un ciclo in $G$, esso è composto esclusivamente da archi appartenenti a $E$. Nella nostra costruzione, tutti gli archi in $E$ hanno costo $0$ in $G'$. Pertanto, esiste un tour in $G'$ che visita tutti i nodi con costo totale $0$. Poiché i pesi non sono negativi, questo è necessariamente il minimo.
    

Caso B: $G$ non ha un Ciclo Hamiltoniano $\implies C_{min} > 0$

(Dimostriamo la contronominale: Se $C_{min} = 0 \implies G$ ha un HC).

- **Ipotesi**: Il TSP trova un tour in $G'$ con costo totale $0$.
    
- **Tesi**: Esiste un ciclo hamiltoniano in $G$.
    
- **Dimostrazione**: Se il costo totale del tour è $0$, significa che il tour utilizza _solo_ archi con peso $0$. Per la nostra funzione di costo, gli archi di peso $0$ in $G'$ corrispondono esattamente agli archi esistenti in $E$ del grafo $G$. Poiché un tour TSP visita ogni nodo esattamente una volta e torna all'inizio, questo corrisponde per definizione a un Ciclo Hamiltoniano formato solo da archi originali di $G$.

#### **3. Conclusione**

Abbiamo mostrato che:

1. L'algoritmo TSP su $G'$ restituisce $0$ se e solo se $G$ ammette un Ciclo Hamiltoniano.
    
2. L'algoritmo TSP su $G'$ restituisce un valore $\ge 1$ se $G$ non ammette un Ciclo Hamiltoniano.
    

Dato che $HC$ è NP-Completo e la riduzione è polinomiale, il **TSP (versione ottimizzazione) è NP-Hard**.

### Piccolo dettaglio teorico interessante
In alcuni libri al posto di usare i pesi 0 e 1, vengono usati 1 e 2... come mai?
### Il motivo teorico: TSP Metrico vs TSP Generale

Nella tua dimostrazione con pesi 0 (arco presente) e 1 (arco assente), proviamo a vedere se vale la Disuguaglianza Triangolare:

$$c(u, w) \le c(u, v) + c(v, w)$$

Immagina tre nodi $u, v, w$:

1. Esiste l'arco $(u, v)$ nel grafo originale $\rightarrow$ peso $0$.
    
2. Esiste l'arco $(v, w)$ nel grafo originale $\rightarrow$ peso $0$.
    
3. **NON** esiste l'arco $(u, w)$ nel grafo originale $\rightarrow$ peso $1$.
    

Controlliamo la disuguaglianza:

$$c(u, w) \le c(u, v) + c(v, w)$$
$$1 \le 0 + 0$$
$$1 \le 0$$

Falso! La disuguaglianza triangolare NON vale.

#### Perché è importante?

Se usiamo pesi **1** (arco presente) e **2** (arco assente):

1. Disuguaglianza nel caso peggiore (scorciatoia non esistente):
    
    $$c(u, w) \le c(u, v) + c(v, w)$$
    
    $$2 \le 1 + 1$$
    
    $$2 \le 2$$
    
    Vero!
    

Conclusione Accademica:

Usando pesi 1 e 2, dimostriamo che anche il "Metric TSP" (TSP dove vale la disuguaglianza triangolare) è NP-Complete.

Questa è una dimostrazione più forte: stiamo dicendo che il problema rimane difficile anche se imponiamo regole geometriche sensate (come appunto la disuguaglianza triangolare).

Se usassimo 0 e 1 (o pesi arbitrariamente grandi per i non-archi, tipo $M$), staremmo dimostrando la difficoltà solo del **TSP Generale**, che è un risultato corretto ma meno potente, perché il TSP Generale non è nemmeno approssimabile (Teorema di non approssimabilità), mentre il Metric TSP sì.
# OLD

## **Esempio: TSP (Travelling Salesman Problem)**

**INPUT**: Grafo completo con archi pesati
**OUTPUT**: Ciclo hamiltoniano di costo minimo

**Teorema**: Il TSP è NP-hard

Devo dimostrare che  $Ciclo Hamiltoniano \leq_p TSP$, quindi devo risolvere il problema del ciclo Hamiltoniano con il TSP.

Istanza CicloHamiltoniano --> TRASFORMAZIONE input --> Istanza TSP --> Algoritmo TSP --> TRASFORMAZIONE risultato --> Output Sì/No

Ci servono quindi due algoritmi polinomiali di trasformazione.
#### TRASFORMAZIONE Istanza
Il problema del Ciclo Hamiltoniano prende in input un grafo qualunque, mentre il TSP ha bisogno di un grafo connesso e pesato.
Quindi dato un grafo $G = (V, E)$, creiamo $G' = (V, E')$ completo con pesi:
- Agli archi già presenti assegno costo 0
- Agli archi che aggiungo assegno costo 1

#### TRASFORMAZIONE Risultato
Eseguo l'algoritmo del TSP.
Se il ciclo hamiltoniano minimo ha costo:
- 0 --> allora il ciclo hamiltoniano è presente anche nel Grafo originale (Risposta Sì)
- 1 --> allora il ciclo hamiltoniano non è presente nel Grafo originale (Risposta No)

**In Sintesi**: Riduciamo il problema del Ciclo Hamiltoniano (NP-completo) al TSP:

1. Dato un grafo $G = (V, E)$, creiamo $G' = (V, E')$ completo con pesi:
   - $c(e) = 0$ se $e \in E$
   - $c(e) = 1$ altrimenti
2. Se il ciclo hamiltoniano di costo minimo in $G'$ ha costo 0, allora $G$ ha un ciclo hamiltoniano
3. Se ha costo $> 0$, allora $G$ non ha ciclo hamiltoniano

Dato che abbiamo dimostrato che il problema del TSP è almeno difficile quanto un problema np-completo standard (ciclo hamiltoniano), possiamo dire che il TSP è NP-hard.
