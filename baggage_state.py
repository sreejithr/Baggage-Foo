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
    def __getitem__(self, key):
        if type(key) is not int or key < 0:
            raise

        if len(state[key:key+self.bins_per_cart]) < 2:
            raise
        else:
            return state[key:key+self.bins_per_cart]

    def __iter__(self):
        i = 0
        while i < len(self.state):
            yield self.state[i:i+self.bins_per_cart]
            i += self.bins_per_cart
