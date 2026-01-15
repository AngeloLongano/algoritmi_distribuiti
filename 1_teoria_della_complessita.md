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

Obiettivo: Dimostrare che $TSP (Optmization) \geq_p HC (decisionale)$.

_Vogliamo dimostrare che se avessimo un oracolo (un algoritmo efficiente) in grado di risolvere il TSP, potremmo usarlo per risolvere il problema del Ciclo Hamiltoniano (HC)._

Poiché il problema del Ciclo Hamiltoniano ($HC$) è noto essere NP-Completo, se dimostriamo che esso è riducibile polinomialmente al TSP di ottimizzazione, allora il TSP è almeno tanto difficile quanto un problema NP-Completo, dunque è NP-Hard.

#### **1. Intuizione e Strategia della Riduzione**

Il problema $HC$ è un problema decisionale (Esiste un ciclo? Sì/No), mentre il $TSP$ è un problema di ottimizzazione (Trova il ciclo di costo minimo).

Per collegarli, dobbiamo trasformare la struttura topologica del grafo di HC in costi per il TSP.

L'idea chiave è penalizzare l'uso di archi non esistenti:

- Assegniamo costo **0** agli archi che esistono realmente (nessuna penalità).
- Assegniamo costo **1** agli archi che non esistono (penalità).

In questo modo, il costo totale del tour fungerà da "rivelatore": se il costo è 0, il tour non ha mai "barato" (ha usato solo archi esistenti); se il costo è $\ge 1$, il tour è stato costretto a "barare" (ha usato archi che non c'erano in origine).

![[Pasted image 20260113182650.png]]

#### **2. Definizione Formale della Riduzione**

Costruiamo un algoritmo di trasformazione $f$ che mappa un'istanza $G$ di HC in un'istanza $G'$ di TSP.
- **Input:** Grafo $G = (V, E)$.
- **Output:** Grafo completo ponderato $G' = (V, E')$ con funzione costo $c$.

**Costruzione di $G'$:**

1. **Vertici:** $V' = V$ (stessi nodi).
2. **Archi:** $E' = V \times V$ (grafo completo: colleghiamo tutto con tutto).
3. Pesi: Per ogni coppia $(u, v)$, il peso è definito come:$$c(u, v) = \begin{cases} 0 & \text{se } (u, v) \in E \quad (\text{arco originale}) \\ 1 & \text{se } (u, v) \notin E \quad (\text{arco fittizio}) \end{cases}$$
_Nota: La costruzione di $G'$ richiede di iterare su tutte le coppie di nodi, impiegando un tempo $O(|V|^2)$, che è polinomiale.

![[Code_Generated_Image.png|500]]
#### **3. Dimostrazione di Correttezza**

Sia $C_{min}$ il valore della soluzione ottima restituita dal TSP su $G'$. 
Dobbiamo dimostrare che $C_{min} = 0 \iff G \text{ ha un HC}$.

**Direzione A**

> **Ipotesi:** $G \text{ ha un HC} \implies$ **Tesi:**  $C_{min} = 0$

- **Ragionamento:** Se $G$ ha un ciclo Hamiltoniano, esiste una permutazione di vertici collegati solo da archi in $E$.
    
- **Nel grafo TSP:** Poiché abbiamo mappato tutti gli archi di $E$ con peso $0$, questo ciclo esiste anche in $G'$ e ha costo somma $0$. Dato che i pesi sono non-negativi, $0$ è il minimo possibile.
    
- **Conclusione:** L'algoritmo TSP troverà questo tour (o uno equivalente) e restituirà $0$.

Direzione B

> **Ipotesi:** $C_{min} = 0 \implies$ **Tesi:**  $G$ ha un HC

