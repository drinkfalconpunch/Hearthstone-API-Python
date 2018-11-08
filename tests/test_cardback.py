import vcr
import requests
import pytest

from credentials import api_key
from hearthstone import HearthstoneAPI


@vcr.use_cassette('tests/cassettes/test_cardback.yml')
def test_get_cardback_attributes(cardback_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.cardback.get_cardback_attributes(
        cardback_name)['name'] == 'Classic'


@vcr.use_cassette('tests/cassettes/test_cardback.yml')
def test_get_cardback_image(cardback_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.cardback.get_cardback_image(
        cardback_name
    ) == 'http://wow.zamimg.com/images/hearthstone/backs/original/Card_Back_Default.png'


@vcr.use_cassette('tests/cassettes/test_cardback.yml')
def test_get_cardback_image_animated(cardback_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.cardback.get_cardback_image_animated(
        cardback_name
    ) == 'http://wow.zamimg.com/images/hearthstone/backs/animated/Card_Back_Default.gif'


@vcr.use_cassette('tests/cassettes/test_cardback.yml')
def test_get_cardback_description(cardback_name='classic'):
    r = HearthstoneAPI(api_key=api_key)
    assert r.cardback.get_cardback_description(
        cardback_name) == 'The only card back you\'ll ever need.'
