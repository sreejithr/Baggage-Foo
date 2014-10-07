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
