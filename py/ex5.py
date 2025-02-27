def filtaMaggiorenni(l: list):
    filtro = []
    for d in l:
        if d.get("età")>=18:
            filtro.append(d)
    return filtro

persone = [
    {"nome": "Alice", "età": 25},
    {"nome": "Bob", "età": 17},
    {"nome": "Charlie", "età": 30}
]
print(filtaMaggiorenni(persone))