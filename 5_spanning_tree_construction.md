## Spanning Tree
![[Pasted image 20260210185302.png|300]]
Uno **spanning tree** (in italiano: _albero di copertura_) di un grafo connesso $G=(V,E)$ è un **sottografo** $T=(V,E’)$ tale che:

1. contiene **tutti** i vertici di $G$ (quindi “spanning” = _che copre/spazia_ su tutti i nodi):
    
    $$V(T)=V(G)$$
    
2. usa solo alcuni archi del grafo originale:
    
    $$E’ \subseteq E$$ 
    
3. è un **albero**, cioè è **connesso e aciclico** (non contiene cicli).
    

  

### **Proprietà super importante (da sapere a memoria)**

  

Se $G$ è connesso e ha $n=|V|$ nodi, allora **ogni spanning tree ha esattamente $n-1$ archi**. (È la proprietà classica degli alberi; nel testo CLRS viene richiamata quando parla di spanning tree come sottoinsieme aciclico che connette tutti i vertici.) 

  

### **Perché è utile nei distribuiti**

  

Nei protocolli distribuiti spesso si costruisce prima uno spanning tree e poi si eseguono broadcast/traversal **solo sull’albero** per ridurre i messaggi: sull’albero, ad esempio, il broadcast costa esattamente $n-1$ messaggi. 

  

### **Cosa “sanno” i nodi a fine costruzione (nel corso)**

  

Nel problema **SPT** (spanning tree construction) in ambiente distribuito, alla fine non è richiesto che un nodo conosca tutto $T$: ogni nodo $x$ deve selezionare localmente un insieme Tree-neighbors(x) ⊆ N(x) che rappresenta **quali vicini sono collegati a lui nell’albero**.

# Spanning Tree Construction (SPT) 

### Problema e output “locale”
Dato un grafo connesso $G=(V,E)$, vogliamo costruire uno **spanning tree** $T=(V,E')$ con $E'\subseteq E$ e $T$ aciclico e connesso. Nella versione distribuita, **alla fine ogni nodo non conosce tutto l’albero**, ma solo quali tra i suoi vicini sono collegati a lui tramite un arco di $T$ (variabile tipo `Tree-neighbours(x)`).  [oai_citation:0‡2_distributed algorithms.pdf](sediment://file_000000000e00720aba4a92c7d9b8209f)

Assunzioni tipiche nelle slide (ambiente ristretto):
- **Single initiator**, link bidirezionali, affidabilità totale, grafo connesso.  [oai_citation:1‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

---

### Idea 1: costruire lo spanning tree “da broadcast”
C’è un fatto generale molto utile: **l’esecuzione di un qualunque protocollo di broadcast** (con unico iniziatore) **induce uno spanning tree**: per ogni nodo $x\neq s$, definisci `parent(x)` come il vicino da cui $x$ riceve l’informazione **per la prima volta**; la relazione “parent” definisce un albero radicato nell’iniziatore.  [oai_citation:2‡DESIGN AND ANALYSIS.pdf](sediment://file_000000009810720aa5644501ee86e744)

Ma attenzione: sapere solo `parent(x)` **non basta** per risolvere SPT come definito nel corso/libro, perché ogni nodo deve anche determinare **chi sono i figli** e quali vicini **non** sono tree-neighbors; questo richiede ulteriore “feedback” (es. messaggi YES/NO).  [oai_citation:3‡DESIGN AND ANALYSIS.pdf](sediment://file_000000009810720aa5644501ee86e744)

---

### Protocollo SHOUT (costruzione per “richieste Q” + risposte YES/NO)
**Intuizione:** l’iniziatore chiede ai vicini di diventare suoi vicini nell’albero; ogni nodo dice **YES** solo alla **prima** richiesta che riceve (scegliendo così il proprio parent) e risponde **NO** alle richieste successive.  [oai_citation:4‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

**Stati (slide):**
$$S=\{\text{INITIATOR},\text{IDLE},\text{ACTIVE},\text{DONE}\},\quad S_{term}=\{\text{DONE}\}$$  [oai_citation:5‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

**Variabili tipiche:**
- `parent`, `root`, `Tree-neighbours(x)` (insieme dei vicini in $T$), `counter` (conta le risposte ricevute dai vicini).  [oai_citation:6‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

**Correttezza (idea chiave):**
- Ogni nodo (tranne l’iniziatore) manda **esattamente un YES** ⇒ ogni nodo sceglie un solo parent.
- La relazione costruita da `Tree-neighbours` definisce un **albero connesso** che contiene tutti i nodi (terminazione locale).  [oai_citation:7‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

**Message complexity (peggiore):**
- Dalle slide si ricava che nel worst-case:
$$M(\text{SHOUT}) = 4m - 2n + 2 = 2\cdot(2m-n+1).$$  [oai_citation:8‡2_distributed algorithms.pdf](sediment://file_000000000e00720aba4a92c7d9b8209f)

> Nel riassunto grande puoi mettere solo: “SHOUT = flooding + YES/NO per far conoscere ai nodi anche figli/non-figli; $M=4m-2n+2$”.  [oai_citation:9‡2_distributed algorithms.pdf](sediment://file_000000000e00720aba4a92c7d9b8209f)

---

### Protocollo SHOUT+ (ottimizzazione: senza NO)
Nelle slide compare una variante **senza NO**: quando un nodo ACTIVE riceve una richiesta $Q$, la interpreta implicitamente come “NO” (incrementa `counter` e basta). In questo modo:
- su ogni link transitano esattamente **due messaggi** (o $Q$–YES oppure $Q$–$Q$), quindi:
$$M(\text{SHOUT}^+) = 2m.$$  [oai_citation:10‡2_distributed algorithms.pdf](sediment://file_000000000e00720aba4a92c7d9b8209f)

---

### Spanning Tree Construction by Traversal (Depth-First Traversal)
Un’altra famiglia di soluzioni costruisce lo spanning tree tramite una **visita DFS distribuita** usando un **token** (Forward/Return/Back-edge).
- Quando un nodo riceve il **ForwardToken** per la prima volta, memorizza chi lo ha inviato (quello è il `parent`) e prova a inoltrare il token a un vicino non visitato; se un nodo riceve di nuovo il ForwardToken su un arco, risponde con **Back-edge token** (quell’arco non è nell’albero). 
- Eliminando i back-edge si ottiene lo spanning tree; `parent(x)` è chi ha inviato per primo il token, e i figli sono i vicini che non risultano back-edge.  [oai_citation:11‡2_distributed algorithms.pdf](sediment://file_000000006d5471f4bb6d83bdba1930e2)

(Questa parte è utile per capire che esistono costruzioni SPT anche “per traversal”, ma in genere SHOUT/SHOUT+ sono più puliti come costruzione locale dei `Tree-neighbours`.)

---

### Importante: cosa succede con più iniziatori?
Se togli l’assunzione “single initiator”, i protocolli progettati per unico iniziatore **possono fallire**: ad esempio SHOUT con due initiator può costruire una **foresta** (non connessa). 

Risultato teorico (libro): **SPT è deterministically unsolvable sotto le sole restrizioni standard $R$** (cioè senza imporre un unico iniziatore o assunzioni extra).  [oai_citation:12‡DESIGN AND ANALYSIS.pdf](sediment://file_000000009810720aa5644501ee86e744)