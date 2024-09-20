# Importando as bibliotecas pandas e matplotlib.pyplotm e renomeando-as para: pd e plt.
import pandas as pd;
import matplotlib.pyplot as plt;

# Guardando a tabela em uma variável "tabela",
tabela = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/baseEnade17_Sistemas.xlsx');

# Mudando os valores da coluna MODALIDADE (trocando os valores 0 e 1 pelos valores EAD e PRE(presencial)).
tabela['MODALIDADE'] = tabela['MODALIDADE'].replace({1: 'PRE', 0: 'EAD'});
tabela['TURNO'] = tabela['TURNO'].replace({1 : 'MAT', 2 : 'VES', 3 : 'INT', 4 : 'NOT'});

# Transformando a coluna "SEXO" em uma tabela e guardando a quantidade de vezes que os valores "M" e "F" aparecem na tabela.
tabelaSexo = tabela['SEXO'].value_counts();
# Transformando a quantidade de pessoas do sexo masculino em poprcentagem.
colunaSexoM = (tabelaSexo["M"] * 100) / 125;
# Transformando a quantidade de pessoas do sexo feminino em poprcentagem.
colunaSexoF = (tabelaSexo["F"] * 100) / 125;

# Printando a coluna "SEXO".
print(tabelaSexo);

# Utilizando a biblioteca matplotlib.pyplot para criar um gráfico de barras da coluna "SEXO".
# "tabelaSexo.index" fornece rótulos para o eixo x.
# "tabelaSexo.values" fornece os valores para o eixo y.
# "color" muda as cores das colunas.
plt.bar(tabelaSexo.index, tabelaSexo.values, color=['mediumblue', 'firebrick']);
# Define o rótulo do eixo x como "Sexo".
plt.xlabel('Sexo');
# Define o rótulo do eixo y como "Contagem".
plt.ylabel('Contagem');
# Define o título do gráfico.
plt.title('Distribuição de Sexo');
# Exibe o gráfico na tela.
plt.show();

# Printando a porcentagem do total de pessoas do sexo masculino.
print(f"Total sexo masculino: {colunaSexoM}%");
# Printando a porcentagem do total de pessoas do sexo feminino.
print(f"Total sexo feminino: {colunaSexoF}%");

# Realizando a análide da coluna "SEXO".
print(f"Através da tabela e do gráfico permite observar a diferença entre os gêneros. O sexo masculino é representado por {tabelaSexo['M']} pessoas, correspondendo a aproximadamente {colunaSexoM}% do total, enquanto o sexo feminino é representado por {tabelaSexo['F']} pessoas, correspondendo a aproximadamente {colunaSexoF}%.")

# Transformando a coluna "TURNO" em uma tabela e guardando a quantidade de vezes que os valores "NOT", "MAT", "INT" e "VES" aparecem na tabela.
tabelaTurno = tabela['TURNO'].value_counts();

# Transformando a quantidade de vezes que o turno "NOT" aparece na tabela em porcentagem.
colunaTurnoNoite = (tabelaTurno["NOT"] * 100) / 125;
# Transformando a quantidade de vezes que o turno "MAT" aparece na tabela em porcentagem.
colunaTurnoMatutino = (tabelaTurno["MAT"] * 100) / 125;
# Transformando a quantidade de vezes que o turno "INT" aparece na tabela em porcentagem.
colunaTurnoIntegral = (tabelaTurno["INT"] * 100) / 125;
# Transformando a quantidade de vezes que o turno "VES" aparece na tabela em porcentagem.

# Printando a tabela "TURNO".
print(tabelaTurno);

# Utilizando a biblioteca matplotlib.pyplot para criar um gráfico de barras da coluna "TURNO".
# "tabelaTurno.index" fornece rótulos para o eixo x.
# "tabelaTurno.values" fornece os valores para o eixo y.
# "color" muda as cores das colunas.
plt.bar(tabelaTurno.index, tabelaTurno.values, color=['mediumblue', 'gold', 'firebrick']);
# Define o rótulo do eixo x como "Turno".
plt.xlabel('Turno');
# Define o rótulo do eixo y como "Contagem".
plt.ylabel('Contagem');
# Define o título do gráfico.
plt.title('Distribuição dos Turnos');
# Dexibe o gráfico na tela.
plt.show();

