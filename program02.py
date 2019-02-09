'''
Abbiamo n pulsanti numerati da 1 a N ed N lampadine anch'esse numerate da 1 a N.
Il generico pulsante x cambia lo stato (da accesa a spenta o viceversa) della lampadina x
e di tutte le lampadine il cui numero identificativo e' un divisore di x.
Ad esempio il pulsante 18 cambia lo stato delle lampadine 1,2,3,6,9,18.
Ogni pulsante puo' essere premuto al massimo una volta e i pulsanti vanno premuti
in ordine crescente (una volta premuto il pulsante x  non e' piu' possibile premere
i pulsanti da 1 a x-1).
Sapendo N e l'insieme 'accese' delle lampadine al momento accese
bisogna individuare la sequenza crescente di bottoni da premere perche'
tutte le lampadine risultino accese.
Definire una funzione es2(N, accese) che dati:
- il numero N di lampadine
- l'insieme 'accese' contenente gli identificativi delle lampadine al momento accese
determina e restituisce la lista contenente nell'ordine i pulsanti da premere perche'
le N lampadine risultino tutte accese.
Ad esempio per N=6 e accese={2,4} es2(N, accese) restituisce la lista [2,5,6] infatti:
-all'inizio sono accese le lampadine {2,4}
-dopo aver premuto il pulsante 2 saranno accese le lampadine {1,4}
-dopo aver premuto il pulsante 5 saranno accese le lampadine {4,5}
-dopo aver premuto il pulsante 6 saranno accese le lampadine {1,2,3,4,5,6}

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''
def es2(N, ins):

    buttons = []
    light_on = list(ins.copy())

    #tutte le luci accese
    if len(ins) == N:
        return buttons
    
    start_index = N
    #se solo una lampadina è spenta
    if N - len(ins) == 1:
        for i in range (1,N):
            if not i in light_on: 
                start_index = i
                break

    #per ogni lampadina e i suoi divisori controllo se sono accesi:
    for lampadina_index in range(start_index,0,-1):
        
        if not lampadina_index in light_on:
            buttons.append(lampadina_index)
            #controlla se i divisori sono accesi o spenti e agisci di conseguenza
            for i in range(1, lampadina_index):
                if lampadina_index % i == 0:
                    #se è acceso spegni e viceversa
                    if i in light_on:
                        light_on.remove(i)
                    else:
                        light_on.append(i)

    buttons.sort()
    return buttons
