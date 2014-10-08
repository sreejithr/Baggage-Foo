import sys

from baggage_foo.state import BaggageState
from baggage_foo.solver import Solver

bins = ["B", "A"]
try:
    num_of_baggage_bins = int(sys.argv[1])
    baggage_arrangement = ['*'] * (2*num_of_baggage_bins) +\
                          bins * num_of_baggage_bins
    solver = Solver(BaggageState(baggage_arrangement))
    print '\n'.join(
        ["{} to {}".format(movement[0], movement[1]) for movement in
         solver.shortest_path_to_goal()]
    )
except ValueError:
    print "Provide the number of baggage bins. Usage:"
    print "\t./runner <number_of_baggage_bins>"

