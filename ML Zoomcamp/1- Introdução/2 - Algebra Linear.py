import numpy as np
# Básico de Algebra Linear - Matemática onde se estuda os espaços vetoriais e suas transformações
# Operações de Vetores Simples, Multiplicação Vetor-Vetor , Vetor-Matriz , Matriz-Matriz
# Identidade da Matriz e Matriz Inversa.
# No sentido de vetores simples já foi visto anteriormente em 1 - numpy
# Multiplicação de Arrays , Soma de Arrays.
# Multiplicação de Vetores. Nesse sentido uma array é um vetor devido na algebra linear em matemática
# ser uma 'coluna' mas em python usamos como uma 'row'.
U = np.array([1,2,3,4])
v = np.array([5,0,0,8])
print(U * v)
# Em uma Algebra linear multiplicamos cada numero de acordo com o outro na mesma posição
# Sendo o produto a soma dessa multiplicação.
prod = np.dot(U,v)
# Utilizando a função .dot() Product
print(prod)
# Diferenciamos o array de 'rows' com 'Transpose Operation' T
# Função de multiplicação Vetor-Vetor(A,B)
def Vetor_Vetor_Mult(U,v):
    assert(U.shape[0] == v.shape[0])
    # com .shape vemos o a dimensão do array em inteiro.
    n = U.shape[0]
    prod = 0.0
    # Atribuimos o valor que pegamos .shape a n
    for i in range(n):
        prod = prod + U[i] * v[i]
    # Para variavel i no range do tamanho do vetor atribuido.
    # Na indexação 0 e continuamente até acabar = o produto sera a U vezes v
    return prod
print(Vetor_Vetor_Mult(U,v))

# Em uma multiplicação de Matrizes e Vetores, pegamos a mesma ideia da multiplicação de vetores.
# Porem a matriz recebe uma indexação de acordo com o tantos de linhas/'rows'
X = np.array([[1,2,3], # Xº
     [4,5,6], # X¹
     [7,8,9]]) # X²
v = np.array([9,5,7])
# Nesse exemplo a primeira linha da matriz x é Xº a segunda é X¹ e a terceira x².
# Nesse sentido a multiplicação se torna o produto de [Xº, X¹, X²] com z
def Matriz_vetor_mult(X,v):
    assert(X.shape[1] == v.shape[0])
    # Como vai ser uma multiplicação de uma Matriz e ela possui 2 dimensões é comparado o numero de colunas
    # com o array unidimensional.

    numero_linhas = X.shape[0]
    # Assim vamos ter o numero de 'rows' que é preciso multiplicar
    prod = np.zeros(numero_linhas)
    # Criamos uma variavel produto com zerada do tamanho de 'rows' de X.
    for i in range(numero_linhas):
        prod[i] = Vetor_Vetor_Mult(X[i],v)
    return prod

print(Matriz_vetor_mult(X,v))
# Ou
print(X.dot(v))

# Identity Matrix é uma matriz quadrada onde possui 1 em diagonais e zeros no resto.
# Quando uma variavel x*1 = x
print(np.eye(3))
# sendo .eye(x) sendo x o tamanho dessa diagonal.

# Matriz inversa.
# Quando uma matriz elevada a -1 vezes ela mesmo é igual a uma matriz Identity

X = np.array([[1,1,2],
            [0,0.5,1],
              [0,2,1]])

X_inv = np.linalg.inv(X)
# Com essa função temos o inverso de X
print(X_inv)

print(X_inv.dot(X))
# Verifica se a matriz é ou não indetity matrix