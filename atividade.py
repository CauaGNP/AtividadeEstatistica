import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np

tabela = pd.read_excel('tabelaAlunos.xlsx');

tabela['MODALIDADE'] = tabela['MODALIDADE'].replace({1: 'PRE', 0: 'EAD'})
tabela['TURNO'] = tabela['TURNO'].replace({1 : 'MAT', 2 : 'VES', 3 : 'INT', 4 : 'NOT'})
