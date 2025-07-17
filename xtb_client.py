import json
from xapi import Client

def conectar_xtb():
    with open("creds.json") as f:
        creds = json.load(f)

    client = Client(
        user_id=creds["userId"],
        password=creds["password"],
        mode=creds["mode"]  # 'demo' o 'real'
    )

    client.login()
    print("✅ Conectado exitosamente a XTB DEMO")

    return client