# Printando a porcentagem do total do turno noite.
print(f"Total alunos turno: noite {colunaTurnoNoite}%");
# Printando a porcentagem do total do turno matutino.
print(f"Total alunos turno: matutino {colunaTurnoMatutino}%");
# Printando a porcentagem do total do turno integral.
print(f"Total alunos turno: integral {colunaTurnoIntegral}%");
# Printando a porcentagem do total do turno vespertino.
print(f"Total alunos turno: vespertino 0.0%");

# Realizando a análise da coluna "MODALIDADE"
print(f"Por meio da tabela e do gráfico podemos observar a distribuição dos turnos. O turno noturno conta com {tabelaTurno['NOT']} estudantes, representando {colunaTurnoNoite}% do total. O turno matutino possui {tabelaTurno['MAT']} estudantes, correspondendo a {colunaTurnoMatutino}%. O turno integral conta com {tabelaTurno['INT']} estudantes, representando {colunaTurnoIntegral}%, enquanto o turno vespertino não possui estudantes, representando 0% do total.")

# Transformando a coluna "MODALIDADE" em uma tabela e guardando a quantidade de vezes que os valores "PRE" e "EAD" aparecem na tabela.
tabelaModalidade = tabela['MODALIDADE'].value_counts();

# Transformando a quantidade de vezes que a modalidade "PRE" aparece na tabela em porcentagem.
colunaModalidadePresencial = (tabelaModalidade["PRE"] * 100) / 125;
# Transformando a quantidade de vezes que a modalidade "EAD" aparece na tabela em porcentagem.
colunaModalidadeEAD = (tabelaModalidade["EAD"] * 100) / 125;

# Printando a tabela "MODALIDADE".
print(tabelaModalidade)

# Utilizando a biblioteca matplotlib.pyplot para criar um gráfico de barras da coluna "TURNO".
# "tabelaModalidade.index" fornece rótulos para o eixo x.
# "tabelaModalidade.values" fornece os valores para o eixo y.
# "color" muda as cores das colunas.
plt.bar(tabelaModalidade.index, tabelaModalidade.values, color=['mediumblue', 'firebrick']);
# Define o rótulo do eixo x como "Modalidade".
plt.xlabel('Modalidade');
# Define o rótulo do eixo y como "Contagem".
plt.ylabel('Contagem');
# Define o título do gráfico.
plt.title('Distribuição das Modalidades');
# Dexibe o gráfico na tela.
plt.show();

# Printando a porcentagem do total de alunos da modalidade presencial.
print(f"Total de alunos na modalidade presencial: {colunaModalidadePresencial}%");
# Printando a porcentagem do total de alunos da modalidade EAD.
print(f"Total de alunos na modalidade EAD: {colunaModalidadeEAD}%");

# Realizando a análise da coluna "MODALIDADE"
print(f"A análise da tabela e do gráfico permite observar a diferença na quantidade de alunos que optam pela modalidade presencial ({tabelaModalidade['PRE']} alunos, correspondendo a aproximadamente {colunaModalidadePresencial}%) em comparação àqueles que escolhem a modalidade EAD ({tabelaModalidade['EAD']} alunos, representando aproximadamente {colunaModalidadeEAD}%).")

# Transformando a coluna "Categoria acadêmica" em uma tabela e guardando a quantidade de vezes que os valores "Privada" e "Publica" aparecem na tabela.
tabelaCategoriaAcademica = tabela['CategoriaAdm'].value_counts();

