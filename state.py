"""
BaggageState
------------
@author: Sreejith R
"""
class BaggageState(object):
    """
    Represents state of baggage bins.
    """
    def __init__(self, configuration, bins_per_cart=2, empty_space_token='*'):
        self.configuration = configuration
        self.bins_per_cart = bins_per_cart
        self.empty_token = empty_space_token

    # TODO: See if required
    @property
    def count(self):
        return len(self.configuration)

    def is_empty_at_index(self, index):
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

    def __getitem__(self, key):
        if type(key) is not int or key < 0:
            raise

        if len(self.state[key:key+self.bins_per_cart]) < 2:
            raise
        else:
            return self.state[key:key+self.bins_per_cart]

    def __iter__(self):
        i = 0
        while i < len(self.state):
            yield self.state[i:i+self.bins_per_cart]
            i += self.bins_per_cart

