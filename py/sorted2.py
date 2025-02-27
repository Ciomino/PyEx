parole = ["casa", "elefante", "sole", "bicicletta", "albero"]
# Risultato atteso: ['sole', 'casa', 'albero', 'elefante', 'bicicletta']
print(sorted(parole, key=lambda x: len(x)))

numeri = [-10, 5, -3, 7, -8, 2]
# Risultato atteso: [2, -3, 5, -8, 7, -10]
print(sorted(numeri, key= lambda x: abs(x)))

date = ["12/05/2023", "25/12/2021", "01/01/2022", "15/08/2020"]
# Risultato atteso: ["15/08/2020", "25/12/2021", "01/01/2022", "12/05/2023"]
print(sorted(date, key=lambda x: (x.split("/")[2],x.split("/")[1],x.split("/")[0])))

studenti = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("David", 75)]
# Risultato atteso: [('Bob', 92), ('Alice', 85), ('Charlie', 85), ('David', 75)]
print(sorted(studenti, key=lambda x: (-x[1], x[0])))


#Dati una lista di prodotti con nome e prezzo, ordina prima per prezzo crescente e, in caso di prezzi uguali, in ordine alfabetico per nome.
prodotti = [
    {"nome": "Mela", "prezzo": 1.5},
    {"nome": "Banana", "prezzo": 1.2},
    {"nome": "Arancia", "prezzo": 1.5},
    {"nome": "Kiwi", "prezzo": 2.0}
]

print(sorted(prodotti, key=lambda x: (x.get("prezzo"),x.get("nome"))))
# Risultato atteso:
# [
#     {'nome': 'Banana', 'prezzo': 1.2},
#     {'nome': 'Arancia', 'prezzo': 1.5},
#     {'nome': 'Mela', 'prezzo': 1.5},
#     {'nome': 'Kiwi', 'prezzo': 2.0}
# ]