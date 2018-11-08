from .cardback import HearthstoneCardback


class HearthstoneAPI(object):
    HEARTHSTONE_URL = 'https://omgvamp-hearthstone-v1.p.mashape.com/'
    API_LOCALES = ('enUS', 'enGB', 'deDE', 'esES', 'esMX', 'frFR', 'itIT',
                   'koKR', 'plPL', 'ptBR', 'ruRU', 'zhCN', 'zhTW', 'jaJP',
                   'thTH')

    def __init__(self, api_key=None, locale='enUS', **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self._api_key = api_key
        self.header = {'X-Mashape-Key': self._api_key}
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
        return HearthstoneCardback(
            api_key=self._api_key,
            api_url=self.HEARTHSTONE_URL,
            locale=self._locale)
