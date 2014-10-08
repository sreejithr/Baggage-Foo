import unittest

from ..state import BaggageState
from ..solver import Solver


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.config_1 = ['*', '*', '*', '*', '*', '*',
                         'B', 'A', 'B', 'A', 'B', 'A']
        self.config_2 = ['*', '*', '*', '*', '*', '*', '*', '*',
                         'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A']
        self.config_3 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*',
                         'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A']
        self.start_1 = BaggageState(self.config_1)
        self.start_2 = BaggageState(self.config_2)
        self.start_3 = BaggageState(self.config_3)

    def test_add_to_open_set(self):
        solver = Solver(self.start_1)
        solver._add_to_open_set(self.start_1, 0)
        self.assertEqual(solver.to_visit, [(0, self.start_1)])

    def test_heuristic(self):
        pass

    def test_shortest_path_to_goal(self):
        solver = Solver(self.start_1)
        print [(each.src, each.dest) for each in solver.shortest_path_to_goal()]

