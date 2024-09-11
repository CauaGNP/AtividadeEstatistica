import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

tabela = pd.read_excel('tabelaAlunos.xlsx');

tabela['MODALIDADE'] = tabela['MODALIDADE'].replace({1: 'PRE', 0: 'EAD'})
tabela['TURNO'] = tabela['TURNO'].replace({1 : 'MAT', 2 : 'VES', 3 : 'INT', 4 : 'NOT'})

tabelaSexo = tabela['SEXO'].value_counts();
# print(tabelaSexo)
#Mais pessoas do sexo masculino(~= 86,4%) do que feminino(~= 13,6%)
tabelaTurno = tabela['TURNO'].value_counts()
# print(tabelaTurno)
#Cerca de 64% dos alunos estudam no período noturno  20% estudam no período matutino e 16% estudm no período integral
tabelaModalidade = tabela['MODALIDADE'].value_counts()
# print(tabelaModalidade)
#Cerca de 84,6% dos alunos estão na modalidade presencial enquanto 15,2% dos alunos estão na modalidade EAD.
tabelaCatAc = tabela['CategoriaAdm'].value_counts()
print(tabelaCatAc)
#Cerca de 72,8% estudaram em escola privada enquanto 27,2% estudaram em escola pública
