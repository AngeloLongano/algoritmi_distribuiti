# Riassunto - Teoria della Complessità

## **Introduzione**

La teoria della complessità classifica i problemi in base alla difficoltà di risolverli efficientemente. Si concentra sui **problemi decisionali** (output SI o NO), poiché la trattazione formale è più agevole e permette di trarre conclusioni applicabili anche ad altri tipi di problemi.

**Esempio**: Il problema **Shortest Path** può essere espresso sia come problema di ottimizzazione (qual è la lunghezza del cammino minimo?) che come problema decisionale (esiste un cammino di lunghezza $\leq k$?).

***

## **Classe P (Polynomial Time)**

**Definizione**: La classe **P** è l'insieme di problemi decisionali risolvibili con un algoritmo di costo computazionale **polinomiale** nella dimensione dell'input.

Trovare un algoritmo polinomiale per un problema è sufficiente per dimostrare l'appartenenza a P. Ma cosa succede se non si trova un algoritmo polinomiale né una dimostrazione che questo non esista?

***

## **Classe NP (Non-deterministic Polynomial Time)**

## **Esempio: Ciclo Hamiltoniano**

- **INPUT**: Grafo $G = (V, E)$
- **OUTPUT**: Esiste un ciclo in $G$ che passa per tutti i nodi esattamente una volta?

Per questo problema:

- Non si conoscono algoritmi polinomiali
- Un algoritmo forza bruta richiede tempo **fattoriale**
- Possiamo **verificare** una soluzione in tempo polinomiale: data una permutazione dei nodi, possiamo verificare in tempo lineare se rappresenta un ciclo hamiltoniano

## **Certificato e Algoritmo Verificatore**

**Certificato**: sequenza di caratteri di dimensione al massimo polinomiale che contiene l'evidenza che un'istanza $i$ sia positiva per il problema Π.

**Algoritmo verificatore**: algoritmo decisionale che prende in input un'istanza $i$ e un certificato $C_i$, restituendo SI se $i$ è positiva per Π, NO altrimenti.

**Osservazione**: Se la risposta è SI, allora $C_i$ è un certificato per l'istanza positiva $i$. Se la risposta è NO, o $i$ non è positiva oppure $C_i$ non è un certificato valido (ma potrebbe esisterne uno).

## **Definizione di NP**

**NP** è l'insieme di problemi decisionali che possono essere **verificati** con un algoritmo verificatore di costo polinomiale.

Un problema Π può essere verificato se:

1. Per ogni istanza positiva $i$ esiste un certificato $C_i$ di dimensione polinomiale
2. Esiste un algoritmo verificatore che risponde SI per ogni coppia $(i, C_i)$ dove $i$ è positiva e $C_i$ è un suo certificato

## **Relazione tra P e NP**

**Teorema**: $P \subseteq NP$

**Dimostrazione**: Ogni problema in P può essere verificato usando l'algoritmo risolutore come verificatore con certificato vuoto. Se l'algoritmo restituisce SI, l'istanza è positiva.

**Domanda aperta**: $NP \subseteq P$? Esistono problemi in NP che sembrano più difficili di quelli in P, candidati per essere in $NP \setminus P$.

***

## **Riduzione di Karp**

**Definizione**: Un problema decisionale $A$ è **riducibile in tempo polinomiale** a $B$ ($A \leq_p B$) se:

- Ogni istanza di $A$ può essere trasformata in tempo polinomiale in un'istanza di $B$
- Ogni istanza positiva di $A$ viene trasformata in un'istanza positiva di $B$
- Ogni istanza negativa di $A$ viene trasformata in un'istanza negativa di $B$

**Intuizione**: $A \leq_p B$ significa che:

- Il problema $B$ non è più facile di $A$ (un algoritmo per $B$ può risolvere $A$)
- Il problema $A$ non è più difficile di $B$

## **Conseguenze**

Se $A \leq_p B$ allora:

- $B \in P \Rightarrow A \in P$ (abbiamo un algoritmo polinomiale per $A$)
- $A \notin P \Rightarrow B \notin P$ (se $B \in P$ avremmo un algoritmo polinomiale per $A$, assurdo)
- $B \leq_p A \Rightarrow A \equiv B$ (i problemi sono equivalentemente difficili)

**Proprietà**: La riduzione polinomiale è **transitiva**: $A \leq_p B \land B \leq_p C \Rightarrow A \leq_p C$.

***

## **Classe NP-Completo**

**Definizione**: Un problema decisionale $A$ è **NP-completo** se:

1. $A \in NP$
2. $\forall B \in NP : B \leq_p A$

## **Come Dimostrare che un Problema è NP-Completo**

Per dimostrare che $A$ è NP-completo, sfruttiamo la transitività della riduzione:

1. Dimostrare che $A \in NP$
2. Scegliere un problema $B$ già dimostrato NP-completo
3. Dimostrare che $B \leq_p A$

**Teorema di Cook-Levin** (1971-1973): Il primo problema dimostrato NP-completo è **SAT** (Satisfiability).

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

***

## **Esempio: TSP (Travelling Salesman Problem)**

**INPUT**: Grafo completo con archi pesati
**OUTPUT**: Ciclo hamiltoniano di costo minimo

**Teorema**: Il TSP è NP-hard

**Dimostrazione**: Riduciamo il problema del Ciclo Hamiltoniano (NP-completo) al TSP:

1. Dato un grafo $G = (V, E)$, creiamo $G' = (V, E')$ completo con pesi:
   - $c(e) = 0$ se $e \in E$
   - $c(e) = 1$ altrimenti
2. Se il ciclo hamiltoniano di costo minimo in $G'$ ha costo 0, allora $G$ ha un ciclo hamiltoniano
3. Se ha costo $> 0$, allora $G$ non ha ciclo hamiltoniano

***

## **Soluzioni per Problemi NP-Hard**

Molti problemi NP-hard hanno importanti applicazioni e non possono essere ignorati. Possibili soluzioni:

- Risolvere efficientemente solo istanze piccole
- Utilizzare euristiche
- Utilizzare algoritmi paralleli/distribuiti
- Utilizzare **algoritmi di approssimazione**: restituiscono in tempo polinomiale una soluzione ammissibile con garanzie sul discostamento dal costo ottimo
