import unittest

from ..state import BaggageState

EMPTY_SPACE_TOKEN = '*'

class TestBaggageState(unittest.TestCase):
    def setUp(self):
        self.config_1 = ['*', '*', '*', '*', '*', 'B', 'A', 'B', 'A']
        self.iterresult_1 = [['*', '*'], ['*', '*'], ['*', '*'], ['*', '*'],
                         ['*', 'B'], ['B', 'A'], ['A', 'B'], ['B', 'A']]
        self.moveresult_1 = ['B', 'A', '*', '*', '*', '*', '*', 'B', 'A']
        self.b_state = BaggageState(self.config_1)


    def test_list_behavior(self):
        # Test if iteration yields expected result
        self.assertEqual([each for each in self.b_state], self.iterresult_1)
        # Test if list indexing works properly
        self.assertEqual(self.b_state[5], ['B', 'A'])

    def test_empty_checking(self):
        self.assertTrue(self.b_state.is_empty_at_index(1))
        self.assertFalse(self.b_state.is_empty_at_index(6))

    def test_baggage_movement(self):
        # Test movement to start
        self.b_state.move_baggage(5, 0)
        self.assertEqual(self.b_state.configuration, self.moveresult_1)

