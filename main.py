from datetime import datetime
import time
from xtb_client import conectar_xtb

def iniciar_eddie():
    print(f"[{datetime.now()}] 🧠 Eddie ha iniciado.")
    client = conectar_xtb()

    # Símbolo a monitorear (puedes cambiar a US.NVDA o US.AAPL)
    symbol = "US.AMD"

    try:
        tick = client.get_symbol(symbol)
        print(f"📈 Precio actual de {symbol}: Ask = {tick['ask']} / Bid = {tick['bid']}")
    except Exception as e:
        print(f"❌ Error al obtener precio de {symbol}: {e}")

    return client

if __name__ == "__main__":
    client = iniciar_eddie()

    try:
        while True:
            print(f"[{datetime.now()}] Eddie está monitoreando el mercado...")
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Eddie fue detenido manualmente.")
