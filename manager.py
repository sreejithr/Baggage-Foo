"""
BaggageManager
--------------
@author: Sreejith R
"""
from .state import BaggageState

class BaggageManager(object):
    """
    BaggageManager is delegated with all the logic which moves the baggage bins.
    """
    def _is_valid_src(self, state, index):
        try:
            return not state.is_empty_at_index(index)
        except: # TODO: Catch custom exception
            return False

    def _is_valid_dest(self, state, index):
        try:
            return state.is_empty_at_index(index)
        except: # TODO: Catch custom exception
            return False

    def next_possible_states(self, state):
        # For each node, generate all possible single moves
        def make_new_state(state, src, dest):
            if self._is_valid_dest(state, dest):
                new_state = BaggageState(state, state.bins_per_cart)
                new_state.move_baggage(src, dest)
                return new_state
            return False

        for src, _ in enumerate(state):
            if self._is_valid_src(state, src):
                for dest, _ in enumerate(state):
                    new_state = make_new_state(state, src, dest)
                    yield new_state

