import string

from .base import HearthstoneBase
# from .mixins import APIMixin
from .const import CARD_ATTRIBUTES


class HearthstoneCard(HearthstoneBase):
    def __init__(self, **attributes):
        super(HearthstoneCard, self).__init__(CARD_ATTRIBUTES, **attributes)


# class HearthstoneCardSet(APIMixin):

#     def __init__(self, header, locale, **kwargs):
#         self.header = header
#         self.locale = locale
#         self.callback = kwargs.pop('callback', None)

        # factions = self._get_info('factions', self.header)
        # {'attack': None, 'collectible': None, 'cost': None, 'durability': None, 'health': None}

    # def _get_cards_by_set(self, card_set, params=None, callback=None):
    #     if not isinstance(card_set, str):
    #         raise ValueError(f'Card set must be a string. {card_set}')
    #     request = self.get_asset(
    #         'cards',
    #         'sets',
    #         string.capwords(card_set),
    #         header=self.header,
    #         params=params,
    #         callback=callback)
    #     return request

    # def _find_cardback(self, cardback_name):
    #     if not cardback_name:
    #         return self.cardbacks
    #     if not isinstance(cardback_name, str):
    #         raise ValueError('Cardback name must be a string.')
    #     cardback_name = string.capwords(cardback_name)
    #     for back in self.cardbacks:
    #         if cardback_name == back.name:
    #             return back
    #     raise ValueError('Cardback name not found.')

    # def _get_cards_by_faction(self, faction, params=None, callback=None):
    #     faction = string.capwords(faction)
    #     if faction not in self.FACTIONS:
    #         raise ValueError(f'Invalid faction. {faction}')
    #     return self.get_asset(
    #         'cards',
    #         'factions',
    #         faction,
    #         header=self.header,
    #         params=params,
    #         callback=callback)

        # for key, value in card.enumerate():

    # def _get_card_set(self, set_name, params=None):
    #     set_name = string.capwords(set_name)
    #     self._is_name_valid(set_name)

    #     return self.get_cards(subclass='sets', subvalue=set_name, header=self.header, params=params)