# Transformando a quantidade de vezes que a categoria academica "Privada" aparece na tabela em porcentagem.
colunaCategoriaAcademicaPrivada = (tabelaCategoriaAcademica["Privada"] * 100) / 125;
# Transformando a quantidade de vezes que a categoria acadecima "Publica" aparece na tabela em porcentagem.
colunaCategoriaAcademicaPublica = (tabelaCategoriaAcademica["Publica"] * 100) / 125;

# Printando a tabela "CategoriaAcademica".
print(tabelaCategoriaAcademica);

# Utilizando a biblioteca matplotlib.pyplot para criar um gráfico de barras da coluna "TURNO".
# "tabelaCategoriaAcademica.index" fornece rótulos para o eixo x.
# "tabelaCategoriaAcademica.values" fornece os valores para o eixo y.
# "color" muda as cores das colunas.
plt.bar(tabelaCategoriaAcademica.index, tabelaCategoriaAcademica.values, color=['mediumblue', 'firebrick']);
# Define o rótulo do eixo x como "Categoria Academica".
plt.xlabel('Categoria Academica');
# Define o rótulo do eixo y como "Contagem".
plt.ylabel('Contagem');
# Define o título do gráfico.
plt.title('Distribuição das Categorias Academicas');
# Dexibe o gráfico na tela.
plt.show();

# Printando a porcentagem do total de alunos da categoria academica privada.
print(f"{colunaCategoriaAcademicaPrivada}% dos alunos são de escola privada");
# Printando a porcentagem do total de alunos da categoria academica publica.
print(f"{colunaCategoriaAcademicaPublica}% dos alunos são de escola publica");

# Printando a análise da coluna categoria academica.
print(f"Verificando a tabela e o gráfico é possível analisar a diferença das categorias acadêmicas dos alunos, que, em sua maioria, se encaixa na categoria privada com {tabelaCategoriaAcademica['Privada']} alunos, representando {colunaCategoriaAcademicaPrivada}% da quantidades de vagas, enquanto {tabelaCategoriaAcademica['Publica']} representam os alunos de escola publica, respectivamente {colunaCategoriaAcademicaPublica}% do gráfico.");

# Criando uma tabela de contigência usando a biblioteca pandas e a função .crosstab().
# Os primeiros parêmetros indica as colunas da tabela que iremos utilizar nesse caso as colunas "SEXO" e "MODALIDADE".
# "margins" são utilizadas para criar a soma dos valores.
# "margins_name" que representará o nome da nossa soma, no caso "Total".
tabelaDeContigencia = pd.crosstab(
    tabela["SEXO"],
    tabela["MODALIDADE"],
    margins= 'True',
    margins_name= "Total"
    );

# Printando a tabela de contigência.
print(tabelaDeContigencia);

# Cria um gráfico de barras agrupadas.
tabelaDeContigencia.plot(kind='bar', color=['mediumblue', 'firebrick', 'black'], width=0.8);

# Define o rótulo do eixo x como "Sexo".
plt.xlabel('Sexo');
# Define o rótulo do eixo y como "Número de Pessoas"
plt.ylabel('Número de Pessoas');
# Título do gráfico
plt.title('Distribuição das Modalidades por Sexo');
# Cria uma legenda do gráfico como "Modalidade".
plt.legend(title='Modalidade');
# Printa o gráfico.
plt.show();

# Printando a análise da tabela de contigência.
print("Nota-se uma maior quantidade de estudantes na modalidade presencial em comparação com a EAD.");
print("Na modalidade EAD, a maioria das vagas é preenchida por pessoas do sexo masculino.");
print("Da mesma forma, na modalidade presencial, os indivíduos do sexo masculino também predominam no preenchimento das vagas.");

# Importando a biblioteca seaborn e a renomeando para sns.
import seaborn as sns;

# Guardando os valores "EAD" da coluna "MODALIDADE".
ead = tabela[tabela['MODALIDADE'] == 'EAD'];

# NOTA_GERAL - EAD.

