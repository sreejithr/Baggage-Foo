"""
BaggageState
------------
@author: Sreejith R
"""
class BaggageState(object):
    """
    Represents state of baggage bins.
    """
    def __init__(self, state, bins_per_cart=2, empty_space_token='_'):
        self.state = state
        self.bins_per_cart = bins_per_cart
        self.empty_token = empty_space_token

    @property
    def count(self):
        return len(self.state)

    def is_empty_at_index(self, index):
        for each in self.state[index:index+self.bins_per_cart]:
            if each != self.empty_token:
                return False
        return True

    def move_baggage(self, src, dest):
        self.state[dest:dest+self.bins_per_cart] =\
                                self.state[src:src+self.bins_per_cart]
        self.state[dest:dest+self.bins_per_cart] =\
                                [self.empty_token] * self.bins_per_cart

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
