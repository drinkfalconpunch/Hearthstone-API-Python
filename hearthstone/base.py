class HearthstoneBase(object):
    def __init__(self, class_attributes, **attributes):
        self.class_attributes = class_attributes
        self._attributes = attributes
        self._initialize_attributes()

    def __repr__(self):
        parts = list()
        for key, value in self._class_attributes().items():
            parts.append(f'{key}: {value}')
        return ', '.join(parts)

    def _fetch(self, key):
        value = self._attributes[key]
        del self._attributes[key]
        return value

    def _fetch_or_not_set(self, key, default=None):
        if key not in self._attributes:
            return default
        return self._fetch(key)

    def _initialize_attributes(self):
        for attribute in self.class_attributes:
            setattr(self, attribute, self._fetch_or_not_set(attribute))

    def _class_attributes(self):
        class_attributes = dict()
        for attribute in self.class_attributes:
            class_attributes[attribute] = getattr(self, attribute)
        return class_attributes
