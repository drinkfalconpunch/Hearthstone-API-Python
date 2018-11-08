from .cardback import HearthstoneCardback
from .authenticator import Authenticator

class HearthstoneAPI(object):
    API_LOCALES = ('enUS', 'enGB', 'deDE', 'esES', 'esMX', 'frFR', 'itIT',
                   'koKR', 'plPL', 'ptBR', 'ruRU', 'zhCN', 'zhTW', 'jaJP',
                   'thTH')

    def __init__(self, api_key=None, locale='enUS', **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self.auth = Authenticator(api_key)
        self._locale = locale

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        if locale not in self.API_LOCALES:
            raise ValueError(f'Invalid locale {locale}')
        self._locale = locale

    @property
    def cardback(self):
        return HearthstoneCardback(header=self.auth.header, locale=self._locale)
