from .mixins import APIMixin
import string


class HearthstoneSet(object):
    def __init__(self, name=None, standard=False, wild=False, cards=None):
        self.standard = standard
        self.wild = wild
        self.name = name
        self.cards = cards


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

        return self.get_asset('cards', 'sets', set_name, header=self.header, params=params)

    def get_card_set(self, set_name):
        set_name = string.capwords(set_name)
        self._is_name_valid(set_name)

        standard = self._is_set_standard(set_name)
        wild = self._is_set_wild(set_name)
        cards = self._get_card_set(set_name)

        return HearthstoneSet(set_name, standard, wild, cards)