# Obtendo o valor da media(.mean()) e arrendodando para uma casas decimais(round(...,1)).
mediaEAD = round(ead['NOTA_GERAL'].mean(), 1);
# Obtendo o valor da mediana(.median()).
medianaEAD = ead['NOTA_GERAL'].median();
# Obtendo o valor do desvio padrão(.std()) e arrendodando para uma casas decimais(round(...,1)).
desvioPadraoEAD = round(ead['NOTA_GERAL'].std(), 1);
# Obtendo o valor do coeficiente de variação e arrendodando para uma casas decimais(round(...,1)).
coeficienteVariacaoEAD = round((ead['NOTA_GERAL'].std() / ead['NOTA_GERAL'].mean()) * 100, 1);
# Obtendo o valor do primeiro quartil (.quantile(0.25)) e arrendodando para uma casas decimais(round(...,1)).
primeiroQuartilEAD = round(ead['NOTA_GERAL'].quantile(0.25), 1);
# Obtendo o valor do terceiro quartil (.quantile(0.75)) e arrendodando para uma casas decimais(round(...,1)).
terceiroQuartilEAD = round(ead['NOTA_GERAL'].quantile(0.75), 1);

# Calculando o valor máximo e mínimo.
valorMaximoEAD = round(terceiroQuartilEAD + ((terceiroQuartilEAD - primeiroQuartilEAD) * 1.5),1);
valorMinimoEAD = round(primeiroQuartilEAD - ((terceiroQuartilEAD - primeiroQuartilEAD) * 1.5),1);

# Guardando os valores dos outliers e arrendodando para uma casas decimais(round(...,1)).
outlierMaximoEAD = round(ead['NOTA_GERAL'].max(), 1);
outlierMinimoEAD = round(ead['NOTA_GERAL'].min(), 1);

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos EAD (coluna "NOTA_GERAL"): {mediaEAD}');
print(f'Mediana dos alunos EAD (coluna "NOTA_GERAL"): {medianaEAD}');
print(f'Desvio padrão dos alunos EAD (coluna "NOTA_GERAL"): {desvioPadraoEAD}');
print(f'Coeficiente de Variação dos alunos EAD (coluna "NOTA_GERAL"): {coeficienteVariacaoEAD}');
print(f'Primeiro Quartil dos alunos EAD (coluna "NOTA_GERAL"): {primeiroQuartilEAD}');
print(f'Terceiro Quartil dos alunos EAD (coluna "NOTA_GERAL"): {terceiroQuartilEAD}');

# Guardando os valores "PRE" da coluna "MODALIDADE".
presencial = tabela[tabela['MODALIDADE'] == 'PRE'];

# NOTA_GERAL - Presencial

# Obtendo o valor da media (.mean()) e arrendodando para uma casas decimais(round(...,1)).
mediaPresencial = round(presencial['NOTA_GERAL'].mean(), 1);
# Obtendo o valor da mediana (.median()).
medianaPresencial = presencial['NOTA_GERAL'].median();
# Obtendo o valor do desvio padrão (.std()) e arrendodando para uma casas decimais(round(...,1)).
desvioPadraoPresencial = round(presencial['NOTA_GERAL'].std(), 1);
# Obtendo o valor do coeficiente de variação e arrendodando para uma casas decimais(round(...,1)).
coeficienteVariacaoPresencial = round((presencial['NOTA_GERAL'].std() / presencial['NOTA_GERAL'].mean()) * 100, 2);
# Obtendo o valor do primeiro quartil (.quantile(0.25)) e arrendodando para uma casas decimais(round(...,1))..
primeiroQuartilPresencial = round(presencial['NOTA_GERAL'].quantile(0.25),1);
# Obtendo o valor do terceiro quartil (.quantile(0.75)) e arrendodando para uma casas decimais(round(...,1))..
terceiroQuartilPresencial = round(presencial['NOTA_GERAL'].quantile(0.75),1);

# Calculando o valor máximo e mínimo.
valorMaximoPresencial = terceiroQuartilEAD + ((terceiroQuartilPresencial - primeiroQuartilPresencial) * 1.5).round(1);
valorMinimoPresencial = primeiroQuartilEAD - ((terceiroQuartilPresencial - primeiroQuartilPresencial) * 1.5).round(1);

