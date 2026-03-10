#  Metodi Numerici per Intelligenza Artificiale
## Informazioni sul corso
> Anno: 2025/2026

> Docenti: Damiana Lazzaro, Lorenzo Pellegrini

### Sito del corso
https://www.unibo.it/it/studiare/insegnamenti-competenze-trasversali-moocs/insegnamenti/insegnamento/2025/493349

## Documentazione Numpy

### Informazioni preliminari
- Con `np` si intende `numpy`, si presume quindi che il pacchetto sia importato come `import numpy as np`; 
- Con `arr` si intende una variabile qualsiasi di tipo `np.ndarray` (quindi un array di Numpy);
- Con `size` si intende un'espressione Size-Like, ovvero una tupla di tipo `(n, m, ...)`.

### Numpy sheet

| Comando | Cosa fa |
| -- | ----------- |
| `np.random.randn(*size)` | Genera una matrice con `size` dimensioni con valori distribuiti sulla normale standard (Gaussiana) |
| `np.random.randint(min, max, size)` | Matrice con `size` dimensioni con numeri interi tra min (incluso) e max (escluso) | 
| `np.linspace(start, stop, quantity)` | Array con `quantity` valori con numeri equidistanti da start (incluso) a stop (incluso) | 
| `np.arange(start, stop, step)` | Equivalente di "range()" in python, solo che restituisce un `np.array`. start incluso, stop escluso |
| `np.concat(tuple[np.ndarray], axis)` | Concatena gli array sull'`axis`. Se `axis` non è definito, allora gli array saranno appiattiti (vedi `arr.flatten()`) |  
| `np.vstack(tuple[np.ndarray])` | Concatena gli array contenuti in `tuple` considerando ognuno come una nuova riga | 
| `np.hstack(tuple[np.ndarray])` | Uguale a `np.vstack(...)` | 
| `np.diag(arr, k)` | Se `arr` è un array ad una dimensione, restituisce una matrice che ha come `k`-esima diagonale l'array specificato. Nel caso in cui `k != 0` bisogna considerare che la matrice risultante avrà come size `(len(arr) + abs(k), len(arr) + abs(k))` |
| `np.eye(righe, colonne=righe, k=0, dtype=float)` | Crea una matrice di grandezza `righe` x `colonne` la cui diagonale `k` ha tutti 1. Il tipo di default è float |
| `arr.reshape(size)` | Cambia le dimensioni di un array in `size`. Utilizzando `-1` come size per un asse, questo sarà calcolato automaticamente. | 
| `arr.base` | Restituisce l'array originale se `arr` è una View, `None` se l'array è l'originale (o una copia, ma non una View di un altro array) |
| `arr.ravel()` | Crea una view di `arr` a 1 dimensione |
| `arr.flatten()` | Crea una copia di `arr` a 1 dimensione |
| `arr[{start, stop, step},{start,stop,step},{...}]` | Gli `ndarray` hanno la possibilità di effettuare lo slicing per ogni dimensione (Il risultato sarà una **copia**) |
 
### Numpy operations
> Queste operazioni sono ottimizzate da Numpy in C, per cui conviene sempre usare questi piuttosto che i cicli di Python (nettamente più lenti).

Siano `A` e `B` due `np.ndarray`

| Operazione | Cosa fa |
| ---------- | ------- |
| `A + B` | Somma ogni elemento di A e B uno per uno (vedi `np.sum()`) |
| `A - B` | Fa la differenza di ogni elemento di A e B uno per uno (vedi `np.subtract()`) |
| `A * B` | Moltiplica ogni elemento di A e B uno per uno (vedi `np.multiply()`|
| `A / B` | Divide ogni elemento di A e B uno per uno (vedi `np.divide()`) |
| `A // B` | Divide e arrotonda per difesso ogni elemento di A e B uno per uno (vedi `np.floor_divide()`) | 
| `A ** B` | Eleva ogni elemento di A agli elementi di B uno per uno (vedi `np.power()`)
| `A @ B` | Moltiplicazione tra le matrici (vedi `np.matmul()`) |
| `A > B` | Vale anche per altre condizioni booleane, crea una maschera booleana (`np.ndarray` di bool)|