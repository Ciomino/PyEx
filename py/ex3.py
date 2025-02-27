def opSet(s1: set, s2: set):
    intS = s1 & s2
    uniS = s1 | s2

    return intS,uniS

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(opSet(set1,set2))