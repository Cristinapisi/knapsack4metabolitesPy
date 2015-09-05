__author__ = 'Cristina'

"""
Run this with python.
 - run_locally is used to search for solutions from console for a pair mass and tolerance
  for example, for Glucose, you would enter mass 180.06338811828 and tolerance 0 or 1 and expect C6H12O6
 - run_tests is used to search for solutions for a set of pairs of mass and tolerance, stored in a file, one pair per line, separated by a ','
    for example, look at Small.txt
 - run_for_frank will work with the framework in which this will be integrated, called FRANK

Parameters:
 - what function to use:
        - exhaustive_search
        - knapsack  (not yet, TO DO)
        (presumably soon opting in or out of 7 golden rules)
        (maybe other variations in the future)
 - in and out files where appropriate
 - a delta which is set below as the computation error allowed.
    At the moment it is set at the lowest value that does not affect the correctness of results
    This is not the tolerance value for measurement errors, as those vary among experiments.
    This is to cope with the limitations of python for high precision floats equality.

"""

import os
import datetime
from solvers import exhaustive_search, exhaustive_search_7rules, greedy, greedy_7rules, knapsack, knapsack_7rules
from functions import get_formula_string, solve, read_file, get_output_folder

solvers_basic = \
    {'exhaustive': exhaustive_search,
     'greedy': greedy,
     'knapsack': knapsack}

solvers_7rules = \
    {'exhaustive_7rules': exhaustive_search_7rules,
     'greedy_7rules': greedy_7rules,
     'knapsack_7rules': knapsack_7rules}

solvers_all = {}
solvers_all.update(solvers_basic)
solvers_all.update(solvers_7rules)

# computation error allowed
delta = 0.00000000001

incorrect_input = "Nope, not what I asked you to enter"


def run_locally(function, delta):
    """
    Run from console
    Enter manually: 1 mass and 1 tolerance (in ppm)
    :return: print formulas
    """

    try:
        mass = float(input("Enter a mass: "))
        tolerance = float(input("Enter a tolerance (in ppm): ")) / 1000000
        t1 = datetime.datetime.utcnow()
        formulas = function.search(mass, tolerance, delta)
        t2 = datetime.datetime.utcnow()
        for formula in formulas:
            print get_formula_string(formula)
        print "Search time: " + str(t2 - t1)
    except SyntaxError:
        print incorrect_input
    except NameError:
        print incorrect_input


def run_for_file(filein, location, restrict):
    data_in = read_file(os.path.join(location, filein))
    output_folder = get_output_folder(filein, "output_files", restrict)
    for solver in solvers_all:
        solve(data_in, delta, restrict, solvers_all[solver], False, os.path.join(output_folder, solver + '.txt'))
    for solver in solvers_basic:
        solve(data_in, delta, restrict, solvers_basic[solver], True,
              os.path.join(output_folder, solver + '_post_7rules' + '.txt'))


def run_for_frank():
    """
    TO DO
    :return:
    """


if __name__ == '__main__':
    # run_locally(solvers_list['exhaustive'], delta)
    # run_locally(solvers_list['greedy'], delta)
    # run_locally(solvers_list['greedy_7rules'], delta)
    # run_locally(solvers_list['knapsack'], delta)
    # run_locally(solvers_list['knapsack_7rules'], delta)

    # data_in = read_file('testingthis.txt')
    # run_tests(data_in, exhaustive_search, True, 'thisresult.txt', delta, True)

    # run with just CHNOPS
    run_for_file("Small.txt", "input_files", True)
    run_for_file("Medium.txt", "input_files", True)
    run_for_file("Large.txt", "input_files", True)
    # run with all elements in the periodic_table
    run_for_file("Small.txt", "input_files", False)
    run_for_file("Medium.txt", "input_files", False)
    run_for_file("Large.txt", "input_files", False)

    # run_for_frank()
    print "Done"
