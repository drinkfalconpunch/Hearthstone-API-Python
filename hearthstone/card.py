import requests

# from .hearthstone import HearthstoneAPI
from .utils import slash_join


class HearthstoneCard(object):
    def __init__(self, header, locale, **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self.api_key = api_key
        self.cardback = kwargs.pop('cardback', None)
        self.callback = kwargs.pop('callback', None)
        self.cardbacks = self._get_card_backs()

    def _get_card_backs(self, cardback=None):
        url = slash_join(self._HEARTHSTONE_URL, 'cardbacks')
        #f'cardbacks?callback={cardback}')
        return requests.get(url, headers=self.header).text