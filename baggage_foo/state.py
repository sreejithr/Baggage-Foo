"""
BaggageState
------------
@author: Sreejith R
"""
class BaggageState(object):
    """
    Represents state of baggage bins. Configuration is a mandatory argument to
    initialize. It is a list form of the state.

    Example configuration:
        ['*', '*', '*', '*', 'B', 'A', 'B', 'A']

    where '*' is empty space. You can specify custom empty space token using
    `empty_space_token`
    """
    def __init__(self, configuration, moves=0, bins_per_cart=2,
                 empty_space_token='*'):
        self.configuration = list(configuration)
        self.bins_per_cart = bins_per_cart
        self.empty_token = empty_space_token
        self.moves = moves
        self.src, self.dest = None, None

    @property
    def num_of_bin_sets(self):
        """
        Set of bins is a bin set. For eg, BA is a bin set.
        """
        num_of_baggages = len(self.configuration)/2
        return num_of_baggages/self.bins_per_cart

    def is_empty_at_index(self, index):
        """
        Checks whether the bin set at given index is empty. For eg, '**' is empty.
        """
        bins = self.configuration[index:index+self.bins_per_cart]
        if len(bins) != self.bins_per_cart:
            raise

        for each in bins:
            if each != self.empty_token:
                return False

        return True

    def replace(self, index, value):
        if len(value) != self.bins_per_cart:
            raise

        for offset in range(self.bins_per_cart):
            del self.configuration[index+offset]
            self.configuration.insert(index+offset, value[offset])

    def move_baggage(self, src, dest):
        # Replace destination with value of source
        self.replace(dest, self.configuration[src:src+self.bins_per_cart])

        # Replace source with empty space tokens
        self.replace(src, [self.empty_token] * self.bins_per_cart)

        # Record the moves that led to this state
        self.src, self.dest = src, dest

    @property
    def text(self):
        return ''.join(self.configuration)

    def __getitem__(self, key):
        """
        To support indexing like in a list
        """
        if type(key) is not int or key < 0:
            raise # TODO Custom exception

        if len(self.configuration[key:key+self.bins_per_cart]) < 2:
            raise # TODO Custom exception
        else:
            return self.configuration[key:key+self.bins_per_cart]

    def __iter__(self):
        """
        Object can be iterated. Yields self.configuration one by one
        """
        i = 0
        while i < len(self.configuration):
            bins = self.configuration[i:i+self.bins_per_cart]
            if len(bins) == self.bins_per_cart:
                yield bins
            i += 1

    def __eq__(self, other):
        return self.configuration == other.configuration

    def __str__(self):
        return ''.join(self.text)

    def __repr__(self):
        return ''.join(self.text)

