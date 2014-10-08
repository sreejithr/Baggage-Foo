"""
BaggageManager
--------------
@author: Sreejith R
"""
import re

from .state import BaggageState


class BaggageManager(object):
    """
    BaggageManager is delegated with all the logic which moves the baggage bins.
    """
    def __init__(self, num_of_bin_sets, bins_per_cart=2, bin_priority_order=None):
        self.num_of_bin_sets = num_of_bin_sets
        self.bins_per_cart = bins_per_cart
        self.bin_priority_order = bin_priority_order or ['A', 'B']

        # For use in methods which check whether a state is close to the desired
        # arrangement
        self.desired_arrangement = []
        for bin_label in self.bin_priority_order:
            self.desired_arrangement.extend([bin_label] * self.num_of_bin_sets)

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

    def is_goal(self, state):
        return ''.join(self.desired_arrangement) in state.text

    def distance_from_goal(self, state):
        empty_finder_regex = re.compile('\{}'.format(state.empty_token))
        possible_goal = ['*'] * len(empty_finder_regex.findall(state.text))
        possible_goal += self.desired_arrangement
        possible_goal += ['*'] * (len(state.text) - len(possible_goal))

        distance = 0
        for index, bin in enumerate(state.configuration):
            if bin != possible_goal[index]:
                distance += 1

        return distance

    def next_possible_states(self, state):
        # For each node, generate all possible single moves
        def make_new_state(state, src, dest):
            if self._is_valid_dest(state, dest):
                new_state = BaggageState(state.configuration, state.moves+1,
                                         state.bins_per_cart)
                new_state.move_baggage(src, dest)
                return new_state
            return False

        for src, _ in enumerate(state):
            if self._is_valid_src(state, src):
                for dest, _ in enumerate(state):
                    new_state = make_new_state(state, src, dest)
                    if new_state:
                        yield new_state

