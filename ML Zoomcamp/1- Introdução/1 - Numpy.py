
# Numpy é uma biblioteca é principalmente usada para trabalhar com numeros, matrizes e arrays e grandes dados numéricos conceitos usados em ML.
import numpy as np

#criação de arrays usando numpy
print(np.zeros(3))
#com zeros
print(np.ones(3))
#com uns
print(np.full(3,4))
# Nesse exemplo o primeiro espaço é usado para definir o tamanho da array, e o segundo espaço o numero que estara preenchendo.
#É possivel transformar uma lista numerica em um array de Numpy.
array_teste = np.array([1,5,8,9,7,61,54])
# Tambem possui indexação nesses arrays
print(array_teste[3],array_teste[0])
# Criação de arrays usando ranges indexação começa sempre em 0 então é ultimo numero -1, com regras parecidas com range com primeiro espaço sendo o de começo e o segundo o tanto até onde vai e o terceiro 'step' como usado com pular mas não é possivel usar -1 como reverse .arange(start,stop,step,dtype) e a formatação dos dados podendo ser inteiro ou float.
print(np.arange(1,11,2))
# Criação de arrays usando .linspace com o primeiro numero sendo sobre o começo, o segundo o ultimo e o terceiro a quantidade de numeros entre 1 e outro.
print(np.linspace(1,100,7))
# Criação de Arrays Multidimensionais bem ao usarmos duas chaves ((A, B)) o A sendo Rows a 'distancia' vertical, e B sendo as colunas 'distancia' horizonal.
print(np.zeros((5, 3)))

# Para criar manualmente essa arrays multidimensionais pensamos como uma lista dentro de uma lista sendo as listas de dentro separadas
# por colchetes envolta da lista maior com colchetes.
Arr_Multi= np.array([[0,1,2],
                     [3,4,5],
                     [6,7,8]])
print(Arr_Multi)
# A indexação desses arrays multidimensionais passa a ser por 2 caracteres, o primeiro pela Row e segundo pela coluna.
print(Arr_Multi[0, 2], Arr_Multi[1, 1], Arr_Multi[2, 2])
# É possivel fazer alteração de uma variavel usando essa indexação
Arr_Multi[1, 2] = 10
# Essa indexação de listas dentro de listas pode ser usada tambem quando queremos modificar uma row ou coluna inteira.
# Sendo EXEMPLO[Rows: Colunas] Especificando apenas 1 das 'distancias'
Arr_Multi[0] = [1,5,9]
# Asimilando todas as variaveis na Rows da indexação 0 a primeira recebe = a lista com novas variaveis.
print(Arr_Multi)

Arr_Multi[:, 1] = [2,3,4]
# Todas as variaveis da coluna 1 , a segunda, recebe as novas variaveis.
print(Arr_Multi)

# Operações de comparação.
# print(array_teste >= 9)

array_teste2 = np.array([1,2,37,8,9,8,5])
# ARRAYS TEM QUE TER O MESMO TAMANHO.
print(array_teste > array_teste2)

print(array_teste2[array_teste2 > array_teste])
# é mostrado 37 porque na sua posição ele é maior comparado a 8, é mostrado 9 porque na sua posição é maior comparado ao 7.

# .min() Mostra o menor valor do array.
# .max() Mostra o maior valor do array.
# .sum() Mostra a soma dos valores dentro da array.
# .mean() Mostra a média de valores da array.
# Também funcionam em arrays de duas dimensões.

# .std()
# Standard Deviation , Desvio padrão é uma medida que mostra o quao distante os valores estão da média aritmética.
medida_sem_variação = np.array([0,2,3,4,5,6,7,8,10])
print(medida_sem_variação.std())
std_teste = np.array([0,20,50,100,1000])
print(std_teste.std())

# Imagino que essa variação vai ser mais falada posteriormente.
# Quanto maior o numero do desvio padrão mais a média está diferente de uma 'média' realmente mediana.