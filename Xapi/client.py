import requests
from .exceptions import XTBClientError
from .models import LoginResponse

class Client:
    def __init__(self, host='https://xapi.xtb.com', client_id=None, password=None):
        self.host = host
        self.session = requests.Session()
        self.client_id = client_id
        self.password = password
        self.sid = None

    def login(self):
        payload = {
            "command": "login",
            "arguments": {
                "userId": self.client_id,
                "password": self.password
            }
        }
        response = self.session.post(self.host, json=payload).json()
        if not response['status']:
            raise XTBClientError("Login failed: " + response.get('errorDescr', 'No error description'))
        self.sid = response['streamSessionId']
        return LoginResponse(**response)

    def logout(self):
        return self._send_command("logout")

    def _send_command(self, command, arguments=None):
        payload = {
            "command": command,
            "arguments": arguments or {}
        }
        response = self.session.post(self.host, json=payload).json()
        if not response['status']:
            raise XTBClientError(response.get('errorDescr', 'Unknown error'))
        return response