# Guardando os valores dos outliers.
outlierMaximoPresencial = presencial['NOTA_GERAL'].max();
outlierMinimoPresencial = presencial['NOTA_GERAL'].min();

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {mediaPresencial}');
print(f'Mediana dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {medianaPresencial}');
print(f'Desvio padrão dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {desvioPadraoPresencial}');
print(f'Coeficiente de variação dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {coeficienteVariacaoPresencial}');
print(f'Primeiro quartil dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {primeiroQuartilPresencial}');
print(f'Terceiro quartil dos alunos da modalidade presencial (coluna "NOTA_GERAL"): {terceiroQuartilPresencial}');

# BloxPlot "NOTA_GERAL"

# .figure(tamanho do gráfico).
plt.figure(figsize=(8, 6));
# Criando o gráfico bloxplot.
sns.boxplot(x='MODALIDADE', y='NOTA_GERAL', data=tabela, );
# Título do gráfico.
plt.title('Distribuição das Notas por Modalidade (NOTA_GERAL)');
# Definindo o rótulo do eixo x como "Modalidade".
plt.xlabel('Modalidade');
# Definindo o rótulo do eixo y como "Notas"
plt.ylabel('Notas');
# Printa o gráfico.
plt.show();

# Análise dos gráficos.
print("Analisando o gráfico BoxPlot:");
print(f"O gráfico referente à modalidade presencial apresenta uma distribuição simétrica, onde a distância entre o primeiro e o terceiro quartil é equidistante da mediana.Além disso os valores da media ({mediaPresencial}) e mediana ({medianaPresencial}) são relativamente próximos.");
print(f"Também podemos observar que alguns alunos obtiveram notas superiores ({outlierMaximoPresencial}) ao valor máximo esperado ({valorMaximoPresencial}).");
print(f"Em contrapartida, o gráfico da modalidade EAD apresenta uma distribuição assimétrica negativa, visto que a linha da mediana está mais próxima do terceiro quartil, indicando que a média ({mediaEAD}) é inferior à mediana ({medianaEAD}).");
print(f"Observa-se também que alguns alunos obtiveram notas maiores ({outlierMaximoPresencial}) ao valor máximo esperado ({valorMaximoPresencial}).");
print(f"Da mesma forma, alguns alunos na modalidade EAD atingiram notas superiores ({outlierMaximoEAD}) ao valor máximo esperado ({valorMaximoEAD}).");


# NOTA-FORM_GER - EAD

# Obtendo o valor da media (.mean()) e arrendodando para duas casas decimais(round(...,2)).
mediaFormGerEAD = round(ead['NOTA-FORM_GER'].mean(), 2);
# Obtendo o valor da mediana (.median()).
medianaFormGerEAD = ead['NOTA-FORM_GER'].median();
# Obtendo o valor do desvio padrão (.std()) e arrendodando para duas casas decimais(round(...,2)).
desvioPadraoFormGerEAD = round(ead['NOTA-FORM_GER'].std(), 2);
# Obtendo o valor do coeficiente de variação e arrendodando para duas casas decimais(round(...,2)).
coeficienteVariacaoFormGerEAD = round((ead['NOTA-FORM_GER'].std() / ead['NOTA-FORM_GER'].mean()) * 100, 2);
# Obtendo o valor do primeiro quartil (.quantile(0.25)).
primeiroQuartilFormGerEAD = ead['NOTA-FORM_GER'].quantile(0.25);
# Obtendo o valor do terceiro quartil (.quantile(0.75)).
terceiroQuartilFormGerEAD = ead['NOTA-FORM_GER'].quantile(0.75);

# Calculando o valor máximo e mínimo.
valorMaximoFormGerEAD = round(terceiroQuartilFormGerEAD + ((terceiroQuartilFormGerEAD - primeiroQuartilFormGerEAD) * 1.5),1);
valorMinimoFormGerEAD = round(primeiroQuartilFormGerEAD - ((terceiroQuartilFormGerEAD - primeiroQuartilFormGerEAD) * 1.5),1);

