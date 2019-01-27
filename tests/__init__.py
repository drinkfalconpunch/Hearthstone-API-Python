import vcr
import pytest

try:
    from hearthstone import HearthstoneAPI
except:
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
    from hearthstone import HearthstoneAPI

from credentials import api_key

class HearthstoneSetup(object):
    def setup(self):
        self.hearthstone = HearthstoneAPI(api_key=api_key)