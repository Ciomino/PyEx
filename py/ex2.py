def formatta_lista(l: list):
    s = set(l)
    lModificata = list(s)
    return sorted(lModificata)

test=[1,1,2,2,5,3,6,5]
print(formatta_lista(test))