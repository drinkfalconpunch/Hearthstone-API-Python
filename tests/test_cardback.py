import vcr
import pytest

from . import HearthstoneSetup


class TestCardbackAPI(HearthstoneSetup):
    @vcr.use_cassette('tests/cassettes/test_cardback.yml')
    def test_get_cardback_attributes(self, cardback_name='classic'):
        assert self.hearthstone.cardback.get_cardback_attributes(cardback_name)['name'] == 'Classic'

    @vcr.use_cassette('tests/cassettes/test_cardback.yml')
    def test_get_cardback_image(self, cardback_name='classic'):
        assert self.hearthstone.cardback.get_cardback_image(cardback_name) == 'http://wow.zamimg.com/images/hearthstone/backs/original/Card_Back_Default.png'

    @vcr.use_cassette('tests/cassettes/test_cardback.yml')
    def test_get_cardback_image_animated(self, cardback_name='classic'):
        assert self.hearthstone.cardback.get_cardback_image_animated(cardback_name) == 'http://wow.zamimg.com/images/hearthstone/backs/animated/Card_Back_Default.gif'

    @vcr.use_cassette('tests/cassettes/test_cardback.yml')
    def test_get_cardback_description(self, cardback_name='classic'):
        assert self.hearthstone.cardback.get_cardback_description(
            cardback_name) == 'The only card back you\'ll ever need.'

    @vcr.use_cassette('tests/cassettes/test_cardback.yml')
    def test_get_cardback_none(self, cardback_name='random'):
        with pytest.raises(ValueError):
            self.hearthstone.cardback.get_cardback_description(cardback_name)
