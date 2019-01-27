import vcr
import pytest

from . import HearthstoneSetup

class TestSetAPI(HearthstoneSetup):
    @vcr.use_cassette('tests/cassettes/test_sets.yml')
    def test_get_card_set_is_wild(self, set_name='classic'):
        assert self.hearthstone.sets.get_card_set(set_name).wild == True

    @vcr.use_cassette('tests/cassettes/test_sets.yml')
    def test_get_card_set_is_standard(self, set_name='classic'):
        assert self.hearthstone.sets.get_card_set(set_name).standard == True