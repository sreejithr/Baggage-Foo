"""
Baggage Bin Problem using A* Algorithm
--------------------------------------
@author: Sreejith R
"""
from heapq import heappush

from .state import BaggageState
from .manager import BaggageManager

EMPTY_SPACE_TOKEN = '*'


class Solver(object):
    """
    Runs the A* algorithm to find the optimum moves.
    """
    def __init__(self, start):
        self.start = start
        self.goal = None
        self.baggage_manager = BaggageManager(start.num_of_bin_sets)

        self.to_visit = []
        self.cost_so_far = {self.start.text: 0}
        self.came_from = {self.start.text: None}

    def heuristic(self, state):
        """
        Lesser the heuristic, closer the given state is to the goal. Uses
        Manhattan distance.
        
        :type return: int
        """
        return self.baggage_manager.distance_from_goal(state)

    def _add_to_open_set(self, state, priority):
        """
        Open set is a priority queue maintained as a heap.
        """
        heappush(self.to_visit, (priority, state))

    def shortest_path_to_goal(self):
        """
        Finds the shortest path and returns the optimum moves as tuples. Eg:
        
        """
        # Traverse the states
        self._traverse()

        # Now retrace the path
        current = self.goal
        path = [current]
        while current != self.start:
            current = self.came_from[current.text]
            path.insert(0, current)

        unsigned_to_signed = len(path[-1].configuration)/2 - 1

        return [(each.src-unsigned_to_signed, each.dest-unsigned_to_signed) for
                each in path if each != self.start]

    def _traverse(self):
        closed_set = []
        self._add_to_open_set(self.start, 0)

        while self.to_visit:
            current = self.to_visit.pop(0)[1]

            if self.baggage_manager.is_goal(current):
                self.goal = current
                return

            for next in self.baggage_manager.next_possible_states(current):
                new_cost = self.cost_so_far[current.text] + next.moves

                # `next` should be unvisited and cost for this path should be
                # lesser than the previously calculated cost to get here.
                if next.text not in closed_set or new_cost <\
                   self.cost_so_far[next.text]:
                    # Change the move count of `next` such that it came from
                    # current
                    next.moves = current.moves + 1
                    self.cost_so_far[next.text] = new_cost
                    self.came_from[next.text] = current
                    closed_set.append(next.text)
                    priority = new_cost + self.heuristic(next)
                    self._add_to_open_set(next, priority)

