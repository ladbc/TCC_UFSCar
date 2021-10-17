# Autor: Leticia Amaral da Cunha    2021
# TCC Ufscar - Engenharia de Computação

from pandas import read_csv

loadData = read_csv('./Data/Simples_Carga_de_Energia_Dia_Hora_data.csv')
print(loadData.head())