# Guardando os valores dos outliers e arrendodando para uma casas decimais(round(...,1)).
outlierMaximoFormGerEAD = round(ead['NOTA-FORM_GER'].max(), 1);
outlierMinimoFormGerEAD = round(ead['NOTA-FORM_GER'].min(), 1);

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos EAD (coluna "NOTA-FORM_GER"): {mediaFormGerEAD}');
print(f'Mediana dos alunos EAD (coluna "NOTA-FORM_GER"): {medianaFormGerEAD}');
print(f'Desvio padrão dos alunos EAD (coluna "NOTA-FORM_GER"): {medianaFormGerEAD}');
print(f'Coeficiente de Variação dos alunos EAD (coluna "NOTA-FORM_GER"): {coeficienteVariacaoFormGerEAD}');
print(f'Primeiro Quartil dos alunos EAD (coluna "NOTA-FORM_GER"): {primeiroQuartilFormGerEAD}');
print(f'Terceiro Quartil dos alunos EAD (coluna "NOTA-FORM_GER"): {terceiroQuartilFormGerEAD}');

# NOTA-FORM_GER - Presencial

# Obtendo o valor da media (.mean()) e arrendodando para duas casas decimais(round(...,2)).
mediaFormGerPresencial = round(presencial['NOTA-FORM_GER'].mean(), 2);
# Obtendo o valor da mediana (.median()).
medianaFormGerPresencial = presencial['NOTA-FORM_GER'].median();
# Obtendo o valor do desvio padrão (.std()) e arrendodando para duas casas decimais(round(...,2)).
desvioPadraoFormGerPresencial = round(presencial['NOTA-FORM_GER'].std(), 2);
# Obtendo o valor do coeficiente de variação e arrendodando para duas casas decimais(round(...,2)).
coeficienteVariacaoFormGerPresencial = round((presencial['NOTA-FORM_GER'].std() / presencial['NOTA-FORM_GER'].mean()) * 100, 2);
# Obtendo o valor do primeiro quartil (.quantile(0.25))e arredondando para duas casas decimais(round(...,2)).
primeiroQuartilFormGerPresencial = round(presencial['NOTA-FORM_GER'].quantile(0.25), 2);
# Obtendo o valor do terceiro quartil (.quantile(0.75)).
terceiroQuartilFormGerPresencial = presencial['NOTA-FORM_GER'].quantile(0.75);

# Calculando o valor máximo e mínimo.
valorMaximoFormGerPresencial = terceiroQuartilEAD + ((terceiroQuartilFormGerPresencial - primeiroQuartilFormGerPresencial) * 1.5).round(1);
valorMinimoFormGerPresencial = primeiroQuartilEAD - ((terceiroQuartilFormGerPresencial - primeiroQuartilFormGerPresencial) * 1.5).round(1);

# Guardando os valores dos outliers.
outlierMaximoFormGerPresencial = presencial['NOTA-FORM_GER'].max();
outlierMinimoFormGerPresencial = presencial['NOTA-FORM_GER'].min();

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {mediaFormGerPresencial}');
print(f'Mediana dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {medianaFormGerPresencial}');
print(f'Desvio padrão dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {desvioPadraoFormGerPresencial}');
print(f'Coeficiente de variação dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {coeficienteVariacaoFormGerPresencial}');
print(f'Primeiro quartil dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {primeiroQuartilFormGerPresencial}');
print(f'Terceiro quartil dos alunos da modalidade presencial (coluna "NOTA-FORM_GER"): {terceiroQuartilFormGerPresencial}');

# BloxPlot "NOTA-FORM_GER".

