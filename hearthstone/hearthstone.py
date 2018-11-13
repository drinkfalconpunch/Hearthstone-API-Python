from .cardback import HearthstoneCardback
from .card import HearthstoneCard
from .mixins import APIMixin
from .authenticator import Authenticator
from .sets import HearthstoneSets


class HearthstoneAPI(APIMixin):
    def __init__(self, api_key=None, locale=None, **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self.auth = Authenticator(api_key)
        self._get_locales()
        self._locale = locale
        self._get_info('patch', self.auth.header)

    def _get_locales(self):
        setattr(self, 'locales', self._get_info('locales', header=self.auth.header))

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        if locale not in self.locales:
            raise ValueError(f'Invalid locale {locale}')
        self._locale = locale if locale else 'enUS'

    @property
    def cardback(self):
        return HearthstoneCardback(self.auth.header, locale=self.locale)

    @property
    def card(self):
        return HearthstoneCard(header=self.auth.header, locale=self.locale)

    @property
    def sets(self):
        return HearthstoneSets(header=self.auth.header, locale=self.locale)
