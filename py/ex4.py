def countList(l: list):
    d = {}
    for x in l:
        i = l.count(x)
        if d.get(x)!=x:
            d[x]=i
    return d

lista = ["mela", "banana", "mela", "arancia", "banana", "banana"]
print (countList(lista))

#funzione ottimizzata
def count_list(l: list):
    d = {}
    for x in l:
        if x in d:
            d[x] += 1  # Se già presente, incrementa il conteggio
        else:
            d[x] = 1  # Se non presente, inizializza a 1
    return d

lista = ["mela", "banana", "mela", "arancia", "banana", "banana"]
print(count_list(lista))