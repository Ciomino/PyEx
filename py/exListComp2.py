words = ["apple", "banana", "cat", "dog", "elephant"]
lFiltroW = [x for x in words if len(x)>4]
print(lFiltroW)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lDispariN = [x for x in numbers if x%2==1]
print (lDispariN)

lCoppieQ = [[x,x**2] for x in range(1,6)]
print(lCoppieQ)

numbers1 = [1, 2, 3, 4, 5, 6, 10, 15, 20, 30]
lDiv3_5 = [x for x in numbers1 if x%3==0 and x%5==0]
print(lDiv3_5)
# Risultato atteso: [15, 30]

words1 = ["apple", "banana", "orange", "umbrella", "cat"]
v = ["a","e","i","o","u"]
lConsonante = [x for x in words1 if x[0].lower() not in v]
print(lConsonante)
# Risultato atteso: ['banana', 'cat']