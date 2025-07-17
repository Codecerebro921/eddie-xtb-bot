import time
from datetime import datetime

def iniciar_eddie():
    print(f"[{datetime.now()}] Eddie inició correctamente en modo DEMO.")
    print("Esperando próximas instrucciones para operar...")

# Lógica principal
if __name__ == "__main__":
    iniciar_eddie()

    try:
        while True:
            print(f"[{datetime.now()}] Eddie está activo... monitoreando.")
            time.sleep(60)  # Espera 60 segundos
    except KeyboardInterrupt:
        print("Eddie fue detenido manualmente.")
