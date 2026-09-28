import pandas as pd

# __version__ = 3.0.6

# Pandas é um biblioteca para manipular os dados de uma forma tabular por tabelas.

# O data frame é bem parecido com as formas do excel de colunas.
       #df
# A forma é chamada de DataFrame, com dados organizados em colunas.

# Os dados é parecido com uma lista sendo cada lista 1 nesse exemplo abaixa 1 carro. Nessa lista ela é alocada a coluna.

# Então nesse caso os 'dados' é uma lista de listas

# data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],]
# Aqui vemos que há uma lista o [] maior que envolve todas as listas separadas por virgula ela vai ser as rows do nosso arrays multidimensional, distancia 'vertical'.

# columns = ['Fabricante', 'Modelo', 'Ano', 'Motor','Cilindros do Motor','Embreagem', 'Estilo do Veiculo', 'Preço']
# Vemos que a coluna é uma lista normal, ela que da a separação pros dados.
# É usado de uma forma alternativa ao dictionarys pois se não teriamos que repetir várias e várias vezes
# para cada carro.



data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],]

columns = ['Fabricante', 'Modelo', 'Ano', 'Motor','Cilindros do Motor','Embreagem', 'Estilo do Veiculo', 'Preço']

df = pd.DataFrame(data, columns=columns)

# Aqui atribuimos a lista de columns para colunas columns. Assim a biblioteca Pandas já nomeia cada coluna.
df.head()
# com .head() mostramos os primeiros dados de data.
# é usado assim que carregamos uma grande quantidade de dados.
# .tail() as ultimas
# .info() Um resumo do DataFrame, incluido nomes de colunas , tipo de dados e valores não nulos.
# df.tail()
# df.info() # vemos que possui um valor nulo em Motor.
# df.coluna ou df['coluna'] é uma forma de mostrar apenas as informações daquela indexação.
# porem apenas df.coluna não é muito utilizado devido a indisponibilidade de usar espaço 'Estilo_Veiculo'
print(df.Fabricante)

# Acessando 2 ou mais colunas de uma vez, usamos chaves duplas e os valores que queremos.
print(df[['Fabricante','Modelo', 'Preço']])

# Podemos adicionar uma coluna porem temos que adicionar também as novas informações.
df['Teste'] = [1,2,3,4,5]
# Dessa mesma forma podemos substituir as informações caso já possua uma coluna com esse nome.
print(df['Teste'])
del df['Teste']
# Deletando bem pareceido com dictionarys

# O DataFrame é indexado acho que já escrevi isso ou to tendo um dejavu
print(df.index)
# Vemos que a indexação a primeira posição é 0 e nesse data frame a ultima é 5. Onde é selecionado 1 a 1.
# com .loc[Indexação] podemos ver uma linha/rows dos dados. Se for mais de uma rows chaves duplas [[]]
print(df.loc[[0,3]])

# Também podemos mudar o nome da indexação comparando com uma lista que vai dar nome a indexação:
# Precisa ser do mesmo tamanho!
df.index = ['Carro1', 'Carro2', 'Carro3', 'Carro4', 'Carro5']

print(df.loc['Carro2'])

# mas possui outra forma caso esteja nessa formatação de string, podemos usar .iloc[] que usa index normal.

# Igual em numpy nos podemos usar operadores.
# Pegamos uma coluna que possui valores numericos e usamos a operação:
print(df['Preço']*2)
# print(df['Ano'] >= 2017)
# E tbm aplicar funções usadas como .mean() , .max() , .min()

print(df.Preço.mean())

# Utilizando comparações como filtro:
print(df[df['Ano'] >= 2017])

# Multiplos filtros aqui fiquei um pouco perdido devido a troca de chaves mas e entendi o porque
# separa em várias linhas um codigo que dava pra fazer em uma linha. Devido ao abrir e fechar tantas vezes.
print(df[
          (df['Ano'] >= 2017) &
         (df['Preço'] >= 27150)
      ])

# Podemos fazer operações com string para podermos criar um padrão nas informações.
# Geralmente substituidos o espaço ' ' por '_' e colocamos todas as letras minusculas com .str.lower()
df['Estilo do Veiculo'] = df['Estilo do Veiculo'].str.replace(' ', '_').str.lower()
print(df)
# Para padronizar as informações daquela coluna.

# df.unique() Valores unicos de cada coluna. (valores repetidos são contados apenas 1 vez)


# df.isnull() retorna informando quantas informações estão faltantes como True.
# df.isnull().sum() Retorna em valor númerico a quantidade que está faltando em cada coluna.
# Quando precisamos substituir em uma tabela dados nulos ou incoerentes, buscar inconsistencias.


# Agrupamento
print(df.groupby('Embreagem').Preço.mean())
# Muito usado quando você precisa comparar certas colunas com outras no caso saber o preço médio
# Exemplho: um carro com a embreagem manual e comparar com outro com embreagem automatica.
# A diferença de preços de fabricantes, ano do carro.

# Podemos transforma uma coluna numérica em array com .values no nome da coluna;
teste = df.Preço.values
print(teste)

# Convertendo dataframe em dictionary:
# df.to_dict(orient='records')
# Usado para podermos depois de modificarmos a tabela como quisermos podermos salvar essa lista para
# envio ou como backup como quiser.
