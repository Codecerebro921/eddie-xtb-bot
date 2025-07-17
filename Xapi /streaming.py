import websocket
import json
import threading

class StreamingClient:
    def __init__(self, stream_url, stream_session_id):
        self.url = f"{stream_url}/stream/{stream_session_id}"
        self.ws = None

    def connect(self):
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.daemon = True
        self.thread.start()

    def subscribe_prices(self, symbol):
        self.ws.send(json.dumps({
            "command": "getTickPrices",
            "symbol": symbol
        }))

    def on_message(self, ws, message):
        print(f"Message received: {message}")

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws):
        print("Streaming connection closed.")
