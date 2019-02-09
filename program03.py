'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''
def es3(lista,testo):
  
    dictionary_counter = {}
    dicitonary_index   = {}
    word_to_remove     = []

    current_test = testo
    sorted_list = sorted(lista, key=len, reverse=True)
    for word in sorted_list:
        if word in current_test and len(word):
        # aggiungo la parola tenendo traccia di quante volte è presente e a che punto della stringa testo si trova
          replace_time = current_test.count(word)
          dictionary_counter.setdefault(word,replace_time)
          dicitonary_index.setdefault(current_test.index(word),word)
          word_to_remove.append(word)
          substitute = len(word) * "*"
          current_test = current_test.replace(word, substitute,replace_time)
    
    for word in word_to_remove:
        if word in lista:
          lista.remove(word)

    #ordino la lista in base all index nel testo per avere il giusto ordinamento
    list_to_return = []
    while len(dicitonary_index) > 0:
        min_value = min(dicitonary_index.keys())
        word_to_append = dicitonary_index.pop(min_value)
        list_to_return.append(word_to_append)

    values         = dictionary_counter.values()
    max_value      = max(values)
    list_to_check  = sorted(dictionary_counter.keys())
    
    for word in list_to_check:
        if dictionary_counter.get(word) == max_value:
          tuple_to_ret = (list_to_return,word)
          return tuple_to_ret
