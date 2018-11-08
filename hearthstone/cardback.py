import requests
import string

from .utils import slash_join
from .base import HearthstoneBase


class Cardback(HearthstoneBase):
    CLASS_ATTRIBUTES = ('cardBackId', 'name', 'description', 'source',
                        'sourceDescription', 'enabled', 'img', 'imgAnimated',
                        'sortCategory', 'sortOrder', 'locale')

    def __init__(self, **attributes):
        super(Cardback, self).__init__(**attributes)

    def _cardback_attributes(self):
        return self._class_attributes()

    def _cardback_image(self):
        return getattr(self, 'img')

    def _cardback_image_animated(self):
        return getattr(self, 'imgAnimated')

    def _cardback_name(self):
        return getattr(self, 'name')

    def _cardback_description(self):
        return getattr(self, 'description')


class HearthstoneCardback(object):
    def __init__(self, api_key, api_url, locale='enUS', **kwargs):
        self.api_key = api_key
        self.api_url = api_url
        self.header = {'X-Mashape-Key': self.api_key}
        self.callback = kwargs.pop('callback', None)
        self.cardbacks = self._get_cardbacks()

    def _get_cardbacks(self):
        url = slash_join(self.api_url, 'cardbacks')
        #f'cardbacks?callback={cardback}')
        request = requests.get(url, headers=self.header).json()
        cardbacks = list()
        for cardback in request:
            cardbacks.append(Cardback(**cardback))
        return cardbacks

    def _find_card(self, cardback_name):
        if not cardback_name:
            return self.cardbacks
        if not isinstance(cardback_name, str):
            raise ValueError('Cardback name must be a string.')
        cardback_name = string.capwords(cardback_name)
        for back in self.cardbacks:
            if cardback_name == back.name:
                return back
        raise ValueError('Cardback name not found.')

    def get_cardback_attributes(self, cardback_name=None):
        return self._find_card(cardback_name)._cardback_attributes()

    def get_cardback_image(self, cardback_name=None):
        return self._find_card(cardback_name)._cardback_image()

    def get_cardback_image_animated(self, cardback_name=None):
        return self._find_card(cardback_name)._cardback_image_animated()

    def get_cardback_description(self, cardback_name=None):
        return self._find_card(cardback_name)._cardback_description()