# .figure(tamanho do gráfico).
plt.figure(figsize=(8, 6));
# Criando o gráfico bloxplot.
sns.boxplot(x='MODALIDADE', y='NOTA-FORM_GER', data=tabela);
# Título do gráfico.
plt.title('Distribuição das Notas por Modalidade (NOTA-FORM_GER)');
# Definindo o rótulo do eixo x como "Modalidade".
plt.xlabel('Modalidade');
# Definindo o rótulo do eixo y como "Notas"
plt.ylabel('Notas');
# Printa o gráfico.
plt.show();

# Análise dos gráficos.
print("Analisando o gráfico BoxPlot:");
print(f"O gráfico referente á modalidade presencial apresenta uma distribuição assimétrica negativa, uma vez que a linha da mediana está mais próximo do terceiro quartil, apontando que a media ({mediaFormGerPresencial}) é menor que a mediana ({medianaFormGerPresencial})");
print(f"Já no gráfico da modalidade EAD apresenta uma distribuição assimétrica negativa, visto que a linha da mediana está mais próximo do primeiro quartil, indicando que a media ({mediaFormGerEAD}) é maior que a mediana ({medianaFormGerEAD})");
print(f"Ambas modalidades não apresentam outliers, indicando que nenhuma das notas ultrapassaram os valores máximos ou mínimos.");

# NOTA_COMPESPE - EAD

# Obtendo o valor da media (.mean()) e arrendodando para duas casas decimais(round(...,2)).
mediaCompespeEAD = round(ead['NOTA_COMPESPE'].mean(), 2);
# Obtendo o valor da mediana (.median()).
medianaCompespeEAD = ead['NOTA_COMPESPE'].median();
# Obtendo o valor do desvio padrão (.std()) e arrendodando para duas casas decimais(round(...,2)).
desvioPadraoCompespeEAD = round(ead['NOTA_COMPESPE'].std(), 2);
# Obtendo o valor do coeficiente de variação e arrendodando para duas casas decimais(round(...,2)).
coeficienteVariacaoCompespeEAD = round((ead['NOTA_COMPESPE'].std() / ead['NOTA_COMPESPE'].mean()) * 100, 2);
# Obtendo o valor do primeiro quartil (.quantile(0.25)).
primeiroQuartilCompespeEAD = round(ead['NOTA_COMPESPE'].quantile(0.25), 2);
# Obtendo o valor do terceiro quartil (.quantile(0.75)).
terceiroQuartilCompespeEAD = ead['NOTA_COMPESPE'].quantile(0.75);

# Calculando o valor máximo e mínimo.
valorMaximoCompespeEAD = round(terceiroQuartilCompespeEAD + ((terceiroQuartilCompespeEAD - primeiroQuartilCompespeEAD) * 1.5),1);
valorMinimoCompespeEAD = round(primeiroQuartilCompespeEAD - ((terceiroQuartilCompespeEAD - primeiroQuartilCompespeEAD) * 1.5),1);

# Guardando os valores dos outliers e arrendodando para uma casas decimais(round(...,1)).
outlierMaximoCompespeEAD = round(ead['NOTA_COMPESPE'].max(), 1);
outlierMinimoCompespeEAD = round(ead['NOTA_COMPESPE'].min(), 1);

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos EAD (coluna "NOTA_COMPESPE"): {mediaCompespeEAD}');
print(f'Mediana dos alunos EAD (coluna "NOTA_COMPESPE"): {medianaCompespeEAD}');
print(f'Desvio padrão dos alunos EAD (coluna "NOTA_COMPESPE"): {medianaCompespeEAD}');
print(f'Coeficiente de Variação dos alunos EAD (coluna "NOTA_COMPESPE"): {coeficienteVariacaoCompespeEAD}');
print(f'Primeiro Quartil dos alunos EAD (coluna "NOTA_COMPESPE"): {primeiroQuartilCompespeEAD}');
print(f'Terceiro Quartil dos alunos EAD (coluna "NOTA_COMPESPE"): {terceiroQuartilCompespeEAD}');

# NOTA-COMPESPE - Presencial

