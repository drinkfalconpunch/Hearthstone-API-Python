from urllib.parse import urljoin
import requests

from .const import HEARTHSTONE_URL

class APIMixin(object):
    def _get_api_url(self, asset):
        return urljoin(HEARTHSTONE_URL, asset)

    def get_asset(self, asset, header, params=None, callback=None):
        url = self._get_api_url(asset)
        return requests.get(url, headers=header, params=params).json()