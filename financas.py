#!/bin/bash

import pandas as pd
import yfinance as yf
import numpy as np

# Baixar dados históricos de ações da Apple usando yfinance
df = yf.download("AAPL", start="2026-01-01", end="2026-08-31")
print(df.head())
print()
print(df.tail())
print()

# Calcular a média móvel simples de 20 dias
df['MA20'] = df['Close'].rolling(window=20).mean()
print(df[['Close', 'MA20']].tail())

print()
# Criar um programa que carrega um dataframe que tenha os nomes, idades e salários de funcionários, e calcula o salário médio por idade.
df_funcionarios = pd.DataFrame({
    'nome': ['Alice', 'Manel', 'Bob', 'Eva', 'Francis', 'Charlie', 'David', 'Grace', 'Hannah', 'Ian'],
    'idade': [25, 25, 30, 30, 30, 35, 35, 40, 40, 40],
    'salario': [50000, 35000, 65000, 58000, 60000, 70000, 75000, 80000, 83000, 90000]
})

salario_medio_por_idade = df_funcionarios.groupby('idade')['salario'].mean()
print(salario_medio_por_idade)

print()

print("Fim do programa.")
