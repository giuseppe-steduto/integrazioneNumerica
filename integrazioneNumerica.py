"""
    *** Copyright Giuseppe Steduto - 2020***
    Programma per l'integrazione numerica di funzioni usando i metodi
    - Dei rettangoli
    - Dei trapezi
    - Delle parabole

    Librerie: numpy
"""

import numpy as np
import math

def F(x, funzioneInserita):
    """Restituisce una funzione scritta in notazione numpy
    Args:
        x: variabile in cui calcolare la funzione (non è importante il valore)
        funzioneInserita (str): L'inserimento testuale dell'utente, la funzione in x
    Returns:
        function: funzione su cui calcolare l'integrale
    """
    return eval("lambda x:" + funzioneInserita)

def metodoRettangoli(f, a, b, n):
    """Restituisce l'integrale definito di una funzione ottenuto con il metodo di integrazione numerica dei rettangoli
    Args:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    Returns:
        str: la stringa "errore", quando qualcosa è andato storto
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            somma += f(i)
        except Error as errore:
            return "errore"

    somma += f(b)
    somma *= (b-a)/n
    return np.around(somma, 5)

def metodoTrapezi(f, a, b, n):
    """Restituisce l'integrale definito di una funzione ottenuto con il metodo di integrazione numerica dei trapezi
    Args:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    Returns:
        str: la stringa "errore", quando qualcosa è andato storto
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            somma += 2*f(i)
        except:
            return "errore"
    somma += f(b)
    somma -= f(a) #Viene contata 2 volte, ma deve essere contata una sola
    somma *= (b-a)/(2*n)
    return np.around(somma, 5)

def metodoParabole(f, a, b, n):
    """Restituisce l'integrale definito di una funzione ottenuto con il metodo di integrazione numerica delle parabole
    Args:
        f: la funzione su cui calcolare l'integrale
        a: estremo inferiore
        b: estremo superiore
        n: numero di intervalli
    Returns:
        str: la stringa "errore", quando qualcosa è andato storto
        float: il risultato dell'integrazione numerica
    """
    somma = 0
    contatore = 0
    for i in np.arange(a, b, (b-a)/n):
        try:
            if contatore % 2 == 0:
                somma += 2*f(i)
            else:
                somma += 4*f(i)
            contatore += 1
        except:
            return "errore"
    somma += f(b)
    somma -= f(a) #Viene contata 2 volte, ma deve essere contata una sola
    somma *= (b-a)/(3*n)
    return np.around(somma, 5)


#MAIN
#output delle istruzioni
print("""Author: Giuseppe Steduto.\n\nBenvenuto in questo calcolatore!
Offre i tre principali metodi di integrazione numerica su un intervallo scelto.
\nISTRUZIONI:
- Inserire una funzione in x
- Usare la notazione delle funzioni e delle costanti di numpy, con il prefisso 'np.' Esempi:
    + Per il valore di pi greco, scrivere 'np.pi'
    + Per il seno di x, scrivere 'np.sin(x)'
    + Per la potenza n-esima di x, scrivere 'np.pow(x, n)
    + Per la radice quadrata, scrivere 'np.sqrt(x)'
    + Per la documentazione completa su numpy: https://www.geeksforgeeks.org/numpy-mathematical-function/
- Rispettare le parentesi!
- Inserire numeri come estremi di integrazione. È possibile usare le costanti di numpy come descritto sopra
""")
x = 0
funzioneInserita = input("Inserisci una funzione in x (notazione numpy): ")
f = F(x, funzioneInserita)
a = float(eval(input("Inserisci l'estremo inferiore (a): ")))
b = float(eval(input("Inserisci l'estremo superiore (b): ")))
n = np.round((b-a)*10)
if not n % 2 == 0: #n deve essere pari
    n += 1
if b <= a:
    print("Gli estremi sono stati inseriti nell'ordine sbagliato. Li scambio.")
    a, b = b, a #Scambia le variabili
print("Calcolo l'integrle definito di", funzioneInserita, "tra", a, "e", b, "dividendo in", n, "intervalli.")

print("Metodo dei rettangoli. ",end = " ")
rettangoli = metodoRettangoli(f, a, b, n)
if rettangoli == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", rettangoli)

print("Metodo dei trapezi. ",end = " ")
trapezi = metodoTrapezi(f, a, b, n)
if trapezi == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", trapezi)

print("Metodo delle parabole. ",end = " ")
parabole = metodoParabole(f, a, b, n)
if parabole == "errore":
    print("\nErrore nel calcolo! Forse la funzione non è continua nell'intervallo, controlla bene.")
else:
    print("Risultato:", parabole)

terminatore = input("\n\nPremi un tasto per terminare.")
