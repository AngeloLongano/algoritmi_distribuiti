# Riassunto - Problemi e Algoritmi

## **Problema Computazionale**

Un **problema computazionale** Π è una questione generale che dipende da parametri i cui valori non sono specificati. Si definisce tramite:

- **INPUT**: insieme $ I $ di possibili assegnamenti ai parametri
- **OUTPUT**: insieme $ S $ di possibili soluzioni
- **Funzione**: $ Π : I → S $

Un'**istanza** del problema si ottiene assegnando valori specifici ai parametri.

***

## **Classificazione dei Problemi per Tipo di Soluzione**

I problemi si classificano in base al tipo di soluzione cercata:

1. **Problemi Decisionali**: la risposta è SI o NO (vero/falso) a seconda che l'input soddisfi o meno una certa proprietà
    - Esempi: test di primalità, test di connettività di un grafo

2. **Problemi di Ricerca**: si cerca una soluzione ammissibile che soddisfa una certa condizione
    - Esempi: ordinare una sequenza di numeri, determinare un albero di copertura per visita DFS

3. **Problemi di Ottimizzazione**: ogni soluzione ammissibile ha un costo associato e si cerca la soluzione ottima (costo minimo o massimo)
    - Esempio: determinare i cammini minimi da sorgente singola
    - Richiede una **funzione obiettivo**

***

## **Algoritmi**

Un **algoritmo** è una procedura generale per risolvere un problema definita tramite una sequenza di passi finita, ben ordinata, non ambigua, effettivamente realizzabile e che termina in tempo finito.

Un algoritmo per il problema Π è **corretto** se, per ogni istanza $$ i ∈ I $, produce la soluzione corrispondente $ Π(i) ∈ S $.

Se non è corretto, in corrispondenza di alcune (o tutte) le istanze:

- **Non termina**
- **Termina con una soluzione sbagliata**

***

## **Algoritmi Efficienti**

Siamo interessati a progettare **algoritmi efficienti** rispetto alle risorse di calcolo:

- **Tempo**: quanto dura l'esecuzione dell'algoritmo?
- **Spazio**: di quanta memoria ha bisogno l'esecuzione?

## **Misure di Efficienza**

**Tempo**:

- **NO**: misurare il tempo di esecuzione su una singola macchina
- **SI**: contare il numero di operazioni elementari necessarie nel caso peggiore (worst case), in funzione della dimensione dell'input

**Spazio**: numero di celle di memoria, in funzione della dimensione dell'input

***

## **Dimensione del Problema**

La dimensione misura la quantità di informazione necessaria per specificare l'istanza:

- **Criterio di costo logaritmico**: numero di bit necessari per rappresentare l'input
- **Criterio di costo uniforme**: numero di "elementi" necessari per rappresentare l'input

***

## **Costo e Complessità Computazionale**

- **Costo computazionale worst case** di un algoritmo: numero di operazioni elementari necessarie per risolvere il problema su qualunque istanza (anche la peggiore)

- **Complessità computazionale** di un problema: costo computazionale dell'algoritmo di minimo costo che risolve il problema

Un algoritmo **corretto** fornisce un **upper bound** alla complessità del problema. Un **lower bound** stabilisce il numero minimo di operazioni necessarie a ogni algoritmo per risolvere il problema nel caso peggiore.

***

## **Notazione Asintotica**

La notazione asintotica permette di esprimere limiti superiori e inferiori al costo computazionale e di rendere la misura indipendente dall'esecutore utilizzato.

## **O-grande (O)**

Date due funzioni $ f, g : ℕ → ℝ^+ $, diciamo che $$ f(n) ∈ O(g(n)) $$ se esistono $ c > 0 $ e $ n_0 ∈ ℕ $ tali che $$ f(n) ≤ c·g(n) $$ per ogni $ n ≥ n_0 $.

**Intuizione**: a partire da $ n_0 $, la funzione $ f(n) $ non sta mai sopra $ c·g(n) $.

**Interpretazione**: una funzione in alto è O-grande di qualsiasi funzione più in basso.

## **Omega (Ω)**

$$ f(n) ∈ Ω(g(n)) $$ se esistono $ c > 0 $ e $ n_0 ∈ ℕ $ tali che $$ f(n) ≥ c·g(n) $$ per ogni $ n ≥ n_0 $.

**Intuizione**: a partire da $ n_0 $, la funzione $ f(n) $ non sta mai sotto $ c·g(n) $.

**Interpretazione**: una funzione in basso è Omega di qualsiasi funzione più in alto.

## **Theta (Θ)**

$$ f(n) ∈ Θ(g(n)) $$ se esistono $ c_1, c_2 > 0 $ e $ n_0 ∈ ℕ $ tali che $$ c_1·g(n) ≤ f(n) ≤ c_2·g(n) $$ per ogni $ n ≥ n_0 $.

**Intuizione**: la funzione $ f(n) $ è limitata superiormente e inferiormente da multipli di $ g(n) $.

***

## **Classificazione dei Problemi per Difficoltà**

In base al costo computazionale, i problemi si classificano in:

1. **Problemi Trattabili (facili)**: esiste un algoritmo di costo computazionale **polinomiale** $$ T(n) ∈ O(n^k), k ≥ 0 $$
2. **Problemi Presumibilmente Intrattabili (difficili)**: non abbiamo un algoritmo di costo polinomiale, ma non è stato dimostrato che non esista
3. **Problemi Intrattabili**: si può dimostrare che non esiste un algoritmo di costo polinomiale
    - Esempio: Torre di Hanoi (richiede un numero esponenziale di mosse)
4. **Problemi Irrisolvibili**: si può dimostrare che non esiste alcun algoritmo risolutivo (indipendentemente dal costo)
    - Esempio: **Problema della fermata** (dato un algoritmo A con input D, l'esecuzione di A con input D termina in tempo finito?)

***

## **Perché il Polinomiale è la Soglia di Trattabilità?**

I problemi trattabili sono quelli di costo polinomiale perché:

- Esistono pochi problemi trattabili con algoritmi polinomiali di grado alto
- In molti problemi, lo spazio delle soluzioni è esponenziale: trovare un algoritmo polinomiale significa "fare meglio" di un algoritmo di forza bruta
- Le istanze worst case sono spesso rare o poco probabili
- Costi peggiori del polinomiale diventano rapidamente intrattabili al crescere della dimensione delle istanze
- È una misura indipendente dal progresso tecnologico

***

## **Tesi di Church-Turing**

Modelli di calcolo diversi, ma ragionevoli, si possono simulare a vicenda con uno **slowdown polinomiale**. Sono tutti polinomialmente equivalenti alla Macchina di Turing.

Le classi di problemi non cambiano cambiando modello di calcolo, purché quest'ultimo sia ragionevole.
