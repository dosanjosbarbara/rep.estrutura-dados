#conjunto 

conjunto_a = {1, 2, 3, 4, 5} #conjunto é uma coleção de elementos únicos, ou seja, não pode conter elementos repetidos. Além disso, os conjuntos são mutáveis, o que significa que podemos adicionar ou remover elementos após a criação do conjunto.
conjunto_b = {5, 7, 8, 9, 10}

#uniao de conjuntos
#uniao = conjunto_a.union(conjunto_b) #o método union() retorna um novo conjunto que contém todos os elementos de ambos os conjuntos, sem duplicatas. Se houver elementos repetidos entre os conjuntos, eles aparecerão apenas uma vez no conjunto resultante.
#uniao = conjunto_a | conjunto_b #outra forma de fazer a união de conjuntos
#print(uniao)

#interseccao (juntar os elementos que estão presentes em ambos os conjuntos)
#inter = conjunto_a.intersection(conjunto_b) #o método intersection() retorna um novo conjunto que contém apenas os elementos que estão presentes em ambos os conjuntos.
#inter1 = conjunto_a & conjunto_b #outra forma de fazer a interseccao de conjuntos
#print(inter)

#diferenca (juntar os elementos que estão presentes em um conjunto, mas não no outro)
dif = conjunto_a.difference(conjunto_b) #o método difference() retorna um novo conjunto que contém os elementos que estão presentes no conjunto_a, mas não no conjunto_b.
dif1 = conjunto_a - conjunto_b #outra forma de fazer a diferenca de conjuntos
#print(dif)

#diferenca simetrica (juntar os elementos que estão presentes em um conjunto ou no outro, mas não em ambos)
dif_sim = conjunto_a.symmetric_difference(conjunto_b) #o método symmetric_difference() retorna um novo conjunto que contém os elementos que estão presentes em um conjunto ou no outro, mas não em ambos.
dif_sim1 = conjunto_a ^ conjunto_b #outra forma de fazer a diferenca simetrica de conjuntos
print(dif_sim)  