"""
Baggage Bin Problem using A* Algorithm
--------------------------------------
@author: Sreejith R
"""
from heapq import heappush

from .state import BaggageState
from .manager import BaggageManager

EMPTY_SPACE_TOKEN = '*'


class Astar(object):
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.baggage_manager = BaggageManager()

        self.to_visit = []
        self.cost_so_far = {self.start: 0}
        self.came_from = {self.start: None}
    pass

