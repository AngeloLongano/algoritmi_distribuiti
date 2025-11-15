# Classificazione problemi

La classificazione dei problemi P, NP, NP-completi e NP-hard riguarda la difficoltà nel risolvere problemi decisionali, cioè quelli che hanno risposta “sì” o “no”.

## Classe P

- Problemi che possono essere risolti da un algoritmo in tempo polinomiale rispetto alla dimensione dell’input.
- Risoluzione pratica ed efficiente anche per input molto grandi.
- Esempi: ordinamento di una lista, ricerca del cammino minimo in un grafo.

## Classe NP

- Problemi per cui una soluzione candidata (certificato) può essere verificata in tempo polinomiale, anche se trovare la soluzione potrebbe essere difficile.
- Non è detto che si riesca a risolvere facilmente, ma se qualcuno ti dà la risposta puoi verificarla velocemente.
- Esempi: ciclo hamiltoniano, si può controllare in tempo polinomiale se una sequenza di nodi forma davvero un ciclo hamiltoniano.

## Classe NP-completo

- Problemi tra i più “duri” di NP.
- Sono in NP, e inoltre qualunque altro problema NP può essere ridotto polinomialmente ad uno di questi (usando le riduzioni di Karp).
- Se si trova un algoritmo polinomiale per uno di questi, allora ogni problema di NP diventa polinomiale (quindi P = NP).
- Esempio: SAT [soddisfacibilità di una formula booleana](1).

## Classe NP-hard

- Problemi almeno complessi quanto ogni NP-completo, ma non necessariamente verificabili in tempo polinomiale (non sempre appartengono a NP).
- Spesso sono problemi di ottimizzazione, per cui la verifica della soluzione non è efficiente.
- Esempio: TSP [Problema del commesso viaggiatore, versione di minimizzazione della distanza](1).

## Tabella riassuntiva

| Classe      | Risolvibile velocemente | Verificabile velocemente | Riceve riduzioni da tutti i NP | Esempio           |
|-------------|:----------------------:|:------------------------:|:-----------------------------:|:------------------|
| P           | Sì                     | Sì                       | No                            | Ordinamento, cammino minimo |
| NP          | Non sempre             | Sì                       | No                            | Ciclo hamiltoniano         |
| NP-completo | Non sempre             | Sì                       | Sì                            | SAT                      |
| NP-hard     | Non sempre             | Non sempre               | Sì                            | TSP [ottimizzazione](1)      |

***
In sintesi:

- P = facili da risolvere.
- NP = facili da verificare, non sempre da risolvere.
- NP-completo = difficili da risolvere e massimamente rappresentativi dell’intera classe NP.
- NP-hard = almeno difficili quanto gli NP-completi, spesso ancor più ostici da gestire.
