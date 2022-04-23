# l=[3,1,2,2,4]
# from collections import Counter
 
# def dice_freqs(throws):
#     position = Counter(throws).most_common(6)
#     print(position)
#     v,p=zip(*position) # unpacking 
#     # print(p)
#     aux = [(dict(list(zip(throws,p))) [key], key) for key in dict(list(zip(throws,p))) ]
#     # print(aux)
#     aux.sort()
#     from itertools import repeat, chain
#     b,a=zip(*aux) # unpacking 
#     listaF=list(chain.from_iterable(repeat(value, count) for value, count in zip(a, b)))
#     return listaF
    
# lista= dice_freqs(l)

# for n in lista:
#     print(n)

items=[3,1,2,2,4]

frecuencia = [items.count(p) for p in items]
aux = [(dict(list(zip(items,frecuencia))) [key], key) for key in dict(list(zip(items,frecuencia))) ]
aux.sort()

from itertools import repeat, chain
b,a=zip(*aux) # unpacking 
listaF=list(chain.from_iterable(repeat(value, count) for value, count in zip(a, b)))

for n in listaF:
    print(n)

######################################
# items=[3,1,2,2,4]

# def listaDicFrec(lista):
#     frecuencia = [lista.count(p) for p in lista]
#     print(frecuencia)
#     aux = [(dict(list(zip(lista,frecuencia))) [key], key) for key in dict(list(zip(lista,frecuencia))) ]
#     aux.sort()
#     return aux
    
# lista= listaDicFrec(items)

# from itertools import repeat, chain
# b,a=zip(*lista) # unpacking 
# listaF=list(chain.from_iterable(repeat(value, count) for value, count in zip(a, b)))

# for n in listaF:
#     print(n)