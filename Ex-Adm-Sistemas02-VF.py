#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon nov  3 18:29:28 2024

@author: carlosvitor
"""

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios para o dashboard de KPIs
dados = {
    'Indicador': ['Uptime', 'Tempo de Resposta', 'Uso de CPU', 'Uso de Memória', 'Tickets Resolvidos', 'Tickets Abertos'],
    'Valor': [99.8, 200, 65, 70, 150, 10]  # Valores fictícios
}

# Convertendo para DataFrame
df = pd.DataFrame(dados)

# Configuração do Dashboard
fig, axs = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle("KPI Dashboard de Sistemas Computacionais", fontsize=16)

# Gráficos dos KPIs
axs[0, 0].barh(['Uptime'], [df['Valor'][0]], color='skyblue')
axs[0, 0].set_xlim(0, 100)
axs[0, 0].set_title('Uptime (%)')

axs[0, 1].bar(['Tempo de Resposta'], [df['Valor'][1]], color='orange')
axs[0, 1].set_ylim(0, 500)
axs[0, 1].set_title('Tempo de Resposta (ms)')

axs[0, 2].bar(['Uso de CPU'], [df['Valor'][2]], color='green')
axs[0, 2].set_ylim(0, 100)
axs[0, 2].set_title('Uso de CPU (%)')

axs[1, 0].barh(['Uso de Memória'], [df['Valor'][3]], color='purple')
axs[1, 0].set_xlim(0, 100)
axs[1, 0].set_title('Uso de Memória (%)')

axs[1, 1].bar(['Tickets Resolvidos'], [df['Valor'][4]], color='blue')
axs[1, 1].set_ylim(0, 200)
axs[1, 1].set_title('Tickets Resolvidos')

axs[1, 2].bar(['Tickets Abertos'], [df['Valor'][5]], color='red')
axs[1, 2].set_ylim(0, 50)
axs[1, 2].set_title('Tickets Abertos')

# Ajustes no layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Salvando o gráfico como imagem
plt.savefig("kpi_dashboard.png", format="png", dpi=300)

plt.show()
