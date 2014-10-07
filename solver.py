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

    def heuristic(self, state):
        return 1

    def _add_to_open_set(self, state, priority):
        heappush(self.to_visit, (priority, state))

    def shortest_path_to_goal(self):
        self._traverse()
        path = []

        current = self.goal
        while current != self.start:
            current = self.came_from[current]
            path.insert(0, current)

        return path

    def _traverse(self):
        self._add_to_open_set(self.start, 0)

        while self.to_visit:
            current = self.to_visit.pop(0)
            
            if current == self.goal:
                return

            for next in self.baggage_manager.next_possible_states(current):
                new_cost = self.cost_so_far[current] + next.moves
                if next not in self.came_from.keys() or\
                   new_cost < self.cost_so_far[next]:
                    next.moves = current.moves + 1
                    self.cost_so_far[next] = new_cost
                    self.came_from[next] = current
                    priority = new_cost + self.heuristic(next)
                    self._add_to_open_set(next, priority)


if __name__ == '__main__':
    # Here, we generate the start state. For eg, for 2 bins:
    # ['*', '*', '*', '*', '*', 'B', 'A', 'B', 'A']
#    start = BaggageState(
#        [EMPTY_SPACE_TOKEN] * (self.num_of_bins+1) + []
#    )
    pass

