parole = ["gatto", "cane", "elefante", "topo"]
print(sorted(parole , key=None, reverse=True))

tuples = [(1, 3), (4, 2), (2, 5), (3, 1)]
print(sorted(tuples, key=lambda x: x[1]))

persone = [
    {"nome": "Alice", "età": 25},
    {"nome": "Bob", "età": 17},
    {"nome": "Charlie", "età": 30}
]
print(sorted(persone, key=lambda x : x.get("età")))