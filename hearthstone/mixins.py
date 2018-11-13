import requests

from .const import HEARTHSTONE_URL
from .utils import slash_join

class APIMixin(object):
    # def __init__(self, header, locale, **kwargs):
    #     if api_key is None:
    #         raise AttributeError('API key not found.')
    #     self.header = header
    #     self.locale = locale
    #     self.callback = kwargs.pop('callback', None)

    def _get_api_url(self, *assets):
        return slash_join(HEARTHSTONE_URL, *assets)

    def _get_info(self, value=None, header=None):
        infos = self.get_asset('info', header=header)
        if value:
            setattr(self, value, infos[value])
        else:
            for value in infos.keys():
                setattr(self, value, infos[value])

    def _requests_get(self, url, header=None, params=None):
        return requests.get(url, headers=header, params=params).json()

    def get_cards(self, subclass=None, value=None, header=None, params=None, callback=None):
        url = self._get_api_url('cards', subclass, value)
        return self._requests_get(url, header, params)

    def get_asset(self, *assets, header=None, params=None, callback=None):
        url = self._get_api_url(*assets)
        return self._requests_get(url, header, params)


class CallbackMixin(object):
    def callback(self):
        pass