# Obtendo o valor da media (.mean()) e arrendodando para duas casas decimais(round(...,2)).
mediaCompespePresencial = round(presencial['NOTA_COMPESPE'].mean(), 2);
# Obtendo o valor da mediana (.median()).
medianaCompespePresencial = presencial['NOTA_COMPESPE'].median();
# Obtendo o valor do desvio padrão (.std()) e arrendodando para duas casas decimais(round(...,2)).
desvioPadraoCompespePresencial = round(presencial['NOTA_COMPESPE'].std(), 2);
# Obtendo o valor do coeficiente de variação e arrendodando para duas casas decimais(round(...,2)).
coeficienteVariacaoCompespePresencial = round((presencial['NOTA_COMPESPE'].std() / presencial['NOTA_COMPESPE'].mean()) * 100, 2);
# Obtendo o valor do primeiro quartil (.quantile(0.25))e arredondando para duas casas decimais(round(...,2)).
primeiroQuartilCompespePresencial = round(presencial['NOTA-FORM_GER'].quantile(0.25), 2);
# Obtendo o valor do terceiro quartil (.quantile(0.75)).
terceiroQuartilCompespePresencial = presencial['NOTA-FORM_GER'].quantile(0.75);

# Calculando o valor máximo e mínimo.
valorMaximoCompespePresencial = terceiroQuartilEAD + ((terceiroQuartilCompespePresencial - primeiroQuartilCompespePresencial) * 1.5).round(1);
valorMinimoCompespePresencial = primeiroQuartilEAD - ((terceiroQuartilCompespePresencial - primeiroQuartilCompespePresencial) * 1.5).round(1);


# Guardando os valores dos outliers.
outlierMaximoCompespePresencial = presencial['NOTA_COMPESPE'].max();
outlierMinimoCompespePresencial = presencial['NOTA_COMPESPE'].min();

# Printando os valores da media, mediana, desvio padrão, primeiro quartil e terceiro quartil.
print(f'Media dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {mediaCompespePresencial}');
print(f'Mediana dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {medianaCompespePresencial}');
print(f'Desvio padrão dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {desvioPadraoCompespePresencial}');
print(f'Coeficiente de variação dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {coeficienteVariacaoCompespePresencial}');
print(f'Primeiro quartil dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {primeiroQuartilCompespePresencial}');
print(f'Terceiro quartil dos alunos da modalidade presencial (coluna "NOTA_COMPESPE"): {terceiroQuartilCompespePresencial}');

# Codigo para criar o bloxplot "NOTA_COMPESPE"

# .figure(tamanho do gráfico).
plt.figure(figsize=(8, 6));
# Criando o gráfico bloxplot.
sns.boxplot(x='MODALIDADE', y='NOTA_COMPESPE', data=tabela);
# Título do gráfico.
plt.title('Distribuição das Notas por Modalidade (NOTA_COMPESPE)');
# Definindo o rótulo do eixo x como "Modalidade".
plt.xlabel('Modalidade');
# Definindo o rótulo do eixo y como "Notas"
plt.ylabel('Notas');
# Printa o gráfico.
plt.show();

# Análise dos gráficos.
print(f"Analisando o gráfico BloxPlot:");
print(f"O gráfico representando a modalidade presencial apresenta uma distibuição assimétrica negativa, uma vez que a mediana está perto do terceiro quartil, indicando que a média ({mediaCompespePresencial}) é menor que a mediana ({medianaCompespePresencial})");
print(f"Já no gráfico da modalidade EAD também existe uma distribuição assimétrica negativa, indicando que a média ({mediaCompespeEAD}) é menor que a mediana ({medianaCompespeEAD})");
print(f"Na modalidade presencial apresenta notas acima ({outlierMaximoCompespePresencial}) do valor máximo esperado ({valorMaximoCompespePresencial})");
print(f"Na modalidade EAD também apresenta notas acima ({outlierMaximoCompespeEAD}) do valor máximo esperado ({valorMaximoCompespeEAD}) e notas abaixo ({outlierMinimoCompespeEAD}) do valor mínimo esperado ({valorMinimoCompespeEAD})");
