l=[x**2 for x in range(1,10)]
print(l)

lPari = [x for x in l if x%2==0]
print(lPari)

lTesto = ["adsaefa","fahcue","d","dashgciuagi"]
lLunghezzaP = [len(x) for x in lTesto]

print(lLunghezzaP)

lMaiuscolo = [x.upper() for x in lTesto]

print(lMaiuscolo)