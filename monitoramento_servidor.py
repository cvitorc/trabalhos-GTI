# Desenvolvido por Carlos Vitor - 09/12/2024

import random
import logging
import time
import pandas as pd
import matplotlib.pyplot as plt

# Configuração de limites e logs
ALERT_THRESHOLD = {"cpu": 90, "memory": 80, "disk": 85}  # Limites críticos
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Função para simular métricas do servidor
def simulate_server_metrics():
    return {
        "cpu": random.uniform(50, 100),  # Uso de CPU entre 50% e 100%
        "memory": random.uniform(30, 100),  # Uso de memória entre 30% e 100%
        "disk": random.uniform(20, 100),  # Uso de espaço em disco entre 20% e 100%
    }

# Função para verificar alertas
def check_alerts(metrics):
    for metric, value in metrics.items():
        if value > ALERT_THRESHOLD.get(metric, 100):  # Verifica se passa do limite
            logging.warning(f"ALERTA: {metric.upper()} alto - {value:.2f}%")

# Função para visualizar os dados em gráficos
def plot_metrics(data):
    df = pd.DataFrame(data)
    plt.plot(df["Hora"], df["CPU (%)"], label="CPU", marker="o")
    plt.plot(df["Hora"], df["Memória (%)"], label="Memória", marker="o")
    plt.plot(df["Hora"], df["Disco (%)"], label="Disco", marker="o")
    plt.xlabel("Hora")
    plt.ylabel("Uso (%)")
    plt.title("Métricas Simuladas do Servidor")
    plt.legend()
    plt.grid(True)
    plt.show()

# Função principal para monitoramento contínuo
def monitor_server():
    logging.info("Iniciando monitoramento de servidor simulado...")
    metrics_log = {"Hora": [], "CPU (%)": [], "Memória (%)": [], "Disco (%)": []}
    for _ in range(5):  # Limita a 5 iterações para facilitar testes
        metrics = simulate_server_metrics()
        hora_atual = time.strftime("%H:%M:%S")
        metrics_log["Hora"].append(hora_atual)
        metrics_log["CPU (%)"].append(metrics["cpu"])
        metrics_log["Memória (%)"].append(metrics["memory"])
        metrics_log["Disco (%)"].append(metrics["disk"])
        logging.info(f"Métricas do servidor: {metrics}")
        check_alerts(metrics)
        time.sleep(2)  # Intervalo de 2 segundos
    plot_metrics(metrics_log)

# Execução principal
if __name__ == "__main__":
    monitor_server()