(Utilizziamo l'implicazione diretta sul valore del costo, che è più intuitiva della contronominale per chi legge).

- **Ragionamento:** Supponiamo che l'algoritmo TSP restituisca un tour di costo $0$.
    
- **Analisi dei pesi:** Poiché la somma dei pesi è $0$ e i pesi possibili sono solo $\{0, 1\}$, questo implica che **ogni singolo arco** del tour ha peso $0$.
    
- **Legame con $G$:** Per costruzione, un arco ha peso $0$ in $G'$ solo se esisteva in $G$.
    
- **Conclusione:** Il tour trovato dal TSP è quindi composto esclusivamente da archi originali di $G$. Poiché un tour TSP visita ogni nodo esattamente una volta, questo corrisponde esattamente alla definizione di Ciclo Hamiltoniano in $G$.

**Nota logica**
Dimostrando $C_{min} = 0 \implies G \text{ ha un HC}$  abbiamo dimostrato anche la sua contronominale:

> **Ipotesi:** $G \text{ non ha un HC} \implies$ **Tesi:**  $C_{min} \ne 0$ _(C non può essere negativa, quindi $C_{min} \ge 1$)_

Infatti, se $C_{min} \ge 1$, significa che ogni possibile tour deve usare almeno un arco fittizio, quindi non esiste un HC in $G$._
#### **4. Conclusione**

La riduzione è polinomiale e valida. Risolvere il TSP permette di decidere HC:

- Se $TSP(G') = 0 \rightarrow$ Risposta HC: **SÌ**.
	
- Se $TSP(G') \ge 1 \rightarrow$ Risposta HC: **NO**.

Poiché HC è NP-Completo, **TSP (Ottimizzazione) è NP-Hard**.

***
### **Approfondimento: Perché scegliere pesi 1 e 2 invece di 0 e 1?**

La scelta dei pesi nella riduzione non è casuale, ma determina **quale variante** del TSP stiamo dimostrando essere NP-Hard.

#### **1. Il Test della Disuguaglianza Triangolare**

La disuguaglianza triangolare è la regola che rende un grafo "geometricamente sensato". Essa afferma che andare direttamente da $A$ a $B$ non deve mai costare più che passare attraverso un intermedio $C$:

$$c(u, w) \le c(u, v) + c(v, w)$$

Analizziamo i due casi:

**Caso A: Pesi $\{0, 1\}$ (La riduzione "Base")**

- Arco presente ($u,v$) e ($v,w$) $\to$ costo $0$.
- Arco mancante ($u,w$) $\to$ costo $1$.

- **Verifica:** $1 \le 0 + 0 \implies 1 \le 0$ (**FALSO!**)
    
- **Conclusione:** Questa riduzione genera un grafo che viola la geometria euclidea. Stiamo dimostrando la difficoltà del **TSP Generale**.

**Caso B: Pesi $\{1, 2\}$ (La riduzione "Metrica")**

- Arco presente ($u,v$) e ($v,w$) $\to$ costo $1$.
- Arco mancante ($u,w$) $\to$ costo $2$.
    
- **Verifica:** $2 \le 1 + 1 \implies 2 \le 2$ (**VERO!**)
    
- **Conclusione:** Questa riduzione genera un grafo che rispetta la geometria. Stiamo dimostrando la difficoltà del **Metric-TSP**.

#### **2. Perché questa distinzione è cruciale? (Il vero motivo teorico)**

La distinzione riguarda l'**approssimabilità**:

1. TSP Generale (Pesi 0/1):
    
    È un problema "cattivo". Non solo è NP-Hard, ma non è nemmeno approssimabile.
    
    Teorema: Se esistesse un algoritmo che approssima il TSP generale entro un fattore polinomiale, allora $P=NP$.
    
    Quindi, con pesi 0/1 dimostriamo che il caso peggiore assoluto è intrattabile.
    
2. Metric-TSP (Pesi 1/2):
    
    È un problema "più gentile". È NP-Hard (come dimostrato dalla riduzione con pesi 1/2), ma appartiene alla classe APX.
    
    Esistono algoritmi efficienti che garantiscono una soluzione vicina all'ottimo:
    
    - **2-Approximation:** Basato sull'Albero di Copertura Minimo (MST).
        
    - **Algoritmo di Christofides:** Garantisce un'approssimazione di fattore $1.5$ (o $3/2$).
