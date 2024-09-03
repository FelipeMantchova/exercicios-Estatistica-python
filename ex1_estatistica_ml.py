# -*- coding: utf-8 -*-
"""Ex1_Estatistica_ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AmVzrTr5WXmVv6TFc_jmgC1xyji4rO4_

# Apresentação do Plano de Ensino e Introdução &mdash; Atividade Prática

**Prof. Dr. Jefferson O. Andrade**  
**Pós-graduação em Desenvolvimento de Aplicações Inteligentes**  
**Estatística para Aprendizado de Máquina &mdash; Aula 01**

**Nome:** FELIPE MANTOVANELLI BARROS  
**Matrícula:** 20231DEVAI0025

## Introdução à Atividade

Nesta atividade, vamos explorar um conjunto de dados usando a biblioteca pandas e criar um relatório básico com observações e perguntas para futura investigação.

## Objetivos

- Familiarizar-se com a biblioteca pandas para manipulação de dados
- Aprender a realizar análises exploratórias de dados básicas
- Formular perguntas que possam ser respondidas posteriormente por técnicas de aprendizado de máquinas

## Conjunto de Dados

Para esta atividade, vamos usar o conjunto de dados 'Iris'. Este é um conjunto de dados famoso que contém medidas de 150 flores Iris de três espécies diferentes.
"""

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Carregando o conjunto de dados
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Adicionando a coluna alvo
df['species'] = iris.target

# Mostrando as primeiras linhas do DataFrame
df.head()

"""## Explorando o Conjunto de Dados

Agora que temos nosso conjunto de dados carregado em um DataFrame, podemos começar a explorá-lo.
"""

# Informações gerais sobre o conjunto de dados
df.info()

# Resumo estatístico das características
df.describe()

# Contagem de valores para a espécie
df['species'].value_counts()

"""## Visualização dos Dados

A visualização é uma parte essencial da análise exploratória de dados. Vamos criar alguns gráficos básicos para entender melhor nossos dados.
"""

# Histograma de cada característica
df.hist(figsize=(10, 8))
plt.tight_layout()  # Ajusta o layout para que os gráficos não se sobreponham
plt.show()

# Gráfico de dispersão entre comprimento e largura da pétala
plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=df['species'])
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.show()

"""## Perguntas para Investigação Futura

Com base na exploração inicial do conjunto de dados, que perguntas podemos formular para investigações futuras? Lembre-se de que estas perguntas não precisam ter respostas agora. O objetivo é formular perguntas que possam ser interessantes para responder usando técnicas de aprendizado de máquinas.

Aqui estão alguns exemplos de perguntas que poderíamos fazer:

1. Podemos prever a espécie de uma flor Iris com base em suas medidas?
2. Quais características são mais informativas para prever a espécie de uma flor?
3. Existe uma relação entre o comprimento e a largura da pétala e da sépala?

Agora, é a sua vez! Explore o conjunto de dados e registre suas perguntas e observações.

### Observações

1. A Espécie 2 tem maior as pétalas e sépalas com maiores áreas

### Perguntas:

1. Quais são as medianas, modas e médias das características em cada espécie?

2. Qual espécie tem maior razão entre pétalas? E entre sépalas?

3. Qual a área aproximada de cada pétala e sépala?

4. Qual epécie tem a maior pétala? E sépala?

Lembre-se, a melhor maneira de aprender é fazer. Não tenha medo de experimentar e tentar coisas novas. Boa sorte!

----------------------------------------------
"""

#primeiro vou altrear o nome das colunas
novos_nomes = ['sl', 'sw', 'pl', 'pw', 'spc']
df.columns = novos_nomes
df.head()

#1 Quais são as medianas, modas e médias das características em cada espécie?
#Primeiro preciso saber quantas espécies distintas existem no dataset

especies_distintas = df['spc'].unique()
especies_distintas

#Mediana
for especie in especies_distintas:
    mediana_sl = df[df['spc'] == especie]['sl'].median()
    mediana_sw = df[df['spc'] == especie]['sw'].median()
    mediana_pl = df[df['spc'] == especie]['pl'].median()
    mediana_pw = df[df['spc'] == especie]['pw'].median()
    print(f'Mediana da espécie {especie} - SL:{mediana_sl}; SW:{mediana_sw}; PL:{mediana_pl}; PW:{mediana_pw};')

#1 Quais são as medianas, modas e médias das características em cada espécie?
#Moda
for especie in especies_distintas:
    moda_sl = df[df['spc'] == especie]['sl'].mode()
    moda_sw = df[df['spc'] == especie]['sw'].mode()
    moda_pl = df[df['spc'] == especie]['pl'].mode()
    moda_pw = df[df['spc'] == especie]['pw'].mode()
    print(f'Moda da espécie {especie} - SL:{moda_sl[0]}; SW:{moda_sw[0]}; PL:{moda_pl[0]}; PW:{moda_pw[0]};')

#1 Quais são as medianas, modas e médias das características em cada espécie?
#Média
for especie in especies_distintas:
    mean_sl = df[df['spc'] == especie]['sl'].mean()
    mean_sw = df[df['spc'] == especie]['sw'].mean()
    mean_pl = df[df['spc'] == especie]['pl'].mean()
    mean_pw = df[df['spc'] == especie]['pw'].mean()
    print(f'Média da espécie {especie} - SL:{round(mean_sl, 2)}; SW:{round(mean_sw, 2)}; PL:{round(mean_pl, 2)}; PW:{round(mean_pw, 2)};')

#2 Qual espécie tem maior razão entre pétalas? E entre sépalas?
#Primeiro farei uma cópia do dataframe
#Depois criarei uma nova coluna com as razões de pétalas e sépalas

df_copy = df.copy()

df_copy['rs'] = df_copy['sl'] / df_copy['sw']
df_copy['rp'] = df_copy['pl'] / df_copy['pw']

df_copy

linha_maior_rs = df_copy.loc[df_copy['rs'].idxmax()]
print('A maior razão de sépala está na espécie', linha_maior_rs.spc)


linha_maior_rp = df_copy.loc[df_copy['rp'].idxmax()]
print('A maior razão de pétala está na espécie', linha_maior_rp.spc)

#3 Qual a área aproximada de cada pétala e sépala?
#Criarei as colunas assim como fiz par a razão, usarei uma fórmula de calcular a área de elipses


df_copy['as'] = 3.14159 * df_copy['sl'] * df_copy['sw']
df_copy['ap'] = 3.14159 * df_copy['pl'] * df_copy['pw']

df_copy

linha_maior_as = df_copy.loc[df_copy['as'].idxmax()]
print('A maior área de sépala está na espécie', linha_maior_as.spc)


linha_maior_ap = df_copy.loc[df_copy['ap'].idxmax()]
print('A maior área de pétala está na espécie', linha_maior_ap.spc)