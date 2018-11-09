import string

from .base import HearthstoneBase
from .mixins import APIMixin
from .const import HEARTHSTONE_URL, CLASS_ATTRIBUTES


class Card(HearthstoneBase):
    def __init__(self, **attributes):
        super().__init__(CLASS_ATTRIBUTES, **attributes)


class HearthstoneCard(APIMixin):
    CLASS_ATTRIBUTES = ('set', 'class', 'faction', 'quality', 'race', 'type',
                        'attack', 'collectible', 'cost', 'durability',
                        'health')

    PARAMS = ('attack', 'collectible', 'cost', 'durability', 'health')

    def __init__(self, header, locale, **kwargs):
        self.header = header
        self.locale = locale
        self.callback = kwargs.pop('callback', None)

        factions = self._get_info('factions', self.header)
        # {'attack': None, 'collectible': None, 'cost': None, 'durability': None, 'health': None}

    def _get_cards_by_set(self, card_set, params=None, callback=None):
        if not isinstance(card_set, str):
            raise ValueError(f'Card set must be a string. {card_set}')
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

    CLASSES = ('Neutral', 'Mage', 'Druid', 'Warlock', 'Paladin', 'Rogue',
               'Shaman', 'Hunter', 'Priest', 'Warrior')

    FACTIONS = ('Neutral', 'Horde', 'Alliance')

    def _get_cards_by_faction(self, faction, params=None, callback=None):
        faction = string.capwords(faction)
        if faction not in self.FACTIONS:
            raise ValueError(f'Invalid faction. {faction}')
        return self.get_asset(
            'cards',
            'factions',
            faction,
            header=self.header,
            params=params,
            callback=callback)
