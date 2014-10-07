import unittest

from ..manager import BaggageManager
from ..state import BaggageState


class TestBaggageManager(unittest.TestCase):
    def setUp(self):
        self.b_manager = BaggageManager()
        self.config_1 = ['*', '*', '*', '*', '*', 'B', 'A', 'B', 'A']
        self.possible_states_result = [
            ['*', 'B', '*', '*', '*', '*', 'A', 'B', 'A'],
            ['*', '*', 'B', '*', '*', '*', 'A', 'B', 'A'],
            ['*', '*', '*', 'B', '*', '*', 'A', 'B', 'A'],
            ['*', '*', '*', '*', '*', '*', 'A', 'B', 'A'],
            ['B', 'A', '*', '*', '*', '*', '*', 'B', 'A'],
            ['*', 'B', 'A', '*', '*', '*', '*', 'B', 'A'],
            ['*', '*', 'B', 'A', '*', '*', '*', 'B', 'A'],
            ['*', '*', '*', 'B', 'A', '*', '*', 'B', 'A'],
            ['A', 'B', '*', '*', '*', 'B', '*', '*', 'A'],
            ['*', 'A', 'B', '*', '*', 'B', '*', '*', 'A'],
            ['*', '*', 'A', 'B', '*', 'B', '*', '*', 'A'],
            ['*', '*', '*', 'A', 'B', 'B', '*', '*', 'A'],
            ['B', 'A', '*', '*', '*', 'B', 'A', '*', '*'],
            ['*', 'B', 'A', '*', '*', 'B', 'A', '*', '*'],
            ['*', '*', 'B', 'A', '*', 'B', 'A', '*', '*'],
            ['*', '*', '*', 'B', 'A', 'B', 'A', '*', '*']
        ]
        self.possible_states_result_b_states = [BaggageState(each) for each in
                                                self.possible_states_result]
        self.b_state = BaggageState(self.config_1)
    
    def test_is_valid_src(self):
        # Both bins empty
        self.assertFalse(self.b_manager._is_valid_src(self.b_state, 0))

        # One bin empty
        self.assertTrue(self.b_manager._is_valid_src(self.b_state, 4))

        # At the end. It should be invalid
        self.assertFalse(self.b_manager._is_valid_src(self.b_state, 8))

        # Fully Non-empty
        self.assertTrue(self.b_manager._is_valid_src(self.b_state, 6))

    def test_is_valid_dest(self):
        # Both bins empty
        self.assertTrue(self.b_manager._is_valid_dest(self.b_state, 0))

        # One bin empty
        self.assertFalse(self.b_manager._is_valid_dest(self.b_state, 4))

        # At the end. It should be invalid
        self.assertFalse(self.b_manager._is_valid_dest(self.b_state, 8))

        # Fully Non-empty
        self.assertFalse(self.b_manager._is_valid_dest(self.b_state, 6))

    def test_next_possible_states(self):
        result = list(self.b_manager.next_possible_states(self.b_state))

        # Check if expected number of states are generated
        success = True
        if len(self.possible_states_result_b_states) != len(result):
            success = False
        self.assertTrue(success)

        # Check if they are equal
        success = True
        for each in self.possible_states_result_b_states:
            if not each in result:
                success = False
        self.assertTrue(success)

