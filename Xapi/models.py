class LoginResponse:
    def __init__(self, streamSessionId, status, **kwargs):
        self.streamSessionId = streamSessionId
        self.status = status
