class HearthstoneBase(object):
    CLASS_ATTRIBUTES = ()

    def __init__(self, **attributes):
        self._attributes = attributes
        self._initialize_attributes()

    def _fetch(self, key):
        value = self._attributes[key]
        del self._attributes[key]
        return value

    def _fetch_or_not_set(self, key, default=None):
        if key not in self._attributes:  # Passed in values have the highest priority
            return default
        return self._fetch(key)

    def _initialize_attributes(self):
        for attribute in self.CLASS_ATTRIBUTES:
            setattr(self, attribute, self._fetch_or_not_set(attribute))

    def _class_attributes(self):
        class_attributes = dict()
        for attribute in self.CLASS_ATTRIBUTES:
            class_attributes[attribute] = getattr(self, attribute)
        return class_attributes