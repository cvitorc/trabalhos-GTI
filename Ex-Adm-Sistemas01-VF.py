#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon nov  3 19:30:06 2024

@author: carlosvitor
"""

import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo do projeto de TI para analise de CPI e SPI
dados_projeto = {
    'Periodo': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'PV': [1000, 2000, 3000, 4000, 5000, 6000],  # Valor Planejado (Planned Value)
    'EV': [800, 2200, 2700, 3700, 4900, 6100],   # Valor Agregado (Earned Value)
    'AC': [900, 2100, 2800, 3900, 5000, 6200]    # Custo Real (Actual Cost)
}

# Criar DataFrame
df = pd.DataFrame(dados_projeto)

# Cálculos de EVA
df['CPI'] = df['EV'] / df['AC']  # Índice de Performance de Custo
df['SPI'] = df['EV'] / df['PV']  # Índice de Performance de Prazo

# Gráfico dos valores PV, EV e AC
plt.figure(figsize=(10, 5))
plt.plot(df['Periodo'], df['PV'], marker='o', label='Valor Planejado (PV)')
plt.plot(df['Periodo'], df['EV'], marker='o', label='Valor Agregado (EV)')
plt.plot(df['Periodo'], df['AC'], marker='o', label='Custo Real (AC)')
plt.title('Análise de Valor Agregado (EVA) - Projeto de TI')
plt.xlabel('Período')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)

# Salvando o gráfico como imagem
plt.savefig("EVA.png", format="png", dpi=300)


plt.show()

# Gráfico de CPI e SPI
plt.figure(figsize=(10, 5))
plt.plot(df['Periodo'], df['CPI'], marker='o', label='Índice de Performance de Custo (CPI)')
plt.plot(df['Periodo'], df['SPI'], marker='o', label='Índice de Performance de Prazo (SPI)')
plt.axhline(y=1, color='r', linestyle='--', label='Linha de Base (1.0)')
plt.title('Índices de Performance CPI e SPI')
plt.xlabel('Período')
plt.ylabel('Índice')
plt.legend()
plt.grid(True)

# Salvando o gráfico como imagem
plt.savefig("CPI.png", format="png", dpi=300)

plt.show()
