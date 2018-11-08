import string

from .base import HearthstoneBase
from .mixins import APIMixin


class Card(HearthstoneBase):
    # CLASS_ATTRIBUTES = ('set', 'class', 'faction', 'quality', 'race', 'type',
    #                     'attack', 'collectible', 'cost', 'durability',
    #                     'health')
    CLASS_ATTRIBUTES = ('cardID', 'dbfID', 'name', 'cardSet', 'type',
                        'faction', 'rarity', 'cost', 'attack', 'health',
                        'text', 'flavor', 'artist', 'collectible', 'elite',
                        'race', 'playerClass', 'img', 'imgGole', 'locale',
                        'mechanics')

    def __init__(self, **attributes):
        super().__init__(CLASS_ATTRIBUTES, **attributes)


class HearthstoneCard(APIMixin):
    def __init__(self, header, locale, **kwargs):
        self.header = header
        self.locale = locale
        self.callback = kwargs.pop('callback', None)

    def _get_cards_by_set(self, card_set, params=None, callback=None):
        request = self.get_asset(
            'cards',
            'sets',
            string.capwords(card_set),
            header=self.header,
            params=params,
            callback=callback)
        return request

    def _find_cardback(self, cardback_name):
        if not cardback_name:
            return self.cardbacks
        if not isinstance(cardback_name, str):
            raise ValueError('Cardback name must be a string.')
        cardback_name = string.capwords(cardback_name)
        for back in self.cardbacks:
            if cardback_name == back.name:
                return back
        raise ValueError('Cardback name not found.')