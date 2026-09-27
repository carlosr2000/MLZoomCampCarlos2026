import pandas as pd

# __version__ = 3.0.6

# Pandas é um biblioteca para manipular os dados de uma forma tabular por tabelas.

# Bem parecido com as formas do excel de colunas.

# A forma é chamada de DataFrame, com dados organizados em colunas.

# Os dados é parecido com uma lista sendo cada lista 1 nesse exemplo abaixa 1 carro. Nessa lista ela é alocada a coluna.

# Então nesse caso os 'dados' é uma lista de listas

# data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],]

# Aqui vemos que há uma lista o [] maior que envolve todas as listas separadas por virgula ela vai ser as rows do nosso arrays multidimensional, distancia 'vertical'.

# columns = ['Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders','Transmission Type', 'Vehicle_Style', 'MSRP']

# Vemos que a coluna é uma lista normal, ela que da a separação pros dados. A coluna é uma 'distancia' horzontal.

data = [['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],]

columns = ['Make', 'Model', 'Year', 'Engine HP','Engine Cylinders','Transmission Type', 'Vehicle_Style', 'MSRP']

df = pd.DataFrame(data, columns=columns)
print(df)