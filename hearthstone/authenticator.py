class Authenticator(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.header = {'X-Mashape-Key': self.api_key}