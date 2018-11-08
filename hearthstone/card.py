import requests

from .base import HearthstoneBase
from .utils import slash_join


class CardBase(HearthstoneBase):
    def __init__(self, **attributes):
        super().__init__(**attributes)


class HearthstoneCard(object):
    def __init__(self, api_key, api_url, locale='enUS', **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self.api_key = api_key
        self.cardback = kwargs.pop('cardback', None)
        self.cardbacks = self._get_card_backs()

    def _get_card_backs(self, cardback=None):
        url = slash_join(self._HEARTHSTONE_URL, 'cardbacks')
        #f'cardbacks?callback={cardback}')
        return requests.get(url, headers=self.header, params=params).text