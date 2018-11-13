import vcr
import pytest

from credentials import api_key
from hearthstone import HearthstoneAPI

@vcr.use_cassette('tests/cassettes/test_sets.yml')
def test_get_card_set_is_wild(set_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.sets.get_card_set(set_name).wild == True

@vcr.use_cassette('tests/cassettes/test_sets.yml')
def test_get_card_set_is_standard(set_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.sets.get_card_set(set_name).standard == True