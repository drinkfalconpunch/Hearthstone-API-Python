from .mixins import APIMixin
import string
from .card import HearthstoneCard
from .const import SET_ATTRIBUTES
from .base import HearthstoneBase


class HearthstoneSet(HearthstoneBase):
    def __init__(self, **attributes):
        super(HearthstoneSet, self).__init__(SET_ATTRIBUTES, **attributes)
        self._initialize_cards(attributes.pop('cards', None))

    def _initialize_cards(self, cards=None):
        card_set = list()
        if cards is not None:
            for card in cards:
                card_set.append(HearthstoneCard(**card))
        setattr(self, 'cards', card_set)

class HearthstoneSets(APIMixin):
    def __init__(self, header=None):
        self.header = header
        self._initialize_sets()

    def _initialize_sets(self):
        self._get_info('sets', header=self.header)
        self._get_info('standard', header=self.header)
        self._get_info('wild', header=self.header)

    def _is_name_valid(self, set_name):
        if set_name not in self.sets:
            raise ValueError(f'Invalid set name. {set_name}')

    def _is_set_wild(self, set_name):
        if set_name in self.wild:
            return True
        return False

    def _is_set_standard(self, set_name):
        if set_name in self.standard:
            return True
        return False

    def _get_card_set(self, set_name, params=None):
        set_name = string.capwords(set_name)
        self._is_name_valid(set_name)

        return self.get_cards(subclass='sets', value=set_name, header=self.header, params=params)

    def get_card_set(self, set_name):
        set_name = string.capwords(set_name)
        self._is_name_valid(set_name)

        standard = self._is_set_standard(set_name)
        wild = self._is_set_wild(set_name)
        cards = self._get_card_set(set_name)

        return HearthstoneSet(set_name=set_name, standard=standard, wild=wild, cards=cards)