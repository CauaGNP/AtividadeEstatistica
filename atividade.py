import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

tabela = pd.read_excel('tabelaAlunos.xlsx');

tabela['MODALIDADE'] = tabela['MODALIDADE'].replace({1: 'PRE', 0: 'EAD'})
tabela['TURNO'] = tabela['TURNO'].replace({1 : 'MAT', 2 : 'VES', 3 : 'INT', 4 : 'NOT'})


tabelaSexo = tabela['SEXO'].value_counts();
tSM = (tabelaSexo["M"] * 100) / 125;
tSF = (tabelaSexo["F"] * 100) / 125;
# print(f"Total sexo masculino: {tSM}%");
# print(f"Total sexo feminino: {tSF}%");
#Mais pessoas do sexo masculino(86,4%) do que feminino(13,6%)


tabelaTurno = tabela['TURNO'].value_counts()
# print(tabelaTurno)
tTNOT = (tabelaTurno["NOT"] * 100) / 125;
tTMAT = (tabelaTurno["MAT"] * 100) / 125;
tTINT = (tabelaTurno["INT"] * 100) / 125;
# print(f"Total alunos turno: noite {tTNOT}%");
# print(f"Total alunos turno: matutino {tTMAT}%");
# print(f"Total alunos turno: integral {tTINT}%");
#Cerca de 64% dos alunos estudam no período noturno  20% estudam no período matutino e 16% estudm no período integral


tabelaModalidade = tabela['MODALIDADE'].value_counts()
# print(tabelaModalidade)
tMPRI = (tabelaModalidade["PRE"] * 100) / 125;
tMEAD = (tabelaModalidade["EAD"] * 100) / 125;
# print(f"Total de alunos na modalidade presencial {tMPRI}%");
# print(f"Total de alunos na modalidade EAD {tMEAD}%");
#Cerca de 84,6% dos alunos estão na modalidade presencial enquanto 15,2% dos alunos estão na modalidade EAD.


tabelaCatAc = tabela['CategoriaAdm'].value_counts()
# print(tabelaCatAc)
TCAPRI = (tabelaCatAc["Privada"] * 100) / 125;
TCAPUB = (tabelaCatAc["Publica"] * 100) / 125;
# print(f"{TCAPRI}% dos alunos são de escola privada");
# print(f"{TCAPUB}% dos alunos são de escola publica");
#Cerca de 72,8% estudaram em escola privada enquanto 27,2% estudaram em escola pública
