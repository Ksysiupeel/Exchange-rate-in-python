class Request_failed(Exception):
    def __init__(self):
        super().__init__("the request has failed")