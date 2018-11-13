HEARTHSTONE_URL = 'https://omgvamp-hearthstone-v1.p.mashape.com/'

CARD_ATTRIBUTES = (
    'cardId', 'dbfId', 'name', 'cardSet', 'type', 'faction', 'rarity', 'cost',
    'attack', 'health', 'text', 'flavor', 'artist', 'collectible', 'elite', 'race',
    'playerClass', 'howToGetGold', 'img', 'imgGold', 'locale', 'mechanics'
)

CARDBACK_ATTRIBUTES = (
    'cardBackId', 'name', 'description', 'source', 'sourceDescription', 'enabled',
    'img', 'imgAnimated', 'sortCategory', 'sortOrder', 'locale'
)

SET_ATTRIBUTES = ('name', 'standard', 'wild')

VALID_CARD_SUBCLASSES = (
    'faction', 'races', 'qualities', 'types', 'factions', 'classes', 'sets', 'search'
)

CLASSES = (
    'Neutral', 'Mage', 'Druid', 'Warlock', 'Paladin', 'Rogue', 'Shaman', 'Hunter',
    'Priest', 'Warrior'
)

FACTIONS = ('Neutral', 'Horde', 'Alliance')

CLASS_ATTRIBUTES = ('set', 'class', 'faction', 'quality', 'race', 'type', 'attack',
    'collectible', 'cost', 'durability', 'health'
)

PARAMS = ('attack', 'collectible', 'cost', 'durability', 'health')