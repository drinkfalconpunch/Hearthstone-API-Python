import requests

from .base import HearthstoneBase
from .mixins import APIMixin

class CardBase(HearthstoneBase):
    def __init__(self, **attributes):
        super().__init__(**attributes)


class HearthstoneCard(APIMixin):
    def __init__(self, api_key, api_url, locale='enUS', **kwargs):
        if api_key is None:
            raise AttributeError('API key not found.')
        self.api_key = api_key
        self.cardback = kwargs.pop('cardback', None)
        self.cardbacks = self._get_card_backs()

    def _get_cardbacks(self, callback=None):
        request = self.get_asset('cardbacks', header=self.header)
        cardbacks = list()
        for cardback in request:
            cardbacks.append(Cardback(**cardback))
        return cardbacks