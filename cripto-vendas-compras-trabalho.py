""" desenvolvido por Carlos Vitor, dezembro de 2024 """
import logging
from pycoingecko import CoinGeckoAPI
import time

# Configurações
CONFIG = {
    "buy_margin": 0.95,  # Margem para compra
    "sell_margin": 1.05,  # Margem para venda
    "cryptos": ["bitcoin", "ethereum", "solana", "pendle", "ethervista"],
    "average_prices": {
       "bitcoin": 84157.91,
       "ethereum": 2159.89,
       "solana": 212.95,
       "pendle": 5.50,
       "ethervista": 44.23,
       "morpho": 2.20
    },
    "update_interval": 60  # Intervalo de atualização em segundos
}

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Funções
def initialize_api():
    """Inicializa a API da CoinGecko."""
    return CoinGeckoAPI()

def calculate_alert_prices(average_prices, buy_margin, sell_margin):
    """Calcula os preços de alerta para compra e venda."""
    alert_prices_buy = {crypto: avg * buy_margin for crypto, avg in average_prices.items()}
    alert_prices_sell = {crypto: avg * sell_margin for crypto, avg in average_prices.items()}
    return alert_prices_buy, alert_prices_sell

def fetch_current_prices(cg, cryptos):
    """Obtém os preços atuais das criptomoedas usando a API."""
    try:
        prices = cg.get_price(ids=",".join(cryptos), vs_currencies="usd")
        return {crypto: prices[crypto]["usd"] for crypto in cryptos}
    except Exception as e:
        logging.error(f"Erro ao buscar preços: {e}")
        return {}

def check_alerts(current_prices, alert_prices_buy, alert_prices_sell, average_prices):
    """Verifica se os preços atuais estão dentro dos limites de compra ou venda."""
    for crypto, price in current_prices.items():
        if price <= alert_prices_buy[crypto]:
            decrease_percent = ((average_prices[crypto] - price) / average_prices[crypto]) * 100
            logging.info(f"ALERTA: Comprar {crypto}. Preço atual: {price} (queda de {decrease_percent:.2f}%)")
        elif price >= alert_prices_sell[crypto]:
            increase_percent = ((price - average_prices[crypto]) / average_prices[crypto]) * 100
            logging.info(f"ALERTA: Vender {crypto}. Preço atual: {price} (aumento de {increase_percent:.2f}%)")

def monitor_prices(cg, config):
    """Monitora os preços das criptomoedas em intervalos regulares."""
    logging.info("Iniciando monitoramento de preços.")
    alert_prices_buy, alert_prices_sell = calculate_alert_prices(
        config["average_prices"], config["buy_margin"], config["sell_margin"]
    )

    while True:
        current_prices = fetch_current_prices(cg, config["cryptos"])
        if current_prices:
            check_alerts(current_prices, alert_prices_buy, alert_prices_sell, config["average_prices"])
        time.sleep(config["update_interval"])
        print("\n")

# Execução principal
if __name__ == "__main__":
    cg = initialize_api()
    monitor_prices(cg, CONFIG)
