#  Metodi Numerici per Intelligenza Artificiale
## Informazioni sul corso
> Anno: 2025/2026

> Docenti: Damiana Lazzaro, Lorenzo Pellegrini

### Sito del corso
https://www.unibo.it/it/studiare/insegnamenti-competenze-trasversali-moocs/insegnamenti/insegnamento/2025/493349

## Documentazione Numpy

### Informazioni preliminari
- Con `np` si intende `numpy`, si presume quindi il pacchetto sia importato come `import numpy as np`; 
- Con `arr` si intende una variabile qualsiasi di tipo `np.array` (quindi un array di Numpy).

| Comando | Cosa fa |
| -- | ----------- |
| `np.random.randn(*size)` | Genera una matrice con `size` dimensioni con valori distribuiti sulla normale standard (Gaussiana) |
| `np.random.randint(min, max, size)` | Matrice con `size` dimensioni con numeri interi tra min (incluso) e max (escluso) | 
| `np.linspace(start, stop, quantity)` | Array con `quantity` valori con numeri equidistanti | 
| `np.arange(start, stop, step)` | Equivalente di "range()" in python, solo che restituisce un `np.array` |
| `arr.reshape(size)` | Cambia le dimensioni di un array in `size` | 