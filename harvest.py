############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    def __repr__(self):
        return '<{}>'.format(self.name)


# melon_info = [('musk', ...  ['mint'] ), ()]


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # for code, first_harvest, color...., pairings in melon_info:
    #     melon = MelonType(cpde....)
    #     melon.add_pairing(pairings)
    #     all_melon_types.append(melon)

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing(['mint'])
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing(['mint', 'strawberries'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing(['prosciutto'])
    all_melon_types.append(crenshaw)

    ywater = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    ywater.add_pairing(['ice cream'])
    all_melon_types.append(ywater)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "{} pairs with".format(melon.name)
        for pair in melon.pairings:
            print "- {}".format(pair)
        print


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    codes = {}

    for melon in melon_types:
        codes[melon.code] = melon

    return codes

############
# Part 2   #
############

harvest_info = [('yw', 8, 7, 'Field 2', 'Sheila'),
              ('yw', 3, 4, 'Field 2', 'Sheila'),
              ('yw', 9, 8, 'Field 3', 'Sheila'),
              ('cas', 10, 6, 'Field 35', 'Sheila'),
              ('cren', 8, 9, 'Field 35', 'Michael'),
              ('cren', 8, 2, 'Field 35', 'Michael'),
              ('cren', 2, 3, 'Field 4', 'Michael'),
              ('musk', 6, 7, 'Field 4', 'Michael'),
              ('yw', 7, 10, 'Field 3', 'Sheila')]


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melontype, shape, color, field, picker):
        self.melontype = melontype
        self.shape = shape
        self.color = color
        self.field = field
        self.picker = picker

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.field != "Field 3":
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    all_melons = []
    melons_by_code = make_melon_type_lookup(melon_types)

    for code, shape, color, field, picker in harvest_info:
        melon = Melon(melons_by_code[code], shape, color, field, picker)
        all_melons.append(melon)

    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellability = "sellable"
        else:
            sellability = "not sellable"
        print ("{} harvested {} from {} and it is {}".
               format(melon.picker, melon.melontype.name, melon.field, sellability))


# print_pairing_info(make_melon_types())
# make_melon_type_lookup(make_melon_types())
melons = make_melons(make_melon_types())
get_sellability_report(melons)
