import requests

from .const import HEARTHSTONE_URL
from .utils import slash_join

class APIMixin(object):
    def _get_api_url(self, *assets):
        return slash_join(HEARTHSTONE_URL, *assets)

    def _get_info(self, value=None, header=None):
        infos = self.get_asset('info', header=header)
        if value:
            setattr(self, value, infos[value])
        else:
            for value in infos.keys():
                setattr(self, value, infos[value])

    def get_asset(self, *assets, header=None, params=None, callback=None):
        url = self._get_api_url(*assets)
        return requests.get(url, headers=header, params=params).json()